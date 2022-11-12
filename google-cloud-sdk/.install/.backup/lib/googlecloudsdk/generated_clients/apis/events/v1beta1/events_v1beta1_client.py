"""Generated client library for events version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.events.v1beta1 import events_v1beta1_messages as messages


class EventsV1beta1(base_api.BaseApiClient):
  """Generated client library for service events version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://events.googleapis.com/'
  MTLS_BASE_URL = 'https://events.mtls.googleapis.com/'

  _PACKAGE = 'events'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'EventsV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new events handle."""
    url = url or self.BASE_URL
    super(EventsV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.customresourcedefinitions = self.CustomresourcedefinitionsService(self)
    self.namespaces_customresourcedefinitions = self.NamespacesCustomresourcedefinitionsService(self)
    self.namespaces_triggers = self.NamespacesTriggersService(self)
    self.namespaces = self.NamespacesService(self)
    self.projects_locations_customresourcedefinitions = self.ProjectsLocationsCustomresourcedefinitionsService(self)
    self.projects_locations_triggers = self.ProjectsLocationsTriggersService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class CustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the customresourcedefinitions resource."""

    _NAME = 'customresourcedefinitions'

    def __init__(self, client):
      super(EventsV1beta1.CustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Rpc to list custom resource definitions.

      Args:
        request: (EventsCustomresourcedefinitionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCustomResourceDefinitionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='events.customresourcedefinitions.list',
        ordered_params=[],
        path_params=[],
        query_params=['continue_', 'fieldSelector', 'includeUninitialized', 'labelSelector', 'limit', 'parent', 'resourceVersion', 'watch'],
        relative_path='apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions',
        request_field='',
        request_type_name='EventsCustomresourcedefinitionsListRequest',
        response_type_name='ListCustomResourceDefinitionsResponse',
        supports_download=False,
    )

  class NamespacesCustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the namespaces_customresourcedefinitions resource."""

    _NAME = 'namespaces_customresourcedefinitions'

    def __init__(self, client):
      super(EventsV1beta1.NamespacesCustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a CustomResourceDefinition.

      Args:
        request: (EventsNamespacesCustomresourcedefinitionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomResourceDefinition) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/apiextensions.k8s.io/v1beta1/namespaces/{namespacesId}/customresourcedefinitions/{customresourcedefinitionsId}',
        http_method='GET',
        method_id='events.namespaces.customresourcedefinitions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/apiextensions.k8s.io/v1beta1/{+name}',
        request_field='',
        request_type_name='EventsNamespacesCustomresourcedefinitionsGetRequest',
        response_type_name='CustomResourceDefinition',
        supports_download=False,
    )

  class NamespacesTriggersService(base_api.BaseApiService):
    """Service class for the namespaces_triggers resource."""

    _NAME = 'namespaces_triggers'

    def __init__(self, client):
      super(EventsV1beta1.NamespacesTriggersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new trigger.

      Args:
        request: (EventsNamespacesTriggersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers',
        http_method='POST',
        method_id='events.namespaces.triggers.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='apis/eventing.knative.dev/v1beta1/{+parent}/triggers',
        request_field='trigger',
        request_type_name='EventsNamespacesTriggersCreateRequest',
        response_type_name='Trigger',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Rpc to delete a trigger.

      Args:
        request: (EventsNamespacesTriggersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers/{triggersId}',
        http_method='DELETE',
        method_id='events.namespaces.triggers.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['apiVersion', 'kind', 'propagationPolicy'],
        relative_path='apis/eventing.knative.dev/v1beta1/{+name}',
        request_field='',
        request_type_name='EventsNamespacesTriggersDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a trigger.

      Args:
        request: (EventsNamespacesTriggersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers/{triggersId}',
        http_method='GET',
        method_id='events.namespaces.triggers.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/eventing.knative.dev/v1beta1/{+name}',
        request_field='',
        request_type_name='EventsNamespacesTriggersGetRequest',
        response_type_name='Trigger',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list triggers.

      Args:
        request: (EventsNamespacesTriggersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTriggersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers',
        http_method='GET',
        method_id='events.namespaces.triggers.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['continue_', 'fieldSelector', 'includeUninitialized', 'labelSelector', 'limit', 'resourceVersion', 'watch'],
        relative_path='apis/eventing.knative.dev/v1beta1/{+parent}/triggers',
        request_field='',
        request_type_name='EventsNamespacesTriggersListRequest',
        response_type_name='ListTriggersResponse',
        supports_download=False,
    )

    def ReplaceTrigger(self, request, global_params=None):
      r"""Rpc to replace a trigger. Only the spec and metadata labels and annotations are modifiable. After the Update request, Events for Cloud Run will work to make the 'status' match the requested 'spec'. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.

      Args:
        request: (EventsNamespacesTriggersReplaceTriggerRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('ReplaceTrigger')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceTrigger.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers/{triggersId}',
        http_method='PUT',
        method_id='events.namespaces.triggers.replaceTrigger',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/eventing.knative.dev/v1beta1/{+name}',
        request_field='trigger',
        request_type_name='EventsNamespacesTriggersReplaceTriggerRequest',
        response_type_name='Trigger',
        supports_download=False,
    )

  class NamespacesService(base_api.BaseApiService):
    """Service class for the namespaces resource."""

    _NAME = 'namespaces'

    def __init__(self, client):
      super(EventsV1beta1.NamespacesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsCustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the projects_locations_customresourcedefinitions resource."""

    _NAME = 'projects_locations_customresourcedefinitions'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsLocationsCustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a CustomResourceDefinition.

      Args:
        request: (EventsProjectsLocationsCustomresourcedefinitionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomResourceDefinition) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/customresourcedefinitions/{customresourcedefinitionsId}',
        http_method='GET',
        method_id='events.projects.locations.customresourcedefinitions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='EventsProjectsLocationsCustomresourcedefinitionsGetRequest',
        response_type_name='CustomResourceDefinition',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list custom resource definitions.

      Args:
        request: (EventsProjectsLocationsCustomresourcedefinitionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCustomResourceDefinitionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/customresourcedefinitions',
        http_method='GET',
        method_id='events.projects.locations.customresourcedefinitions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['continue_', 'fieldSelector', 'includeUninitialized', 'labelSelector', 'limit', 'resourceVersion', 'watch'],
        relative_path='v1beta1/{+parent}/customresourcedefinitions',
        request_field='',
        request_type_name='EventsProjectsLocationsCustomresourcedefinitionsListRequest',
        response_type_name='ListCustomResourceDefinitionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsTriggersService(base_api.BaseApiService):
    """Service class for the projects_locations_triggers resource."""

    _NAME = 'projects_locations_triggers'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsLocationsTriggersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new trigger.

      Args:
        request: (EventsProjectsLocationsTriggersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/triggers',
        http_method='POST',
        method_id='events.projects.locations.triggers.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta1/{+parent}/triggers',
        request_field='trigger',
        request_type_name='EventsProjectsLocationsTriggersCreateRequest',
        response_type_name='Trigger',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Rpc to delete a trigger.

      Args:
        request: (EventsProjectsLocationsTriggersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method='DELETE',
        method_id='events.projects.locations.triggers.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['apiVersion', 'kind', 'propagationPolicy'],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='EventsProjectsLocationsTriggersDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a trigger.

      Args:
        request: (EventsProjectsLocationsTriggersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method='GET',
        method_id='events.projects.locations.triggers.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='EventsProjectsLocationsTriggersGetRequest',
        response_type_name='Trigger',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list triggers.

      Args:
        request: (EventsProjectsLocationsTriggersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTriggersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/triggers',
        http_method='GET',
        method_id='events.projects.locations.triggers.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['continue_', 'fieldSelector', 'includeUninitialized', 'labelSelector', 'limit', 'resourceVersion', 'watch'],
        relative_path='v1beta1/{+parent}/triggers',
        request_field='',
        request_type_name='EventsProjectsLocationsTriggersListRequest',
        response_type_name='ListTriggersResponse',
        supports_download=False,
    )

    def ReplaceTrigger(self, request, global_params=None):
      r"""Rpc to replace a trigger. Only the spec and metadata labels and annotations are modifiable. After the Update request, Events for Cloud Run will work to make the 'status' match the requested 'spec'. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.

      Args:
        request: (EventsProjectsLocationsTriggersReplaceTriggerRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('ReplaceTrigger')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceTrigger.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method='PUT',
        method_id='events.projects.locations.triggers.replaceTrigger',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='trigger',
        request_type_name='EventsProjectsLocationsTriggersReplaceTriggerRequest',
        response_type_name='Trigger',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
