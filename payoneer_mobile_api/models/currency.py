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


class Currency(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, display=None, location=None):
        """
        Currency - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'display': 'str',
            'location': 'int'
        }

        self.attribute_map = {
            'code': 'Code',
            'display': 'Display',
            'location': 'Location'
        }

        self._code = code
        self._display = display
        self._location = location

    @property
    def code(self):
        """
        Gets the code of this Currency.

        :return: The code of this Currency.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Currency.

        :param code: The code of this Currency.
        :type: str
        """

        self._code = code

    @property
    def display(self):
        """
        Gets the display of this Currency.

        :return: The display of this Currency.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this Currency.

        :param display: The display of this Currency.
        :type: str
        """

        self._display = display

    @property
    def location(self):
        """
        Gets the location of this Currency.

        :return: The location of this Currency.
        :rtype: int
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Currency.

        :param location: The location of this Currency.
        :type: int
        """

        self._location = location

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
        if not isinstance(other, Currency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other