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
from payoneer_mobile_api.models.app_version import AppVersion


class TestAppVersion(unittest.TestCase):
    """ AppVersion unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAppVersion(self):
        """
        Test AppVersion
        """
        model = payoneer_mobile_api.models.app_version.AppVersion()


if __name__ == '__main__':
    unittest.main()