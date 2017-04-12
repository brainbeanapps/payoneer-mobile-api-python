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


class SmsChallengeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, device_id=None, mac=None, phone_number_id=None):
        """
        SmsChallengeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'device_id': 'DeviceId',
            'mac': 'str',
            'phone_number_id': 'int'
        }

        self.attribute_map = {
            'device_id': 'DeviceId',
            'mac': 'MAC',
            'phone_number_id': 'PhoneNumberId'
        }

        self._device_id = device_id
        self._mac = mac
        self._phone_number_id = phone_number_id

    @property
    def device_id(self):
        """
        Gets the device_id of this SmsChallengeRequest.

        :return: The device_id of this SmsChallengeRequest.
        :rtype: DeviceId
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this SmsChallengeRequest.

        :param device_id: The device_id of this SmsChallengeRequest.
        :type: DeviceId
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")

        self._device_id = device_id

    @property
    def mac(self):
        """
        Gets the mac of this SmsChallengeRequest.

        :return: The mac of this SmsChallengeRequest.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """
        Sets the mac of this SmsChallengeRequest.

        :param mac: The mac of this SmsChallengeRequest.
        :type: str
        """

        self._mac = mac

    @property
    def phone_number_id(self):
        """
        Gets the phone_number_id of this SmsChallengeRequest.

        :return: The phone_number_id of this SmsChallengeRequest.
        :rtype: int
        """
        return self._phone_number_id

    @phone_number_id.setter
    def phone_number_id(self, phone_number_id):
        """
        Sets the phone_number_id of this SmsChallengeRequest.

        :param phone_number_id: The phone_number_id of this SmsChallengeRequest.
        :type: int
        """

        self._phone_number_id = phone_number_id

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
        if not isinstance(other, SmsChallengeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
