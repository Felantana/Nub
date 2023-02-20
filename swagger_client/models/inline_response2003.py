# coding: utf-8

"""
    Compass - Request Tracker

    API documentation for Compass - Request Tracker. This document contains a complete list of fields for a Compass request accessible to an admin. An authorized user may only read, write, and update certain fields or delete based on their role. All requests require a valid OAuth2 Bearer Token passed as a header that is associated with a Cisco CEC user account.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: compass-devcx@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2003(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[SessionCacheEntry]',
        'metadata': 'SessionsMetadata'
    }

    attribute_map = {
        'items': 'items',
        'metadata': '_metadata'
    }

    def __init__(self, items=None, metadata=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self._metadata = None
        self.discriminator = None
        if items is not None:
            self.items = items
        if metadata is not None:
            self.metadata = metadata

    @property
    def items(self):
        """Gets the items of this InlineResponse2003.  # noqa: E501


        :return: The items of this InlineResponse2003.  # noqa: E501
        :rtype: list[SessionCacheEntry]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InlineResponse2003.


        :param items: The items of this InlineResponse2003.  # noqa: E501
        :type: list[SessionCacheEntry]
        """

        self._items = items

    @property
    def metadata(self):
        """Gets the metadata of this InlineResponse2003.  # noqa: E501


        :return: The metadata of this InlineResponse2003.  # noqa: E501
        :rtype: SessionsMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InlineResponse2003.


        :param metadata: The metadata of this InlineResponse2003.  # noqa: E501
        :type: SessionsMetadata
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2003, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other