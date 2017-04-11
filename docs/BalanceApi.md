# payoneer_mobile_api.BalanceApi

All URIs are relative to *https://mobileapi.payoneer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_balance_post**](BalanceApi.md#balance_balance_post) | **POST** /Balance/Balance | Balance


# **balance_balance_post**
> BalanceResponse balance_balance_post(request)

Balance

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.BalanceApi()
request = payoneer_mobile_api.BalanceRequest() # BalanceRequest | 

try: 
    # Balance
    api_response = api_instance.balance_balance_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->balance_balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BalanceRequest**](BalanceRequest.md)|  | 

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

