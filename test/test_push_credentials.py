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
from payoneer_mobile_api.models.push_credentials import PushCredentials


class TestPushCredentials(unittest.TestCase):
    """ PushCredentials unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPushCredentials(self):
        """
        Test PushCredentials
        """
        model = payoneer_mobile_api.models.push_credentials.PushCredentials()


if __name__ == '__main__':
    unittest.main()
