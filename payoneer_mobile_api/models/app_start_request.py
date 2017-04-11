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


class AppStartRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, device_id=None, mac=None, mobile_app_id=None, app_version=None, language_code=None, mobile_platform_type=None, partner_id=None, timestamp=None, is_first_app_start=None):
        """
        AppStartRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'device_id': 'DeviceId',
            'mac': 'str',
            'mobile_app_id': 'MobileAppId',
            'app_version': 'AppVersion',
            'language_code': 'LanguageCode',
            'mobile_platform_type': 'int',
            'partner_id': 'int',
            'timestamp': 'date',
            'is_first_app_start': 'bool'
        }

        self.attribute_map = {
            'device_id': 'DeviceId',
            'mac': 'MAC',
            'mobile_app_id': 'MobileAppId',
            'app_version': 'AppVersion',
            'language_code': 'LanguageCode',
            'mobile_platform_type': 'MobilePlatformType',
            'partner_id': 'PartnerId',
            'timestamp': 'Timestamp',
            'is_first_app_start': 'IsFirstAppStart'
        }

        self._device_id = device_id
        self._mac = mac
        self._mobile_app_id = mobile_app_id
        self._app_version = app_version
        self._language_code = language_code
        self._mobile_platform_type = mobile_platform_type
        self._partner_id = partner_id
        self._timestamp = timestamp
        self._is_first_app_start = is_first_app_start

    @property
    def device_id(self):
        """
        Gets the device_id of this AppStartRequest.

        :return: The device_id of this AppStartRequest.
        :rtype: DeviceId
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this AppStartRequest.

        :param device_id: The device_id of this AppStartRequest.
        :type: DeviceId
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")

        self._device_id = device_id

    @property
    def mac(self):
        """
        Gets the mac of this AppStartRequest.

        :return: The mac of this AppStartRequest.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """
        Sets the mac of this AppStartRequest.

        :param mac: The mac of this AppStartRequest.
        :type: str
        """

        self._mac = mac

    @property
    def mobile_app_id(self):
        """
        Gets the mobile_app_id of this AppStartRequest.

        :return: The mobile_app_id of this AppStartRequest.
        :rtype: MobileAppId
        """
        return self._mobile_app_id

    @mobile_app_id.setter
    def mobile_app_id(self, mobile_app_id):
        """
        Sets the mobile_app_id of this AppStartRequest.

        :param mobile_app_id: The mobile_app_id of this AppStartRequest.
        :type: MobileAppId
        """
        if mobile_app_id is None:
            raise ValueError("Invalid value for `mobile_app_id`, must not be `None`")

        self._mobile_app_id = mobile_app_id

    @property
    def app_version(self):
        """
        Gets the app_version of this AppStartRequest.

        :return: The app_version of this AppStartRequest.
        :rtype: AppVersion
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """
        Sets the app_version of this AppStartRequest.

        :param app_version: The app_version of this AppStartRequest.
        :type: AppVersion
        """
        if app_version is None:
            raise ValueError("Invalid value for `app_version`, must not be `None`")

        self._app_version = app_version

    @property
    def language_code(self):
        """
        Gets the language_code of this AppStartRequest.

        :return: The language_code of this AppStartRequest.
        :rtype: LanguageCode
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this AppStartRequest.

        :param language_code: The language_code of this AppStartRequest.
        :type: LanguageCode
        """

        self._language_code = language_code

    @property
    def mobile_platform_type(self):
        """
        Gets the mobile_platform_type of this AppStartRequest.

        :return: The mobile_platform_type of this AppStartRequest.
        :rtype: int
        """
        return self._mobile_platform_type

    @mobile_platform_type.setter
    def mobile_platform_type(self, mobile_platform_type):
        """
        Sets the mobile_platform_type of this AppStartRequest.

        :param mobile_platform_type: The mobile_platform_type of this AppStartRequest.
        :type: int
        """

        self._mobile_platform_type = mobile_platform_type

    @property
    def partner_id(self):
        """
        Gets the partner_id of this AppStartRequest.

        :return: The partner_id of this AppStartRequest.
        :rtype: int
        """
        return self._partner_id

    @partner_id.setter
    def partner_id(self, partner_id):
        """
        Sets the partner_id of this AppStartRequest.

        :param partner_id: The partner_id of this AppStartRequest.
        :type: int
        """

        self._partner_id = partner_id

    @property
    def timestamp(self):
        """
        Gets the timestamp of this AppStartRequest.

        :return: The timestamp of this AppStartRequest.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AppStartRequest.

        :param timestamp: The timestamp of this AppStartRequest.
        :type: date
        """

        self._timestamp = timestamp

    @property
    def is_first_app_start(self):
        """
        Gets the is_first_app_start of this AppStartRequest.

        :return: The is_first_app_start of this AppStartRequest.
        :rtype: bool
        """
        return self._is_first_app_start

    @is_first_app_start.setter
    def is_first_app_start(self, is_first_app_start):
        """
        Sets the is_first_app_start of this AppStartRequest.

        :param is_first_app_start: The is_first_app_start of this AppStartRequest.
        :type: bool
        """
        if is_first_app_start is None:
            raise ValueError("Invalid value for `is_first_app_start`, must not be `None`")

        self._is_first_app_start = is_first_app_start

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
        if not isinstance(other, AppStartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
