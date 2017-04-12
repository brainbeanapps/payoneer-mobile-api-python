# payoneer_mobile_api.PaymentApi

All URIs are relative to *https://mobileapi.payoneer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_payment_details_post**](PaymentApi.md#payment_payment_details_post) | **POST** /Payment/PaymentDetails | Payment Details
[**payment_payments_post**](PaymentApi.md#payment_payments_post) | **POST** /Payment/Payments | Payments


# **payment_payment_details_post**
> PaymentDetailsResponse payment_payment_details_post(request)

Payment Details

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.PaymentApi()
request = payoneer_mobile_api.PaymentDetailsRequest() # PaymentDetailsRequest | 

try: 
    # Payment Details
    api_response = api_instance.payment_payment_details_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->payment_payment_details_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PaymentDetailsRequest**](PaymentDetailsRequest.md)|  | 

### Return type

[**PaymentDetailsResponse**](PaymentDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_payments_post**
> PaymentsHistoryResponse payment_payments_post(request)

Payments

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.PaymentApi()
request = payoneer_mobile_api.PaymentsHistoryRequest() # PaymentsHistoryRequest | 

try: 
    # Payments
    api_response = api_instance.payment_payments_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->payment_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PaymentsHistoryRequest**](PaymentsHistoryRequest.md)|  | 

### Return type

[**PaymentsHistoryResponse**](PaymentsHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

