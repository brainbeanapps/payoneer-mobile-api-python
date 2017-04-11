# coding: utf-8

"""
    Payoneer Mobile API

    Swagger specification for https://mobileapi.payoneer.com

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TransactionDetailsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, response_code=None, details=None):
        """
        TransactionDetailsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'response_code': 'int',
            'details': 'TransactionDetails'
        }

        self.attribute_map = {
            'response_code': 'ResponseCode',
            'details': 'Details'
        }

        self._response_code = response_code
        self._details = details

    @property
    def response_code(self):
        """
        Gets the response_code of this TransactionDetailsResponse.

        :return: The response_code of this TransactionDetailsResponse.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this TransactionDetailsResponse.

        :param response_code: The response_code of this TransactionDetailsResponse.
        :type: int
        """

        self._response_code = response_code

    @property
    def details(self):
        """
        Gets the details of this TransactionDetailsResponse.

        :return: The details of this TransactionDetailsResponse.
        :rtype: TransactionDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this TransactionDetailsResponse.

        :param details: The details of this TransactionDetailsResponse.
        :type: TransactionDetails
        """

        self._details = details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TransactionDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other