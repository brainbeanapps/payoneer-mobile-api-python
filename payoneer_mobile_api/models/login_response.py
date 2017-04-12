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


class LoginResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, response_code=None, first_name=None, last_name=None, raf_link=None, raf_link_menu=None, email=None, local_currency=None, display_tc=None, permissions=None, orn_link=None, description=None, risk_challenge=None, mobile_session_token=None):
        """
        LoginResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'response_code': 'int',
            'first_name': 'str',
            'last_name': 'str',
            'raf_link': 'str',
            'raf_link_menu': 'str',
            'email': 'str',
            'local_currency': 'str',
            'display_tc': 'bool',
            'permissions': 'list[AccountPermission]',
            'orn_link': 'str',
            'description': 'str',
            'risk_challenge': 'ChallengeResponse',
            'mobile_session_token': 'str'
        }

        self.attribute_map = {
            'response_code': 'ResponseCode',
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'raf_link': 'RAFLink',
            'raf_link_menu': 'RAFLinkMenu',
            'email': 'Email',
            'local_currency': 'LocalCurrency',
            'display_tc': 'DisplayTC',
            'permissions': 'Permissions',
            'orn_link': 'ORNLink',
            'description': 'Description',
            'risk_challenge': 'RiskChallenge',
            'mobile_session_token': 'MobileSessionToken'
        }

        self._response_code = response_code
        self._first_name = first_name
        self._last_name = last_name
        self._raf_link = raf_link
        self._raf_link_menu = raf_link_menu
        self._email = email
        self._local_currency = local_currency
        self._display_tc = display_tc
        self._permissions = permissions
        self._orn_link = orn_link
        self._description = description
        self._risk_challenge = risk_challenge
        self._mobile_session_token = mobile_session_token

    @property
    def response_code(self):
        """
        Gets the response_code of this LoginResponse.
        1 - Success; 34 - (Assumption) Terms&Conditions not agreed;

        :return: The response_code of this LoginResponse.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this LoginResponse.
        1 - Success; 34 - (Assumption) Terms&Conditions not agreed;

        :param response_code: The response_code of this LoginResponse.
        :type: int
        """

        self._response_code = response_code

    @property
    def first_name(self):
        """
        Gets the first_name of this LoginResponse.

        :return: The first_name of this LoginResponse.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this LoginResponse.

        :param first_name: The first_name of this LoginResponse.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this LoginResponse.

        :return: The last_name of this LoginResponse.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this LoginResponse.

        :param last_name: The last_name of this LoginResponse.
        :type: str
        """

        self._last_name = last_name

    @property
    def raf_link(self):
        """
        Gets the raf_link of this LoginResponse.

        :return: The raf_link of this LoginResponse.
        :rtype: str
        """
        return self._raf_link

    @raf_link.setter
    def raf_link(self, raf_link):
        """
        Sets the raf_link of this LoginResponse.

        :param raf_link: The raf_link of this LoginResponse.
        :type: str
        """

        self._raf_link = raf_link

    @property
    def raf_link_menu(self):
        """
        Gets the raf_link_menu of this LoginResponse.

        :return: The raf_link_menu of this LoginResponse.
        :rtype: str
        """
        return self._raf_link_menu

    @raf_link_menu.setter
    def raf_link_menu(self, raf_link_menu):
        """
        Sets the raf_link_menu of this LoginResponse.

        :param raf_link_menu: The raf_link_menu of this LoginResponse.
        :type: str
        """

        self._raf_link_menu = raf_link_menu

    @property
    def email(self):
        """
        Gets the email of this LoginResponse.

        :return: The email of this LoginResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this LoginResponse.

        :param email: The email of this LoginResponse.
        :type: str
        """

        self._email = email

    @property
    def local_currency(self):
        """
        Gets the local_currency of this LoginResponse.

        :return: The local_currency of this LoginResponse.
        :rtype: str
        """
        return self._local_currency

    @local_currency.setter
    def local_currency(self, local_currency):
        """
        Sets the local_currency of this LoginResponse.

        :param local_currency: The local_currency of this LoginResponse.
        :type: str
        """

        self._local_currency = local_currency

    @property
    def display_tc(self):
        """
        Gets the display_tc of this LoginResponse.

        :return: The display_tc of this LoginResponse.
        :rtype: bool
        """
        return self._display_tc

    @display_tc.setter
    def display_tc(self, display_tc):
        """
        Sets the display_tc of this LoginResponse.

        :param display_tc: The display_tc of this LoginResponse.
        :type: bool
        """

        self._display_tc = display_tc

    @property
    def permissions(self):
        """
        Gets the permissions of this LoginResponse.

        :return: The permissions of this LoginResponse.
        :rtype: list[AccountPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this LoginResponse.

        :param permissions: The permissions of this LoginResponse.
        :type: list[AccountPermission]
        """

        self._permissions = permissions

    @property
    def orn_link(self):
        """
        Gets the orn_link of this LoginResponse.

        :return: The orn_link of this LoginResponse.
        :rtype: str
        """
        return self._orn_link

    @orn_link.setter
    def orn_link(self, orn_link):
        """
        Sets the orn_link of this LoginResponse.

        :param orn_link: The orn_link of this LoginResponse.
        :type: str
        """

        self._orn_link = orn_link

    @property
    def description(self):
        """
        Gets the description of this LoginResponse.

        :return: The description of this LoginResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LoginResponse.

        :param description: The description of this LoginResponse.
        :type: str
        """

        self._description = description

    @property
    def risk_challenge(self):
        """
        Gets the risk_challenge of this LoginResponse.

        :return: The risk_challenge of this LoginResponse.
        :rtype: ChallengeResponse
        """
        return self._risk_challenge

    @risk_challenge.setter
    def risk_challenge(self, risk_challenge):
        """
        Sets the risk_challenge of this LoginResponse.

        :param risk_challenge: The risk_challenge of this LoginResponse.
        :type: ChallengeResponse
        """

        self._risk_challenge = risk_challenge

    @property
    def mobile_session_token(self):
        """
        Gets the mobile_session_token of this LoginResponse.

        :return: The mobile_session_token of this LoginResponse.
        :rtype: str
        """
        return self._mobile_session_token

    @mobile_session_token.setter
    def mobile_session_token(self, mobile_session_token):
        """
        Sets the mobile_session_token of this LoginResponse.

        :param mobile_session_token: The mobile_session_token of this LoginResponse.
        :type: str
        """

        self._mobile_session_token = mobile_session_token

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
        if not isinstance(other, LoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
