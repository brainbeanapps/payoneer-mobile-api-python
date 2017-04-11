# coding: utf-8

"""
    Payoneer Mobile API

    Swagger specification for https://mobileapi.payoneer.com

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from payoneer_mobile_api.apis.account_api import AccountApi


class TestAccountApi(unittest.TestCase):
    """ AccountApi unit test stubs """

    def setUp(self):
        self.api = payoneer_mobile_api.apis.account_api.AccountApi()

    def tearDown(self):
        pass

    def test_account_account_post(self):
        """
        Test case for account_account_post

        Account Details
        """
        pass

    def test_account_billing_address_post(self):
        """
        Test case for account_billing_address_post

        Billing Address
        """
        pass

    def test_account_currencies_get_post(self):
        """
        Test case for account_currencies_get_post

        Currencies
        """
        pass

    def test_account_payment_method_details_post(self):
        """
        Test case for account_payment_method_details_post

        Payment Method Details
        """
        pass


if __name__ == '__main__':
    unittest.main()