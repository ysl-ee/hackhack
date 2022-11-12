# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Implementation of update command for updating bucket settings."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.storage import cloud_api
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.storage import flags
from googlecloudsdk.command_lib.storage import user_request_args_factory
from googlecloudsdk.command_lib.storage import wildcard_iterator
from googlecloudsdk.command_lib.storage.tasks import task_executor
from googlecloudsdk.command_lib.storage.tasks import task_graph_executor
from googlecloudsdk.command_lib.storage.tasks import task_status
from googlecloudsdk.command_lib.storage.tasks.buckets import update_bucket_task


_CORS_HELP_TEXT = """
Sets the Cross-Origin Resource Sharing (CORS) configuration on a bucket.
An example CORS JSON document looks like the following:

  [
    {
      "origin": ["http://origin1.example.com"],
      "responseHeader": ["Content-Type"],
      "method": ["GET"],
      "maxAgeSeconds": 3600
    }
  ]

For more information about supported endpoints for CORS, see
[Cloud Storage CORS support]
(https://cloud.google.com/storage/docs/cross-origin#server-side-support).
"""
_LABELS_HELP_TEXT = """
Sets the label configuration for the bucket. An example label JSON document
looks like the following:

  {
    "your_label_key": "your_label_value",
    "your_other_label_key": "your_other_label_value"
  }
"""
_LIFECYCLE_HELP_TEXT = """
Sets the lifecycle management configuration on a bucket. For example,
The following lifecycle management configuration JSON document
specifies that all objects in this bucket that are more than 365 days
old are deleted automatically:

  {
    "rule":
    [
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
"""


