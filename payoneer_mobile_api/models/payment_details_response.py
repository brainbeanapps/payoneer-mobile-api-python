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


class PaymentDetailsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, response_code=None, details=None):
        """
        PaymentDetailsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'response_code': 'int',
            'details': 'PaymentDetails'
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
        Gets the response_code of this PaymentDetailsResponse.
        1 - Success; 34 - (Assumption) Terms&Conditions not agreed;

        :return: The response_code of this PaymentDetailsResponse.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PaymentDetailsResponse.
        1 - Success; 34 - (Assumption) Terms&Conditions not agreed;

        :param response_code: The response_code of this PaymentDetailsResponse.
        :type: int
        """

        self._response_code = response_code

    @property
    def details(self):
        """
        Gets the details of this PaymentDetailsResponse.

        :return: The details of this PaymentDetailsResponse.
        :rtype: PaymentDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this PaymentDetailsResponse.

        :param details: The details of this PaymentDetailsResponse.
        :type: PaymentDetails
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
        if not isinstance(other, PaymentDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
