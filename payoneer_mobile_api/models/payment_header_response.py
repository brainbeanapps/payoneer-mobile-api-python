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


class PaymentHeaderResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, payment_id=None, date=None, loader=None, amount=None, payment_status_category=None):
        """
        PaymentHeaderResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'payment_id': 'str',
            'date': 'str',
            'loader': 'str',
            'amount': 'str',
            'payment_status_category': 'int'
        }

        self.attribute_map = {
            'payment_id': 'PaymentId',
            'date': 'Date',
            'loader': 'Loader',
            'amount': 'Amount',
            'payment_status_category': 'PaymentStatusCategory'
        }

        self._payment_id = payment_id
        self._date = date
        self._loader = loader
        self._amount = amount
        self._payment_status_category = payment_status_category

    @property
    def payment_id(self):
        """
        Gets the payment_id of this PaymentHeaderResponse.

        :return: The payment_id of this PaymentHeaderResponse.
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """
        Sets the payment_id of this PaymentHeaderResponse.

        :param payment_id: The payment_id of this PaymentHeaderResponse.
        :type: str
        """

        self._payment_id = payment_id

    @property
    def date(self):
        """
        Gets the date of this PaymentHeaderResponse.

        :return: The date of this PaymentHeaderResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this PaymentHeaderResponse.

        :param date: The date of this PaymentHeaderResponse.
        :type: str
        """

        self._date = date

    @property
    def loader(self):
        """
        Gets the loader of this PaymentHeaderResponse.

        :return: The loader of this PaymentHeaderResponse.
        :rtype: str
        """
        return self._loader

    @loader.setter
    def loader(self, loader):
        """
        Sets the loader of this PaymentHeaderResponse.

        :param loader: The loader of this PaymentHeaderResponse.
        :type: str
        """

        self._loader = loader

    @property
    def amount(self):
        """
        Gets the amount of this PaymentHeaderResponse.

        :return: The amount of this PaymentHeaderResponse.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PaymentHeaderResponse.

        :param amount: The amount of this PaymentHeaderResponse.
        :type: str
        """

        self._amount = amount

    @property
    def payment_status_category(self):
        """
        Gets the payment_status_category of this PaymentHeaderResponse.

        :return: The payment_status_category of this PaymentHeaderResponse.
        :rtype: int
        """
        return self._payment_status_category

    @payment_status_category.setter
    def payment_status_category(self, payment_status_category):
        """
        Sets the payment_status_category of this PaymentHeaderResponse.

        :param payment_status_category: The payment_status_category of this PaymentHeaderResponse.
        :type: int
        """

        self._payment_status_category = payment_status_category

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
        if not isinstance(other, PaymentHeaderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
