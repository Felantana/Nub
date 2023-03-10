# coding: utf-8

"""
    Compass - Request Tracker

    API documentation for Compass - Request Tracker. This document contains a complete list of fields for a Compass request accessible to an admin. An authorized user may only read, write, and update certain fields or delete based on their role. All requests require a valid OAuth2 Bearer Token passed as a header that is associated with a Cisco CEC user account.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: compass-devcx@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ColumnConfigsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_column_config(self, column_config_id, **kwargs):  # noqa: E501
        """Delete a Column Config  # noqa: E501

        Delete a specified Column Config.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_column_config(column_config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str column_config_id: Unique identifier of a UI column config. (required)
        :param str table_prefix: (development only) An optional identifier used to prefix snowflake tables.. These tables must be defined in the corresponding environment prior to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_column_config_with_http_info(column_config_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_column_config_with_http_info(column_config_id, **kwargs)  # noqa: E501
            return data

    def delete_column_config_with_http_info(self, column_config_id, **kwargs):  # noqa: E501
        """Delete a Column Config  # noqa: E501

        Delete a specified Column Config.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_column_config_with_http_info(column_config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str column_config_id: Unique identifier of a UI column config. (required)
        :param str table_prefix: (development only) An optional identifier used to prefix snowflake tables.. These tables must be defined in the corresponding environment prior to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['column_config_id', 'table_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_column_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'column_config_id' is set
        if ('column_config_id' not in params or
                params['column_config_id'] is None):
            raise ValueError("Missing the required parameter `column_config_id` when calling `delete_column_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'column_config_id' in params:
            path_params['columnConfigId'] = params['column_config_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'table_prefix' in params:
            header_params['Table-Prefix'] = params['table_prefix']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuthorization']  # noqa: E501

        return self.api_client.call_api(
            '/columnConfigs/{columnConfigId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_column_configs(self, **kwargs):  # noqa: E501
        """Get all column configs  # noqa: E501

        Get information of all column configs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_column_configs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Fields to return as part of the response for a column config object, where multiple fields are separated by a comma.
        :param str sort: Field to sort results by, used in conjunction with `order`.
        :param str order: Order by ascending or descending, used in conjunction with `sort`.
        :param str table_prefix: (development only) An optional identifier used to prefix snowflake tables.. These tables must be defined in the corresponding environment prior to use.
        :return: ColumnConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_column_configs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_column_configs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_column_configs_with_http_info(self, **kwargs):  # noqa: E501
        """Get all column configs  # noqa: E501

        Get information of all column configs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_column_configs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Fields to return as part of the response for a column config object, where multiple fields are separated by a comma.
        :param str sort: Field to sort results by, used in conjunction with `order`.
        :param str order: Order by ascending or descending, used in conjunction with `sort`.
        :param str table_prefix: (development only) An optional identifier used to prefix snowflake tables.. These tables must be defined in the corresponding environment prior to use.
        :return: ColumnConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'sort', 'order', 'table_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_column_configs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}
        if 'table_prefix' in params:
            header_params['Table-Prefix'] = params['table_prefix']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuthorization']  # noqa: E501

        return self.api_client.call_api(
            '/columnConfigs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ColumnConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_column_config(self, body, column_config_id, **kwargs):  # noqa: E501
        """Update your Column Config  # noqa: E501

        Patch information about column config.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_column_config(body, column_config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: A JSON object containing patch column config information. (required)
        :param str column_config_id: Unique identifier of a UI column config. (required)
        :param str table_prefix: (development only) An optional identifier used to prefix snowflake tables.. These tables must be defined in the corresponding environment prior to use.
        :return: ColumnConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_column_config_with_http_info(body, column_config_id, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_column_config_with_http_info(body, column_config_id, **kwargs)  # noqa: E501
            return data

    def patch_column_config_with_http_info(self, body, column_config_id, **kwargs):  # noqa: E501
        """Update your Column Config  # noqa: E501

        Patch information about column config.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_column_config_with_http_info(body, column_config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: A JSON object containing patch column config information. (required)
        :param str column_config_id: Unique identifier of a UI column config. (required)
        :param str table_prefix: (development only) An optional identifier used to prefix snowflake tables.. These tables must be defined in the corresponding environment prior to use.
        :return: ColumnConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'column_config_id', 'table_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_column_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_column_config`")  # noqa: E501
        # verify the required parameter 'column_config_id' is set
        if ('column_config_id' not in params or
                params['column_config_id'] is None):
            raise ValueError("Missing the required parameter `column_config_id` when calling `patch_column_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'column_config_id' in params:
            path_params['columnConfigId'] = params['column_config_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'table_prefix' in params:
            header_params['Table-Prefix'] = params['table_prefix']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuthorization']  # noqa: E501

        return self.api_client.call_api(
            '/columnConfigs/{columnConfigId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ColumnConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