def _add_common_args(parser):
  """Register flags for this command.

  Args:
    parser (argparse.ArgumentParser): The parser to add the arguments to.

  Returns:
    buckets update flag group
  """
  parser.add_argument(
      'url', nargs='+', type=str, help='URLs of the buckets to update.')
  cors = parser.add_mutually_exclusive_group()
  cors.add_argument('--cors-file', help=_CORS_HELP_TEXT)
  cors.add_argument(
      '--clear-cors',
      action='store_true',
      help="Clears the bucket's CORS settings.")
  parser.add_argument(
      '--default-storage-class',
      help='Sets the default storage class for the bucket.')
  default_encryption_key = parser.add_mutually_exclusive_group()
  default_encryption_key.add_argument(
      '--default-encryption-key',
      help='Set the default KMS key for the bucket.')
  default_encryption_key.add_argument(
      '--clear-default-encryption-key',
      action='store_true',
      help="Clears the bucket's default encryption key.")
  parser.add_argument(
      '--enable-autoclass',
      action=arg_parsers.StoreTrueFalseAction,
      help='The Autoclass feature automatically selects the best storage class'
      ' for objects based on access patterns.')
  labels = parser.add_mutually_exclusive_group()
  labels.add_argument('--labels-file', help=_LABELS_HELP_TEXT)
  update_labels = labels.add_group()
  update_labels.add_argument(
      '--update-labels',
      metavar='LABEL_KEYS_AND_VALUES',
      type=arg_parsers.ArgDict(),
      help='Add or update labels. Example:'
      ' --update-labels=key1=value1,key2=value2')
  update_labels.add_argument(
      '--remove-labels',
      metavar='LABEL_KEYS',
      type=arg_parsers.ArgList(),
      help='Remove labels by their key names.')
  labels.add_argument(
      '--clear-labels',
      action='store_true',
      help='Clear all labels associated with a bucket.')
  lifecycle = parser.add_mutually_exclusive_group()
  lifecycle.add_argument('--lifecycle-file', help=_LIFECYCLE_HELP_TEXT)
  lifecycle.add_argument(
      '--clear-lifecycle',
      action='store_true',
      help='Removes all lifecycle configuration for the bucket.')
  log_bucket = parser.add_mutually_exclusive_group()
  log_bucket.add_argument(
      '--log-bucket',
      help='Enables usage logging of the bucket, outputting log files to the'
      " specified logging_bucket in this flag. Cloud Storage doesn't validate"
      ' the existence of the bucket receiving logs. In addition to enabling'
      ' logging on your bucket, you will also need to grant'
      ' cloud-storage-analytics@google.com write access to the log bucket.')
  log_bucket.add_argument(
      '--clear-log-bucket',
      action='store_true',
      help="Clears logging bucket receiving the usage current bucket's data.")
  log_object_prefix = parser.add_mutually_exclusive_group()
  log_object_prefix.add_argument(
      '--log-object-prefix',
      help='Specifies the object prefix for logging activity to the log'
      ' bucket. The default prefix is the bucket name. All read and write'
      ' activity to objects in the bucket will be logged for objects matching'
      ' the prefix.')
  log_object_prefix.add_argument(
      '--clear-log-object-prefix',
      action='store_true',
      help='Clears prefix used to determine what usage data to send to'
      ' logging bucket.')
  public_access_prevention = parser.add_mutually_exclusive_group()
  public_access_prevention.add_argument(
      '--public-access-prevention',
      '--pap',
      action=arg_parsers.StoreTrueFalseAction,
      help='If True, sets public access prevention to "enforced".'
      ' If False, sets public access prevention to "inherited".'
      ' For details on how exactly public access is blocked, see:'
      ' http://cloud/storage/docs/public-access-prevention')
  public_access_prevention.add_argument(
      '--clear-public-access-prevention',
      '--clear-pap',
      action='store_true',
      help='Unsets the public access prevention setting on a bucket.',
  )
  parser.add_argument(
      '--requester-pays',
      action=arg_parsers.StoreTrueFalseAction,
      help='Allows you to configure a Cloud Storage bucket so that the'
      ' requester pays all costs related to accessing the bucket and its'
      ' objects.')
  parser.add_argument(
      '--versioning',
      action=arg_parsers.StoreTrueFalseAction,
      help='Allows you to configure a Cloud Storage bucket to keep old'
      ' versions of objects.')
  web_main_page_suffix = parser.add_mutually_exclusive_group()
  web_main_page_suffix.add_argument(
      '--web-main-page-suffix',
      help='Cloud Storage allows you to configure a bucket to behave like a'
      ' static website. A subsequent GET bucket request through a custom'
      ' domain serves the specified "main" page instead of performing the'
      ' usual bucket listing.')
  web_main_page_suffix.add_argument(
      '--clear-web-main-page-suffix',
      action='store_true',
      help='Clear website main page suffix if bucket is hosting website.')
  web_error_page = parser.add_mutually_exclusive_group()
  web_error_page.add_argument(
      '--web-error-page',
      help='Cloud Storage allows you to configure a bucket to behave like a'
      ' static website. A subsequent GET bucket request through a custom'
      ' domain for a non-existent object serves the specified error page'
      ' instead of the standard Cloud Storage error.')
  web_error_page.add_argument(
      '--clear-web-error-page',
      action='store_true',
      help='Clear website error page if bucket is hosting website.')
  flags.add_continue_on_error_flag(parser)
  flags.add_predefined_acl_flag(parser)


