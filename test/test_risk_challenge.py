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
from payoneer_mobile_api.models.risk_challenge import RiskChallenge


class TestRiskChallenge(unittest.TestCase):
    """ RiskChallenge unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRiskChallenge(self):
        """
        Test RiskChallenge
        """
        model = payoneer_mobile_api.models.risk_challenge.RiskChallenge()


if __name__ == '__main__':
    unittest.main()