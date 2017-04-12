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


class PaymentDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, payment_id=None, payment_date=None, payment_status=None, payee_id=None, loader_details=None, payment_amount=None, extra_details=None):
        """
        PaymentDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'payment_id': 'LabelValuePair',
            'payment_date': 'LabelValuePair',
            'payment_status': 'LabelValuePair',
            'payee_id': 'LabelValuePair',
            'loader_details': 'LabelValuePair',
            'payment_amount': 'LabelValuePair',
            'extra_details': 'list[LabelValuePair]'
        }

        self.attribute_map = {
            'payment_id': 'PaymentId',
            'payment_date': 'PaymentDate',
            'payment_status': 'PaymentStatus',
            'payee_id': 'PayeeId',
            'loader_details': 'LoaderDetails',
            'payment_amount': 'PaymentAmount',
            'extra_details': 'ExtraDetails'
        }

        self._payment_id = payment_id
        self._payment_date = payment_date
        self._payment_status = payment_status
        self._payee_id = payee_id
        self._loader_details = loader_details
        self._payment_amount = payment_amount
        self._extra_details = extra_details

    @property
    def payment_id(self):
        """
        Gets the payment_id of this PaymentDetails.

        :return: The payment_id of this PaymentDetails.
        :rtype: LabelValuePair
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """
        Sets the payment_id of this PaymentDetails.

        :param payment_id: The payment_id of this PaymentDetails.
        :type: LabelValuePair
        """

        self._payment_id = payment_id

    @property
    def payment_date(self):
        """
        Gets the payment_date of this PaymentDetails.

        :return: The payment_date of this PaymentDetails.
        :rtype: LabelValuePair
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """
        Sets the payment_date of this PaymentDetails.

        :param payment_date: The payment_date of this PaymentDetails.
        :type: LabelValuePair
        """

        self._payment_date = payment_date

    @property
    def payment_status(self):
        """
        Gets the payment_status of this PaymentDetails.

        :return: The payment_status of this PaymentDetails.
        :rtype: LabelValuePair
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """
        Sets the payment_status of this PaymentDetails.

        :param payment_status: The payment_status of this PaymentDetails.
        :type: LabelValuePair
        """

        self._payment_status = payment_status

    @property
    def payee_id(self):
        """
        Gets the payee_id of this PaymentDetails.

        :return: The payee_id of this PaymentDetails.
        :rtype: LabelValuePair
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """
        Sets the payee_id of this PaymentDetails.

        :param payee_id: The payee_id of this PaymentDetails.
        :type: LabelValuePair
        """

        self._payee_id = payee_id

    @property
    def loader_details(self):
        """
        Gets the loader_details of this PaymentDetails.

        :return: The loader_details of this PaymentDetails.
        :rtype: LabelValuePair
        """
        return self._loader_details

    @loader_details.setter
    def loader_details(self, loader_details):
        """
        Sets the loader_details of this PaymentDetails.

        :param loader_details: The loader_details of this PaymentDetails.
        :type: LabelValuePair
        """

        self._loader_details = loader_details

    @property
    def payment_amount(self):
        """
        Gets the payment_amount of this PaymentDetails.

        :return: The payment_amount of this PaymentDetails.
        :rtype: LabelValuePair
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """
        Sets the payment_amount of this PaymentDetails.

        :param payment_amount: The payment_amount of this PaymentDetails.
        :type: LabelValuePair
        """

        self._payment_amount = payment_amount

    @property
    def extra_details(self):
        """
        Gets the extra_details of this PaymentDetails.

        :return: The extra_details of this PaymentDetails.
        :rtype: list[LabelValuePair]
        """
        return self._extra_details

    @extra_details.setter
    def extra_details(self, extra_details):
        """
        Sets the extra_details of this PaymentDetails.

        :param extra_details: The extra_details of this PaymentDetails.
        :type: list[LabelValuePair]
        """

        self._extra_details = extra_details

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
        if not isinstance(other, PaymentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other