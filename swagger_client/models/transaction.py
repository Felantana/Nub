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

class Transaction(object):
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
        'audit_id': 'int',
        'request_id': 'RequestIdSchema',
        'api_transaction_id': 'str',
        'http_method': 'str',
        'modified_by': 'ModifiedBySchema',
        'modified_dtm': 'ModifiedDtmSchema',
        'changes': 'TransactionChanges',
        'http_status_code': 'int',
        'failure_details': 'ErrorResponse'
    }

    attribute_map = {
        'audit_id': 'auditId',
        'request_id': 'requestId',
        'api_transaction_id': 'apiTransactionId',
        'http_method': 'httpMethod',
        'modified_by': 'modifiedBy',
        'modified_dtm': 'modifiedDtm',
        'changes': 'changes',
        'http_status_code': 'httpStatusCode',
        'failure_details': 'failureDetails'
    }

    def __init__(self, audit_id=None, request_id=None, api_transaction_id=None, http_method=None, modified_by=None, modified_dtm=None, changes=None, http_status_code=None, failure_details=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501
        self._audit_id = None
        self._request_id = None
        self._api_transaction_id = None
        self._http_method = None
        self._modified_by = None
        self._modified_dtm = None
        self._changes = None
        self._http_status_code = None
        self._failure_details = None
        self.discriminator = None
        if audit_id is not None:
            self.audit_id = audit_id
        if request_id is not None:
            self.request_id = request_id
        if api_transaction_id is not None:
            self.api_transaction_id = api_transaction_id
        if http_method is not None:
            self.http_method = http_method
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_dtm is not None:
            self.modified_dtm = modified_dtm
        if changes is not None:
            self.changes = changes
        if http_status_code is not None:
            self.http_status_code = http_status_code
        if failure_details is not None:
            self.failure_details = failure_details

    @property
    def audit_id(self):
        """Gets the audit_id of this Transaction.  # noqa: E501


        :return: The audit_id of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._audit_id

    @audit_id.setter
    def audit_id(self, audit_id):
        """Sets the audit_id of this Transaction.


        :param audit_id: The audit_id of this Transaction.  # noqa: E501
        :type: int
        """

        self._audit_id = audit_id

    @property
    def request_id(self):
        """Gets the request_id of this Transaction.  # noqa: E501


        :return: The request_id of this Transaction.  # noqa: E501
        :rtype: RequestIdSchema
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Transaction.


        :param request_id: The request_id of this Transaction.  # noqa: E501
        :type: RequestIdSchema
        """

        self._request_id = request_id

    @property
    def api_transaction_id(self):
        """Gets the api_transaction_id of this Transaction.  # noqa: E501


        :return: The api_transaction_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._api_transaction_id

    @api_transaction_id.setter
    def api_transaction_id(self, api_transaction_id):
        """Sets the api_transaction_id of this Transaction.


        :param api_transaction_id: The api_transaction_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._api_transaction_id = api_transaction_id

    @property
    def http_method(self):
        """Gets the http_method of this Transaction.  # noqa: E501


        :return: The http_method of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this Transaction.


        :param http_method: The http_method of this Transaction.  # noqa: E501
        :type: str
        """

        self._http_method = http_method

    @property
    def modified_by(self):
        """Gets the modified_by of this Transaction.  # noqa: E501


        :return: The modified_by of this Transaction.  # noqa: E501
        :rtype: ModifiedBySchema
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Transaction.


        :param modified_by: The modified_by of this Transaction.  # noqa: E501
        :type: ModifiedBySchema
        """

        self._modified_by = modified_by

    @property
    def modified_dtm(self):
        """Gets the modified_dtm of this Transaction.  # noqa: E501


        :return: The modified_dtm of this Transaction.  # noqa: E501
        :rtype: ModifiedDtmSchema
        """
        return self._modified_dtm

    @modified_dtm.setter
    def modified_dtm(self, modified_dtm):
        """Sets the modified_dtm of this Transaction.


        :param modified_dtm: The modified_dtm of this Transaction.  # noqa: E501
        :type: ModifiedDtmSchema
        """

        self._modified_dtm = modified_dtm

    @property
    def changes(self):
        """Gets the changes of this Transaction.  # noqa: E501


        :return: The changes of this Transaction.  # noqa: E501
        :rtype: TransactionChanges
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this Transaction.


        :param changes: The changes of this Transaction.  # noqa: E501
        :type: TransactionChanges
        """

        self._changes = changes

    @property
    def http_status_code(self):
        """Gets the http_status_code of this Transaction.  # noqa: E501


        :return: The http_status_code of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this Transaction.


        :param http_status_code: The http_status_code of this Transaction.  # noqa: E501
        :type: int
        """

        self._http_status_code = http_status_code

    @property
    def failure_details(self):
        """Gets the failure_details of this Transaction.  # noqa: E501


        :return: The failure_details of this Transaction.  # noqa: E501
        :rtype: ErrorResponse
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details):
        """Sets the failure_details of this Transaction.


        :param failure_details: The failure_details of this Transaction.  # noqa: E501
        :type: ErrorResponse
        """

        self._failure_details = failure_details

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
        if issubclass(Transaction, dict):
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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
