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
from payoneer_mobile_api.models.sign_documents_request import SignDocumentsRequest


class TestSignDocumentsRequest(unittest.TestCase):
    """ SignDocumentsRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSignDocumentsRequest(self):
        """
        Test SignDocumentsRequest
        """
        model = payoneer_mobile_api.models.sign_documents_request.SignDocumentsRequest()


if __name__ == '__main__':
    unittest.main()
