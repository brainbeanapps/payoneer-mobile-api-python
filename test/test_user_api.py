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
from payoneer_mobile_api.apis.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = payoneer_mobile_api.apis.user_api.UserApi()

    def tearDown(self):
        pass

    def test_user_get_user_settings_post(self):
        """
        Test case for user_get_user_settings_post

        Get User Settings
        """
        pass

    def test_user_login_post(self):
        """
        Test case for user_login_post

        User login
        """
        pass

    def test_user_logout_post(self):
        """
        Test case for user_logout_post

        User Logout
        """
        pass

    def test_user_orn_link_post(self):
        """
        Test case for user_orn_link_post

        User ORN link
        """
        pass

    def test_user_save_user_settings_post(self):
        """
        Test case for user_save_user_settings_post

        Save User Settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
