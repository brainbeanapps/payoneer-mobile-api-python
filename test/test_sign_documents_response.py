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
from payoneer_mobile_api.models.sign_documents_response import SignDocumentsResponse


class TestSignDocumentsResponse(unittest.TestCase):
    """ SignDocumentsResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSignDocumentsResponse(self):
        """
        Test SignDocumentsResponse
        """
        model = payoneer_mobile_api.models.sign_documents_response.SignDocumentsResponse()


if __name__ == '__main__':
    unittest.main()
