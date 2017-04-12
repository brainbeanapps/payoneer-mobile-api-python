# coding: utf-8

"""
    Payoneer Mobile API

    Swagger specification for https://mobileapi.payoneer.com

    OpenAPI spec version: 0.9.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrnRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, device_id=None, mac=None, language_code=None, mobile_app_id=None):
        """
        OrnRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'device_id': 'DeviceId',
            'mac': 'str',
            'language_code': 'LanguageCode',
            'mobile_app_id': 'MobileAppId'
        }

        self.attribute_map = {
            'device_id': 'DeviceId',
            'mac': 'MAC',
            'language_code': 'LanguageCode',
            'mobile_app_id': 'MobileAppId'
        }

        self._device_id = device_id
        self._mac = mac
        self._language_code = language_code
        self._mobile_app_id = mobile_app_id

    @property
    def device_id(self):
        """
        Gets the device_id of this OrnRequest.

        :return: The device_id of this OrnRequest.
        :rtype: DeviceId
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this OrnRequest.

        :param device_id: The device_id of this OrnRequest.
        :type: DeviceId
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")

        self._device_id = device_id

    @property
    def mac(self):
        """
        Gets the mac of this OrnRequest.

        :return: The mac of this OrnRequest.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """
        Sets the mac of this OrnRequest.

        :param mac: The mac of this OrnRequest.
        :type: str
        """

        self._mac = mac

    @property
    def language_code(self):
        """
        Gets the language_code of this OrnRequest.

        :return: The language_code of this OrnRequest.
        :rtype: LanguageCode
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this OrnRequest.

        :param language_code: The language_code of this OrnRequest.
        :type: LanguageCode
        """

        self._language_code = language_code

    @property
    def mobile_app_id(self):
        """
        Gets the mobile_app_id of this OrnRequest.

        :return: The mobile_app_id of this OrnRequest.
        :rtype: MobileAppId
        """
        return self._mobile_app_id

    @mobile_app_id.setter
    def mobile_app_id(self, mobile_app_id):
        """
        Sets the mobile_app_id of this OrnRequest.

        :param mobile_app_id: The mobile_app_id of this OrnRequest.
        :type: MobileAppId
        """
        if mobile_app_id is None:
            raise ValueError("Invalid value for `mobile_app_id`, must not be `None`")

        self._mobile_app_id = mobile_app_id

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
        if not isinstance(other, OrnRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
