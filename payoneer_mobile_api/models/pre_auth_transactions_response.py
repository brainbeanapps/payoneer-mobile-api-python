# coding: utf-8

"""
    Payoneer Mobile API

    Swagger specification for https://mobileapi.payoneer.com

    OpenAPI spec version: 0.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PreAuthTransactionsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, response_code=None, pre_auth_transaction_headers_list=None):
        """
        PreAuthTransactionsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'response_code': 'int',
            'pre_auth_transaction_headers_list': 'list[TransactionHeaderResponse]'
        }

        self.attribute_map = {
            'response_code': 'ResponseCode',
            'pre_auth_transaction_headers_list': 'PreAuthTransactionHeadersList'
        }

        self._response_code = response_code
        self._pre_auth_transaction_headers_list = pre_auth_transaction_headers_list

    @property
    def response_code(self):
        """
        Gets the response_code of this PreAuthTransactionsResponse.
        1 - Success; 34 - (Assumption) Terms&Conditions not agreed;

        :return: The response_code of this PreAuthTransactionsResponse.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PreAuthTransactionsResponse.
        1 - Success; 34 - (Assumption) Terms&Conditions not agreed;

        :param response_code: The response_code of this PreAuthTransactionsResponse.
        :type: int
        """

        self._response_code = response_code

    @property
    def pre_auth_transaction_headers_list(self):
        """
        Gets the pre_auth_transaction_headers_list of this PreAuthTransactionsResponse.

        :return: The pre_auth_transaction_headers_list of this PreAuthTransactionsResponse.
        :rtype: list[TransactionHeaderResponse]
        """
        return self._pre_auth_transaction_headers_list

    @pre_auth_transaction_headers_list.setter
    def pre_auth_transaction_headers_list(self, pre_auth_transaction_headers_list):
        """
        Sets the pre_auth_transaction_headers_list of this PreAuthTransactionsResponse.

        :param pre_auth_transaction_headers_list: The pre_auth_transaction_headers_list of this PreAuthTransactionsResponse.
        :type: list[TransactionHeaderResponse]
        """

        self._pre_auth_transaction_headers_list = pre_auth_transaction_headers_list

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
        if not isinstance(other, PreAuthTransactionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
