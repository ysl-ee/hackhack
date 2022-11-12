"""Generated message classes for run version v1alpha1.

Deploy and manage user provided container images that scale automatically
based on incoming requests. The Cloud Run Admin API v1 follows the Knative
Serving API specification, while v2 is aligned with Google Cloud AIP-based API
standards, as described in https://google.aip.dev/.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'run'


class DomainMapping(_messages.Message):
  r"""Resource to hold the state and status of a user's domain mapping. NOTE:
  This resource is currently in Beta.

  Fields:
    apiVersion: The API version for this call such as
      "domains.cloudrun.com/v1alpha1".
    kind: The kind of resource, in this case "DomainMapping".
    metadata: Metadata associated with this BuildTemplate.
    spec: The spec for this DomainMapping.
    status: The current status of the DomainMapping.
  """

  apiVersion = _messages.StringField(1)
  kind = _messages.StringField(2)
  metadata = _messages.MessageField('ObjectMeta', 3)
  spec = _messages.MessageField('DomainMappingSpec', 4)
  status = _messages.MessageField('DomainMappingStatus', 5)


class DomainMappingCondition(_messages.Message):
  r"""DomainMappingCondition contains state information for a DomainMapping.

  Fields:
    lastTransitionTime: Last time the condition transitioned from one status
      to another. +optional
    message: Human readable message indicating details about the current
      status. +optional
    reason: One-word CamelCase reason for the condition's current status.
      +optional
    severity: How to interpret failures of this condition, one of Error,
      Warning, Info +optional
    status: Status of the condition, one of True, False, Unknown.
    type: Type of domain mapping condition.
  """

  lastTransitionTime = _messages.StringField(1)
  message = _messages.StringField(2)
  reason = _messages.StringField(3)
  severity = _messages.StringField(4)
  status = _messages.StringField(5)
  type = _messages.StringField(6)


class DomainMappingSpec(_messages.Message):
  r"""The desired state of the Domain Mapping.

  Enums:
    CertificateModeValueValuesEnum: The mode of the certificate.

  Fields:
    certificateMode: The mode of the certificate.
    forceOverride: If set, the mapping will override any mapping set before
      this spec was set. It is recommended that the user leaves this empty to
      receive an error warning about a potential conflict and only set it once
      the respective UI has given such a warning.
    routeName: The name of the Knative Route that this DomainMapping applies
      to. The route must exist.
  """

  class CertificateModeValueValuesEnum(_messages.Enum):
    r"""The mode of the certificate.

    Values:
      CERTIFICATE_MODE_UNSPECIFIED: <no description>
      NONE: Do not provision an HTTPS certificate.
      AUTOMATIC: Automatically provisions an HTTPS certificate via GoogleCA or
        LetsEncrypt.
    """
    CERTIFICATE_MODE_UNSPECIFIED = 0
    NONE = 1
    AUTOMATIC = 2

  certificateMode = _messages.EnumField('CertificateModeValueValuesEnum', 1)
  forceOverride = _messages.BooleanField(2)
  routeName = _messages.StringField(3)


class DomainMappingStatus(_messages.Message):
  r"""The current state of the Domain Mapping.

  Fields:
    conditions: Array of observed DomainMappingConditions, indicating the
      current state of the DomainMapping.
    mappedRouteName: The name of the route that the mapping currently points
      to.
    observedGeneration: ObservedGeneration is the 'Generation' of the
      DomainMapping that was last processed by the controller. Clients polling
      for completed reconciliation should poll until observedGeneration =
      metadata.generation and the Ready condition's status is True or False.
    resourceRecords: The resource records required to configure this domain
      mapping. These records must be added to the domain's DNS configuration
      in order to serve the application via this domain mapping.
    url: Cloud Run fully managed: not supported Cloud Run on GKE: supported
      Holds the URL that will serve the traffic of the DomainMapping.
      +optional
  """

  conditions = _messages.MessageField('DomainMappingCondition', 1, repeated=True)
  mappedRouteName = _messages.StringField(2)
  observedGeneration = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  resourceRecords = _messages.MessageField('ResourceRecord', 4, repeated=True)
  url = _messages.StringField(5)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class ListDomainMappingsResponse(_messages.Message):
  r"""ListDomainMappingsResponse is a list of DomainMapping resources.

  Fields:
    apiVersion: The API version for this call such as
      "domains.cloudrun.com/v1alpha1".
    items: List of DomainMappings.
    kind: The kind of this resource, in this case "DomainMappingList".
    metadata: Metadata associated with this DomainMapping list.
    unreachable: Locations that could not be reached.
  """

  apiVersion = _messages.StringField(1)
  items = _messages.MessageField('DomainMapping', 2, repeated=True)
  kind = _messages.StringField(3)
  metadata = _messages.MessageField('ListMeta', 4)
  unreachable = _messages.StringField(5, repeated=True)


class ListMeta(_messages.Message):
  r"""Metadata for synthetic resources like List. In Cloud Run, all List
  Resources Responses will have a ListMeta instead of ObjectMeta.

  Fields:
    continue_: Continuation token is a value emitted when the count of items
      is larger than the user/system limit. To retrieve the next page of
      items, pass the value of `continue` as the next request's `page_token`.
    resourceVersion: Opaque string that identifies the server's internal
      version of this object. It can be used by clients to determine when
      objects have changed. If the message is passed back to the server, it
      must be left unmodified.
      https://git.k8s.io/community/contributors/devel/api-
      conventions.md#concurrency-control-and-consistency
    selfLink: URL representing this object.
  """

  continue_ = _messages.StringField(1)
  resourceVersion = _messages.StringField(2)
  selfLink = _messages.StringField(3)


class ObjectMeta(_messages.Message):
  r"""k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta is metadata that all
  persisted resources must have, which includes all objects users must create.

  Messages:
    AnnotationsValue: Unstructured key value map stored with a resource that
      may be set by external tools to store and retrieve arbitrary metadata.
      They are not queryable and should be preserved when modifying objects.
      In Cloud Run, annotations with 'run.googleapis.com/' and
      'autoscaling.knative.dev' are restricted, and the accepted annotations
      will be different depending on the resource type. *
      `autoscaling.knative.dev/maxScale`: Revision. *
      `autoscaling.knative.dev/minScale`: Revision. *
      `run.googleapis.com/binary-authorization-breakglass`: Service, Job, *
      `run.googleapis.com/binary-authorization`: Service, Job, Execution. *
      `run.googleapis.com/client-name`: All resources. *
      `run.googleapis.com/cloudsql-instances`: Revision, Execution. *
      `run.googleapis.com/cpu-throttling`: Revision. *
      `run.googleapis.com/custom-audiences`: Service. *
      `run.googleapis.com/description`: Service. *
      `run.googleapis.com/encryption-key-shutdown-hours`: Revision *
      `run.googleapis.com/encryption-key`: Revision, Execution. *
      `run.googleapis.com/execution-environment`: Revision, Execution. *
      `run.googleapis.com/gc-traffic-tags`: Service. *
      `run.googleapis.com/ingress`: Service. * `run.googleapis.com/network-
      interfaces`: Revision, Execution. * `run.googleapis.com/post-key-
      revocation-action-type`: Revision. * `run.googleapis.com/secrets`:
      Revision, Execution. * `run.googleapis.com/secure-session-agent`:
      Revision. * `run.googleapis.com/sessionAffinity`: Revision. *
      `run.googleapis.com/startup-cpu-boost`: Revision. *
      `run.googleapis.com/vpc-access-connector`: Revision, Execution. *
      `run.googleapis.com/vpc-access-egress`: Revision, Execution. Execution.
      More info: https://kubernetes.io/docs/user-guide/annotations
    LabelsValue: Map of string keys and values that can be used to organize
      and categorize (scope and select) objects. May match selectors of
      replication controllers and routes. More info:
      https://kubernetes.io/docs/user-guide/labels

  Fields:
    annotations: Unstructured key value map stored with a resource that may be
      set by external tools to store and retrieve arbitrary metadata. They are
      not queryable and should be preserved when modifying objects. In Cloud
      Run, annotations with 'run.googleapis.com/' and
      'autoscaling.knative.dev' are restricted, and the accepted annotations
      will be different depending on the resource type. *
      `autoscaling.knative.dev/maxScale`: Revision. *
      `autoscaling.knative.dev/minScale`: Revision. *
      `run.googleapis.com/binary-authorization-breakglass`: Service, Job, *
      `run.googleapis.com/binary-authorization`: Service, Job, Execution. *
      `run.googleapis.com/client-name`: All resources. *
      `run.googleapis.com/cloudsql-instances`: Revision, Execution. *
      `run.googleapis.com/cpu-throttling`: Revision. *
      `run.googleapis.com/custom-audiences`: Service. *
      `run.googleapis.com/description`: Service. *
      `run.googleapis.com/encryption-key-shutdown-hours`: Revision *
      `run.googleapis.com/encryption-key`: Revision, Execution. *
      `run.googleapis.com/execution-environment`: Revision, Execution. *
      `run.googleapis.com/gc-traffic-tags`: Service. *
      `run.googleapis.com/ingress`: Service. * `run.googleapis.com/network-
      interfaces`: Revision, Execution. * `run.googleapis.com/post-key-
      revocation-action-type`: Revision. * `run.googleapis.com/secrets`:
      Revision, Execution. * `run.googleapis.com/secure-session-agent`:
      Revision. * `run.googleapis.com/sessionAffinity`: Revision. *
      `run.googleapis.com/startup-cpu-boost`: Revision. *
      `run.googleapis.com/vpc-access-connector`: Revision, Execution. *
      `run.googleapis.com/vpc-access-egress`: Revision, Execution. Execution.
      More info: https://kubernetes.io/docs/user-guide/annotations
    clusterName: Not supported by Cloud Run
    creationTimestamp: UTC timestamp representing the server time when this
      object was created. More info:
      https://git.k8s.io/community/contributors/devel/api-
      conventions.md#metadata
    deletionGracePeriodSeconds: Not supported by Cloud Run
    deletionTimestamp: The read-only soft deletion timestamp for this
      resource. In Cloud Run, users are not able to set this field. Instead,
      they must call the corresponding Delete API.
    finalizers: Not supported by Cloud Run
    generateName: Not supported by Cloud Run
    generation: A system-provided sequence number representing a specific
      generation of the desired state.
    labels: Map of string keys and values that can be used to organize and
      categorize (scope and select) objects. May match selectors of
      replication controllers and routes. More info:
      https://kubernetes.io/docs/user-guide/labels
    name: Required. The name of the resource. In Cloud Run, name is required
      when creating top-level resources (Service, Job), must be unique within
      a Cloud Run project/region, and cannot be changed once created. More
      info: https://kubernetes.io/docs/user-guide/identifiers#names If
      ObjectMeta is part of a CreateServiceRequest, name must contain fewer
      than 50 characters.
    namespace: Required. Defines the space within each name must be unique
      within a Cloud Run region. In Cloud Run, it must be project ID or
      number.
    ownerReferences: Not supported by Cloud Run
    resourceVersion: Opaque, system-generated value that represents the
      internal version of this object that can be used by clients to determine
      when objects have changed. May be used for optimistic concurrency,
      change detection, and the watch operation on a resource or set of
      resources. Clients must treat these values as opaque and passed
      unmodified back to the server or omit the value to disable conflict-
      detection. More info:
      https://git.k8s.io/community/contributors/devel/sig-architecture/api-
      conventions.md#concurrency-control-and-consistency
    selfLink: URL representing this object.
    uid: Unique, system-generated identifier for this resource. More info:
      https://kubernetes.io/docs/user-guide/identifiers#uids
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class AnnotationsValue(_messages.Message):
    r"""Unstructured key value map stored with a resource that may be set by
    external tools to store and retrieve arbitrary metadata. They are not
    queryable and should be preserved when modifying objects. In Cloud Run,
    annotations with 'run.googleapis.com/' and 'autoscaling.knative.dev' are
    restricted, and the accepted annotations will be different depending on
    the resource type. * `autoscaling.knative.dev/maxScale`: Revision. *
    `autoscaling.knative.dev/minScale`: Revision. *
    `run.googleapis.com/binary-authorization-breakglass`: Service, Job, *
    `run.googleapis.com/binary-authorization`: Service, Job, Execution. *
    `run.googleapis.com/client-name`: All resources. *
    `run.googleapis.com/cloudsql-instances`: Revision, Execution. *
    `run.googleapis.com/cpu-throttling`: Revision. *
    `run.googleapis.com/custom-audiences`: Service. *
    `run.googleapis.com/description`: Service. *
    `run.googleapis.com/encryption-key-shutdown-hours`: Revision *
    `run.googleapis.com/encryption-key`: Revision, Execution. *
    `run.googleapis.com/execution-environment`: Revision, Execution. *
    `run.googleapis.com/gc-traffic-tags`: Service. *
    `run.googleapis.com/ingress`: Service. * `run.googleapis.com/network-
    interfaces`: Revision, Execution. * `run.googleapis.com/post-key-
    revocation-action-type`: Revision. * `run.googleapis.com/secrets`:
    Revision, Execution. * `run.googleapis.com/secure-session-agent`:
    Revision. * `run.googleapis.com/sessionAffinity`: Revision. *
    `run.googleapis.com/startup-cpu-boost`: Revision. *
    `run.googleapis.com/vpc-access-connector`: Revision, Execution. *
    `run.googleapis.com/vpc-access-egress`: Revision, Execution. Execution.
    More info: https://kubernetes.io/docs/user-guide/annotations

    Messages:
      AdditionalProperty: An additional property for a AnnotationsValue
        object.

    Fields:
      additionalProperties: Additional properties of type AnnotationsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a AnnotationsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Map of string keys and values that can be used to organize and
    categorize (scope and select) objects. May match selectors of replication
    controllers and routes. More info: https://kubernetes.io/docs/user-
    guide/labels

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  annotations = _messages.MessageField('AnnotationsValue', 1)
  clusterName = _messages.StringField(2)
  creationTimestamp = _messages.StringField(3)
  deletionGracePeriodSeconds = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  deletionTimestamp = _messages.StringField(5)
  finalizers = _messages.StringField(6, repeated=True)
  generateName = _messages.StringField(7)
  generation = _messages.IntegerField(8, variant=_messages.Variant.INT32)
  labels = _messages.MessageField('LabelsValue', 9)
  name = _messages.StringField(10)
  namespace = _messages.StringField(11)
  ownerReferences = _messages.MessageField('OwnerReference', 12, repeated=True)
  resourceVersion = _messages.StringField(13)
  selfLink = _messages.StringField(14)
  uid = _messages.StringField(15)


class OwnerReference(_messages.Message):
  r"""This is not supported or used by Cloud Run.

  Fields:
    apiVersion: This is not supported or used by Cloud Run.
    blockOwnerDeletion: This is not supported or used by Cloud Run.
    controller: This is not supported or used by Cloud Run.
    kind: This is not supported or used by Cloud Run.
    name: This is not supported or used by Cloud Run.
    uid: This is not supported or used by Cloud Run.
  """

  apiVersion = _messages.StringField(1)
  blockOwnerDeletion = _messages.BooleanField(2)
  controller = _messages.BooleanField(3)
  kind = _messages.StringField(4)
  name = _messages.StringField(5)
  uid = _messages.StringField(6)


class ResourceRecord(_messages.Message):
  r"""A DNS resource record.

  Enums:
    TypeValueValuesEnum: Resource record type. Example: `AAAA`.

  Fields:
    name: Relative name of the object affected by this record. Only applicable
      for `CNAME` records. Example: 'www'.
    rrdata: Data for this record. Values vary by record type, as defined in
      RFC 1035 (section 5) and RFC 1034 (section 3.6.1).
    type: Resource record type. Example: `AAAA`.
  """

  class TypeValueValuesEnum(_messages.Enum):
    r"""Resource record type. Example: `AAAA`.

    Values:
      RECORD_TYPE_UNSPECIFIED: An unknown resource record.
      A: An A resource record. Data is an IPv4 address.
      AAAA: An AAAA resource record. Data is an IPv6 address.
      CNAME: A CNAME resource record. Data is a domain name to be aliased.
    """
    RECORD_TYPE_UNSPECIFIED = 0
    A = 1
    AAAA = 2
    CNAME = 3

  name = _messages.StringField(1)
  rrdata = _messages.StringField(2)
  type = _messages.EnumField('TypeValueValuesEnum', 3)


class RunNamespacesDomainmappingsCreateRequest(_messages.Message):
  r"""A RunNamespacesDomainmappingsCreateRequest object.

  Fields:
    domainMapping: A DomainMapping resource to be passed as the request body.
    parent: The project ID or project number in which this domain mapping
      should be created.
  """

  domainMapping = _messages.MessageField('DomainMapping', 1)
  parent = _messages.StringField(2, required=True)


class RunNamespacesDomainmappingsDeleteRequest(_messages.Message):
  r"""A RunNamespacesDomainmappingsDeleteRequest object.

  Fields:
    apiVersion: Cloud Run currently ignores this parameter.
    kind: Cloud Run currently ignores this parameter.
    name: The name of the domain mapping being deleted. If needed, replace
      {namespace_id} with the project ID.
    orphanDependents: Deprecated. Specifies the cascade behavior on delete.
      Cloud Run only supports cascading behavior, so this must be false. This
      attribute is deprecated, and is now replaced with PropagationPolicy See
      https://github.com/kubernetes/kubernetes/issues/46659 for more info.
    propagationPolicy: Specifies the propagation policy of delete. Cloud Run
      currently ignores this setting, and deletes in the background. Please
      see kubernetes.io/docs/concepts/workloads/controllers/garbage-
      collection/ for more information.
  """

  apiVersion = _messages.StringField(1)
  kind = _messages.StringField(2)
  name = _messages.StringField(3, required=True)
  orphanDependents = _messages.BooleanField(4)
  propagationPolicy = _messages.StringField(5)


class RunNamespacesDomainmappingsGetRequest(_messages.Message):
  r"""A RunNamespacesDomainmappingsGetRequest object.

  Fields:
    name: The name of the domain mapping being retrieved. If needed, replace
      {namespace_id} with the project ID.
  """

  name = _messages.StringField(1, required=True)


class RunNamespacesDomainmappingsListRequest(_messages.Message):
  r"""A RunNamespacesDomainmappingsListRequest object.

  Fields:
    continue_: Optional encoded string to continue paging.
    fieldSelector: Allows to filter resources based on a specific value for a
      field name. Send this in a query string format. i.e.
      'metadata.name%3Dlorem'. Not currently used by Cloud Run.
    includeUninitialized: Not currently used by Cloud Run.
    labelSelector: Allows to filter resources based on a label. Supported
      operations are =, !=, exists, in, and notIn.
    limit: The maximum number of records that should be returned.
    parent: The project ID or project number from which the domain mappings
      should be listed.
    resourceVersion: The baseline resource version from which the list or
      watch operation should start. Not currently used by Cloud Run.
    watch: Flag that indicates that the client expects to watch this resource
      as well. Not currently used by Cloud Run.
  """

  continue_ = _messages.StringField(1)
  fieldSelector = _messages.StringField(2)
  includeUninitialized = _messages.BooleanField(3)
  labelSelector = _messages.StringField(4)
  limit = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  parent = _messages.StringField(6, required=True)
  resourceVersion = _messages.StringField(7)
  watch = _messages.BooleanField(8)


class RunNamespacesDomainmappingsReplaceDomainMappingRequest(_messages.Message):
  r"""A RunNamespacesDomainmappingsReplaceDomainMappingRequest object.

  Fields:
    domainMapping: A DomainMapping resource to be passed as the request body.
    name: The name of the domain mapping being retrieved. If needed, replace
      {namespace_id} with the project ID.
  """

  domainMapping = _messages.MessageField('DomainMapping', 1)
  name = _messages.StringField(2, required=True)


class RunProjectsLocationsDomainmappingsCreateRequest(_messages.Message):
  r"""A RunProjectsLocationsDomainmappingsCreateRequest object.

  Fields:
    domainMapping: A DomainMapping resource to be passed as the request body.
    parent: The project ID or project number in which this domain mapping
      should be created.
  """

  domainMapping = _messages.MessageField('DomainMapping', 1)
  parent = _messages.StringField(2, required=True)


class RunProjectsLocationsDomainmappingsDeleteRequest(_messages.Message):
  r"""A RunProjectsLocationsDomainmappingsDeleteRequest object.

  Fields:
    apiVersion: Cloud Run currently ignores this parameter.
    kind: Cloud Run currently ignores this parameter.
    name: The name of the domain mapping being deleted. If needed, replace
      {namespace_id} with the project ID.
    orphanDependents: Deprecated. Specifies the cascade behavior on delete.
      Cloud Run only supports cascading behavior, so this must be false. This
      attribute is deprecated, and is now replaced with PropagationPolicy See
      https://github.com/kubernetes/kubernetes/issues/46659 for more info.
    propagationPolicy: Specifies the propagation policy of delete. Cloud Run
      currently ignores this setting, and deletes in the background. Please
      see kubernetes.io/docs/concepts/workloads/controllers/garbage-
      collection/ for more information.
  """

  apiVersion = _messages.StringField(1)
  kind = _messages.StringField(2)
  name = _messages.StringField(3, required=True)
  orphanDependents = _messages.BooleanField(4)
  propagationPolicy = _messages.StringField(5)


class RunProjectsLocationsDomainmappingsGetRequest(_messages.Message):
  r"""A RunProjectsLocationsDomainmappingsGetRequest object.

  Fields:
    name: The name of the domain mapping being retrieved. If needed, replace
      {namespace_id} with the project ID.
  """

  name = _messages.StringField(1, required=True)


class RunProjectsLocationsDomainmappingsListRequest(_messages.Message):
  r"""A RunProjectsLocationsDomainmappingsListRequest object.

  Fields:
    continue_: Optional encoded string to continue paging.
    fieldSelector: Allows to filter resources based on a specific value for a
      field name. Send this in a query string format. i.e.
      'metadata.name%3Dlorem'. Not currently used by Cloud Run.
    includeUninitialized: Not currently used by Cloud Run.
    labelSelector: Allows to filter resources based on a label. Supported
      operations are =, !=, exists, in, and notIn.
    limit: The maximum number of records that should be returned.
    parent: The project ID or project number from which the domain mappings
      should be listed.
    resourceVersion: The baseline resource version from which the list or
      watch operation should start. Not currently used by Cloud Run.
    watch: Flag that indicates that the client expects to watch this resource
      as well. Not currently used by Cloud Run.
  """

  continue_ = _messages.StringField(1)
  fieldSelector = _messages.StringField(2)
  includeUninitialized = _messages.BooleanField(3)
  labelSelector = _messages.StringField(4)
  limit = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  parent = _messages.StringField(6, required=True)
  resourceVersion = _messages.StringField(7)
  watch = _messages.BooleanField(8)


class RunProjectsLocationsDomainmappingsReplaceDomainMappingRequest(_messages.Message):
  r"""A RunProjectsLocationsDomainmappingsReplaceDomainMappingRequest object.

  Fields:
    domainMapping: A DomainMapping resource to be passed as the request body.
    name: The name of the domain mapping being retrieved. If needed, replace
      {namespace_id} with the project ID.
  """

  domainMapping = _messages.MessageField('DomainMapping', 1)
  name = _messages.StringField(2, required=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    ListMeta, 'continue_', 'continue')
encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
