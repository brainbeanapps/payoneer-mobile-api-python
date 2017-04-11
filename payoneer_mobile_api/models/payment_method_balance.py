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


class PaymentMethodBalance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, quote_response_code=None, quote_response_description=None, currency=None, card_balance=None, account_balance=None, last_processed=None):
        """
        PaymentMethodBalance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'quote_response_code': 'int',
            'quote_response_description': 'str',
            'currency': 'str',
            'card_balance': 'str',
            'account_balance': 'str',
            'last_processed': 'str'
        }

        self.attribute_map = {
            'quote_response_code': 'QuoteResponseCode',
            'quote_response_description': 'QuoteResponseDescription',
            'currency': 'Currency',
            'card_balance': 'CardBalance',
            'account_balance': 'AccountBalance',
            'last_processed': 'LastProcessed'
        }

        self._quote_response_code = quote_response_code
        self._quote_response_description = quote_response_description
        self._currency = currency
        self._card_balance = card_balance
        self._account_balance = account_balance
        self._last_processed = last_processed

    @property
    def quote_response_code(self):
        """
        Gets the quote_response_code of this PaymentMethodBalance.

        :return: The quote_response_code of this PaymentMethodBalance.
        :rtype: int
        """
        return self._quote_response_code

    @quote_response_code.setter
    def quote_response_code(self, quote_response_code):
        """
        Sets the quote_response_code of this PaymentMethodBalance.

        :param quote_response_code: The quote_response_code of this PaymentMethodBalance.
        :type: int
        """

        self._quote_response_code = quote_response_code

    @property
    def quote_response_description(self):
        """
        Gets the quote_response_description of this PaymentMethodBalance.

        :return: The quote_response_description of this PaymentMethodBalance.
        :rtype: str
        """
        return self._quote_response_description

    @quote_response_description.setter
    def quote_response_description(self, quote_response_description):
        """
        Sets the quote_response_description of this PaymentMethodBalance.

        :param quote_response_description: The quote_response_description of this PaymentMethodBalance.
        :type: str
        """

        self._quote_response_description = quote_response_description

    @property
    def currency(self):
        """
        Gets the currency of this PaymentMethodBalance.

        :return: The currency of this PaymentMethodBalance.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PaymentMethodBalance.

        :param currency: The currency of this PaymentMethodBalance.
        :type: str
        """

        self._currency = currency

    @property
    def card_balance(self):
        """
        Gets the card_balance of this PaymentMethodBalance.

        :return: The card_balance of this PaymentMethodBalance.
        :rtype: str
        """
        return self._card_balance

    @card_balance.setter
    def card_balance(self, card_balance):
        """
        Sets the card_balance of this PaymentMethodBalance.

        :param card_balance: The card_balance of this PaymentMethodBalance.
        :type: str
        """

        self._card_balance = card_balance

    @property
    def account_balance(self):
        """
        Gets the account_balance of this PaymentMethodBalance.

        :return: The account_balance of this PaymentMethodBalance.
        :rtype: str
        """
        return self._account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        """
        Sets the account_balance of this PaymentMethodBalance.

        :param account_balance: The account_balance of this PaymentMethodBalance.
        :type: str
        """

        self._account_balance = account_balance

    @property
    def last_processed(self):
        """
        Gets the last_processed of this PaymentMethodBalance.

        :return: The last_processed of this PaymentMethodBalance.
        :rtype: str
        """
        return self._last_processed

    @last_processed.setter
    def last_processed(self, last_processed):
        """
        Sets the last_processed of this PaymentMethodBalance.

        :param last_processed: The last_processed of this PaymentMethodBalance.
        :type: str
        """

        self._last_processed = last_processed

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
        if not isinstance(other, PaymentMethodBalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other