def _add_alpha_args(parser):
  """Register flags for the alpha version of this command.

  Args:
    parser (argparse.ArgumentParser): The parser to add the arguments to.

  Returns:
    buckets update flag group
  """
  retention_period = parser.add_mutually_exclusive_group()
  retention_period.add_argument(
      '--retention-period',
      help='Minimum [retention period](https://cloud.google.com'
      '/storage/docs/bucket-lock#retention-periods)'
      ' for objects stored in the bucket, for example'
      ' ``--retention-period=1Y1M1D5S\'\'. Objects added to the bucket'
      ' cannot be deleted until they\'ve been stored for the specified'
      ' length of time. Default is no retention period. Only available'
      ' for Cloud Storage using the JSON API.')
  retention_period.add_argument(
      '--clear-retention-period',
      action='store_true',
      help='Clears the object retention period for a bucket.')
  parser.add_argument(
      '--acl-file',
      hidden=True,
      help='Path to a local JSON or YAML formatted file containing a valid'
      ' policy. The output of `gcloud storage buckets describe`'
      ' `--format="multi(acl:format=json)"` is a valid file and can be edited'
      ' for more fine-grained control.')
  parser.add_argument(
      '--add-acl-grant',
      hidden=True,
      help='JSON object in the format accepted by your cloud provider.'
      ' For example, for GCS, `--add-acl-grant=entity=user-tim@gmail.com,'
      'role=OWNER`')
  parser.add_argument(
      '--lock-retention-period',
      action=arg_parsers.StoreTrueFalseAction,
      help='Locks an unlocked retention policy on the buckets. Caution: A'
      ' locked retention policy cannot be removed from a bucket or reduced in'
      ' duration. Once locked, deleting the bucket is the only way to'
      ' "remove" a retention policy.')
  parser.add_argument(
      '--default-event-based-hold',
      action=arg_parsers.StoreTrueFalseAction,
      help='Sets the default value for an event-based hold on the bucket.'
      ' By setting the default event-based hold on a bucket, newly-created'
      ' objects inherit that value as their event-based hold (it is not'
      ' applied retroactively).')
  parser.add_argument(
      '--uniform-bucket-level-access',
      action=arg_parsers.StoreTrueFalseAction,
      help='Enables or disables [uniform bucket-level access]'
      '(https://cloud.google.com/storage/docs/bucket-policy-only)'
      ' for the buckets.')


def _is_initial_bucket_metadata_needed(user_request_args):
  """Determines if the bucket update has to patch existing metadata."""
  resource_args = user_request_args.resource_args
  if not resource_args:
    return False
  return any([
      resource_args.acl_grants_to_add, resource_args.acl_grants_to_remove,
      resource_args.labels_to_append, resource_args.labels_to_remove
  ])


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Update(base.Command):
  """Update bucket settings."""

  detailed_help = {
      'DESCRIPTION':
          """
      Update a bucket.
      """,
      'EXAMPLES':
          """

      The following command updates the default storage class of a Cloud Storage
      bucket named "my-bucket" to NEARLINE and sets requester pays to true:

        $ {command} gs://my-bucket --default-storage-class=NEARLINE --requester-pays
      """,
  }

  @staticmethod
  def Args(parser):
    _add_common_args(parser)

  def update_task_iterator(self, args):
    user_request_args = (
        user_request_args_factory.get_user_request_args_from_command_args(
            args, metadata_type=user_request_args_factory.MetadataType.BUCKET))
    if user_request_args_factory.modifies_full_acl_policy(user_request_args):
      # TODO(b/244621490): Add test when ACL flags are exposed.
      fields_scope = cloud_api.FieldsScope.FULL
    else:
      fields_scope = cloud_api.FieldsScope.NO_ACL
    for url in args.url:
      for resource in wildcard_iterator.get_wildcard_iterator(
          url,
          fields_scope=fields_scope,
          get_bucket_metadata=_is_initial_bucket_metadata_needed(
              user_request_args)):
        yield update_bucket_task.UpdateBucketTask(
            resource, user_request_args=user_request_args)

  def Run(self, args):
    task_status_queue = task_graph_executor.multiprocessing_context.Queue()
    self.exit_code = task_executor.execute_tasks(
        self.update_task_iterator(args),
        parallelizable=True,
        task_status_queue=task_status_queue,
        progress_manager_args=task_status.ProgressManagerArgs(
            increment_type=task_status.IncrementType.INTEGER,
            manifest_path=None),
        continue_on_error=args.continue_on_error,
    )


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class UpdateAlpha(Update):
  """Update bucket settings."""

  detailed_help = {
      'DESCRIPTION':
          """
      Update a bucket.
      """,
      'EXAMPLES':
          """

      The following command updates the retention period of a Cloud Storage
      bucket named "my-bucket" to one year and thirty-six minutes:

        $ {command} gs://my-bucket --retention-period=1y36m

      The following command clears the retention period of a bucket:

        $ {command} gs://my-bucket --clear-retention-period
      """,
  }

  @staticmethod
  def Args(parser):
    _add_common_args(parser)
    _add_alpha_args(parser)
