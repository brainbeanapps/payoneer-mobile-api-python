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
from payoneer_mobile_api.models.get_challenge_response import GetChallengeResponse


class TestGetChallengeResponse(unittest.TestCase):
    """ GetChallengeResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetChallengeResponse(self):
        """
        Test GetChallengeResponse
        """
        model = payoneer_mobile_api.models.get_challenge_response.GetChallengeResponse()


if __name__ == '__main__':
    unittest.main()
