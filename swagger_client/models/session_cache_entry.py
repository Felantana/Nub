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

class SessionCacheEntry(object):
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
        'cache_hits': 'int',
        'email': 'str',
        'expiration_epoc': 'int',
        'role': 'str',
        'username': 'str'
    }

    attribute_map = {
        'cache_hits': 'cache_hits',
        'email': 'email',
        'expiration_epoc': 'expiration_epoc',
        'role': 'role',
        'username': 'username'
    }

    def __init__(self, cache_hits=None, email=None, expiration_epoc=None, role=None, username=None):  # noqa: E501
        """SessionCacheEntry - a model defined in Swagger"""  # noqa: E501
        self._cache_hits = None
        self._email = None
        self._expiration_epoc = None
        self._role = None
        self._username = None
        self.discriminator = None
        self.cache_hits = cache_hits
        self.email = email
        self.expiration_epoc = expiration_epoc
        self.role = role
        self.username = username

    @property
    def cache_hits(self):
        """Gets the cache_hits of this SessionCacheEntry.  # noqa: E501


        :return: The cache_hits of this SessionCacheEntry.  # noqa: E501
        :rtype: int
        """
        return self._cache_hits

    @cache_hits.setter
    def cache_hits(self, cache_hits):
        """Sets the cache_hits of this SessionCacheEntry.


        :param cache_hits: The cache_hits of this SessionCacheEntry.  # noqa: E501
        :type: int
        """
        if cache_hits is None:
            raise ValueError("Invalid value for `cache_hits`, must not be `None`")  # noqa: E501

        self._cache_hits = cache_hits

    @property
    def email(self):
        """Gets the email of this SessionCacheEntry.  # noqa: E501


        :return: The email of this SessionCacheEntry.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SessionCacheEntry.


        :param email: The email of this SessionCacheEntry.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def expiration_epoc(self):
        """Gets the expiration_epoc of this SessionCacheEntry.  # noqa: E501


        :return: The expiration_epoc of this SessionCacheEntry.  # noqa: E501
        :rtype: int
        """
        return self._expiration_epoc

    @expiration_epoc.setter
    def expiration_epoc(self, expiration_epoc):
        """Sets the expiration_epoc of this SessionCacheEntry.


        :param expiration_epoc: The expiration_epoc of this SessionCacheEntry.  # noqa: E501
        :type: int
        """
        if expiration_epoc is None:
            raise ValueError("Invalid value for `expiration_epoc`, must not be `None`")  # noqa: E501

        self._expiration_epoc = expiration_epoc

    @property
    def role(self):
        """Gets the role of this SessionCacheEntry.  # noqa: E501


        :return: The role of this SessionCacheEntry.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SessionCacheEntry.


        :param role: The role of this SessionCacheEntry.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def username(self):
        """Gets the username of this SessionCacheEntry.  # noqa: E501


        :return: The username of this SessionCacheEntry.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SessionCacheEntry.


        :param username: The username of this SessionCacheEntry.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(SessionCacheEntry, dict):
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
        if not isinstance(other, SessionCacheEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
