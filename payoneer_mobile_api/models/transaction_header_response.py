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


class TransactionHeaderResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, transaction_id=None, date=None, description=None, amount=None, transaction_status_category=None):
        """
        TransactionHeaderResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'transaction_id': 'str',
            'date': 'str',
            'description': 'str',
            'amount': 'str',
            'transaction_status_category': 'int'
        }

        self.attribute_map = {
            'transaction_id': 'TransactionId',
            'date': 'Date',
            'description': 'Description',
            'amount': 'Amount',
            'transaction_status_category': 'TransactionStatusCategory'
        }

        self._transaction_id = transaction_id
        self._date = date
        self._description = description
        self._amount = amount
        self._transaction_status_category = transaction_status_category

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this TransactionHeaderResponse.

        :return: The transaction_id of this TransactionHeaderResponse.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this TransactionHeaderResponse.

        :param transaction_id: The transaction_id of this TransactionHeaderResponse.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def date(self):
        """
        Gets the date of this TransactionHeaderResponse.

        :return: The date of this TransactionHeaderResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this TransactionHeaderResponse.

        :param date: The date of this TransactionHeaderResponse.
        :type: str
        """

        self._date = date

    @property
    def description(self):
        """
        Gets the description of this TransactionHeaderResponse.

        :return: The description of this TransactionHeaderResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TransactionHeaderResponse.

        :param description: The description of this TransactionHeaderResponse.
        :type: str
        """

        self._description = description

    @property
    def amount(self):
        """
        Gets the amount of this TransactionHeaderResponse.

        :return: The amount of this TransactionHeaderResponse.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this TransactionHeaderResponse.

        :param amount: The amount of this TransactionHeaderResponse.
        :type: str
        """

        self._amount = amount

    @property
    def transaction_status_category(self):
        """
        Gets the transaction_status_category of this TransactionHeaderResponse.

        :return: The transaction_status_category of this TransactionHeaderResponse.
        :rtype: int
        """
        return self._transaction_status_category

    @transaction_status_category.setter
    def transaction_status_category(self, transaction_status_category):
        """
        Sets the transaction_status_category of this TransactionHeaderResponse.

        :param transaction_status_category: The transaction_status_category of this TransactionHeaderResponse.
        :type: int
        """

        self._transaction_status_category = transaction_status_category

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
        if not isinstance(other, TransactionHeaderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
