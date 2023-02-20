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

class ViewFilters(object):
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
        'a_z_a_z0_9': 'ViewFiltersAzAZ09'
    }

    attribute_map = {
        'a_z_a_z0_9': '^[a-zA-Z0-9]+$'
    }

    def __init__(self, a_z_a_z0_9=None):  # noqa: E501
        """ViewFilters - a model defined in Swagger"""  # noqa: E501
        self._a_z_a_z0_9 = None
        self.discriminator = None
        if a_z_a_z0_9 is not None:
            self.a_z_a_z0_9 = a_z_a_z0_9

    @property
    def a_z_a_z0_9(self):
        """Gets the a_z_a_z0_9 of this ViewFilters.  # noqa: E501


        :return: The a_z_a_z0_9 of this ViewFilters.  # noqa: E501
        :rtype: ViewFiltersAzAZ09
        """
        return self._a_z_a_z0_9

    @a_z_a_z0_9.setter
    def a_z_a_z0_9(self, a_z_a_z0_9):
        """Sets the a_z_a_z0_9 of this ViewFilters.


        :param a_z_a_z0_9: The a_z_a_z0_9 of this ViewFilters.  # noqa: E501
        :type: ViewFiltersAzAZ09
        """

        self._a_z_a_z0_9 = a_z_a_z0_9

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
        if issubclass(ViewFilters, dict):
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
        if not isinstance(other, ViewFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
