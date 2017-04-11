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


class PaymentMethodDetailsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, device_id=None, mac=None, mobile_account_id=None, currency=None, latest_balance=None):
        """
        PaymentMethodDetailsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'device_id': 'DeviceId',
            'mac': 'str',
            'mobile_account_id': 'int',
            'currency': 'str',
            'latest_balance': 'bool'
        }

        self.attribute_map = {
            'device_id': 'DeviceId',
            'mac': 'MAC',
            'mobile_account_id': 'MobileAccountId',
            'currency': 'Currency',
            'latest_balance': 'LatestBalance'
        }

        self._device_id = device_id
        self._mac = mac
        self._mobile_account_id = mobile_account_id
        self._currency = currency
        self._latest_balance = latest_balance

    @property
    def device_id(self):
        """
        Gets the device_id of this PaymentMethodDetailsRequest.

        :return: The device_id of this PaymentMethodDetailsRequest.
        :rtype: DeviceId
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this PaymentMethodDetailsRequest.

        :param device_id: The device_id of this PaymentMethodDetailsRequest.
        :type: DeviceId
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")

        self._device_id = device_id

    @property
    def mac(self):
        """
        Gets the mac of this PaymentMethodDetailsRequest.

        :return: The mac of this PaymentMethodDetailsRequest.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """
        Sets the mac of this PaymentMethodDetailsRequest.

        :param mac: The mac of this PaymentMethodDetailsRequest.
        :type: str
        """

        self._mac = mac

    @property
    def mobile_account_id(self):
        """
        Gets the mobile_account_id of this PaymentMethodDetailsRequest.

        :return: The mobile_account_id of this PaymentMethodDetailsRequest.
        :rtype: int
        """
        return self._mobile_account_id

    @mobile_account_id.setter
    def mobile_account_id(self, mobile_account_id):
        """
        Sets the mobile_account_id of this PaymentMethodDetailsRequest.

        :param mobile_account_id: The mobile_account_id of this PaymentMethodDetailsRequest.
        :type: int
        """
        if mobile_account_id is None:
            raise ValueError("Invalid value for `mobile_account_id`, must not be `None`")

        self._mobile_account_id = mobile_account_id

    @property
    def currency(self):
        """
        Gets the currency of this PaymentMethodDetailsRequest.

        :return: The currency of this PaymentMethodDetailsRequest.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PaymentMethodDetailsRequest.

        :param currency: The currency of this PaymentMethodDetailsRequest.
        :type: str
        """

        self._currency = currency

    @property
    def latest_balance(self):
        """
        Gets the latest_balance of this PaymentMethodDetailsRequest.

        :return: The latest_balance of this PaymentMethodDetailsRequest.
        :rtype: bool
        """
        return self._latest_balance

    @latest_balance.setter
    def latest_balance(self, latest_balance):
        """
        Sets the latest_balance of this PaymentMethodDetailsRequest.

        :param latest_balance: The latest_balance of this PaymentMethodDetailsRequest.
        :type: bool
        """

        self._latest_balance = latest_balance

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
        if not isinstance(other, PaymentMethodDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other