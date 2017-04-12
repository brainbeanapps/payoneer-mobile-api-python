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


class BillingAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address1=None, address2=None, city=None, zip=None, state=None, country=None, phone=None):
        """
        BillingAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address1': 'str',
            'address2': 'str',
            'city': 'str',
            'zip': 'str',
            'state': 'str',
            'country': 'str',
            'phone': 'str'
        }

        self.attribute_map = {
            'address1': 'Address1',
            'address2': 'Address2',
            'city': 'City',
            'zip': 'Zip',
            'state': 'State',
            'country': 'Country',
            'phone': 'Phone'
        }

        self._address1 = address1
        self._address2 = address2
        self._city = city
        self._zip = zip
        self._state = state
        self._country = country
        self._phone = phone

    @property
    def address1(self):
        """
        Gets the address1 of this BillingAddress.

        :return: The address1 of this BillingAddress.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this BillingAddress.

        :param address1: The address1 of this BillingAddress.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this BillingAddress.

        :return: The address2 of this BillingAddress.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this BillingAddress.

        :param address2: The address2 of this BillingAddress.
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this BillingAddress.

        :return: The city of this BillingAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this BillingAddress.

        :param city: The city of this BillingAddress.
        :type: str
        """

        self._city = city

    @property
    def zip(self):
        """
        Gets the zip of this BillingAddress.

        :return: The zip of this BillingAddress.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this BillingAddress.

        :param zip: The zip of this BillingAddress.
        :type: str
        """

        self._zip = zip

    @property
    def state(self):
        """
        Gets the state of this BillingAddress.

        :return: The state of this BillingAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this BillingAddress.

        :param state: The state of this BillingAddress.
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this BillingAddress.

        :return: The country of this BillingAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillingAddress.

        :param country: The country of this BillingAddress.
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """
        Gets the phone of this BillingAddress.

        :return: The phone of this BillingAddress.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this BillingAddress.

        :param phone: The phone of this BillingAddress.
        :type: str
        """

        self._phone = phone

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
        if not isinstance(other, BillingAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
