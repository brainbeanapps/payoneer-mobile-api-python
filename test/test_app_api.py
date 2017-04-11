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
from payoneer_mobile_api.apis.app_api import AppApi


class TestAppApi(unittest.TestCase):
    """ AppApi unit test stubs """

    def setUp(self):
        self.api = payoneer_mobile_api.apis.app_api.AppApi()

    def tearDown(self):
        pass

    def test_app_app_start_post(self):
        """
        Test case for app_app_start_post

        App Start
        """
        pass

    def test_app_get_sign_documents_post(self):
        """
        Test case for app_get_sign_documents_post

        Get Sign Documents
        """
        pass

    def test_app_resource_get_post(self):
        """
        Test case for app_resource_get_post

        Get Resource
        """
        pass

    def test_app_resources_post(self):
        """
        Test case for app_resources_post

        Resources
        """
        pass

    def test_app_sign_documents_post(self):
        """
        Test case for app_sign_documents_post

        Sign Documents
        """
        pass


if __name__ == '__main__':
    unittest.main()
