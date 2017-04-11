# payoneer_mobile_api.AccountApi

All URIs are relative to *https://mobileapi.payoneer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_account_post**](AccountApi.md#account_account_post) | **POST** /Account/Account | Account Details
[**account_billing_address_post**](AccountApi.md#account_billing_address_post) | **POST** /Account/BillingAddress | Billing Address
[**account_currencies_get_post**](AccountApi.md#account_currencies_get_post) | **POST** /Account/CurrenciesGet | Currencies
[**account_payment_method_details_post**](AccountApi.md#account_payment_method_details_post) | **POST** /Account/PaymentMethodDetails | Payment Method Details


# **account_account_post**
> AccountResponse account_account_post(request)

Account Details

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AccountApi()
request = payoneer_mobile_api.AccountRequest() # AccountRequest | 

try: 
    # Account Details
    api_response = api_instance.account_account_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountRequest**](AccountRequest.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_billing_address_post**
> BillingAddressResponse account_billing_address_post(request)

Billing Address

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AccountApi()
request = payoneer_mobile_api.BillingAddressRequest() # BillingAddressRequest | 

try: 
    # Billing Address
    api_response = api_instance.account_billing_address_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_billing_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingAddressRequest**](BillingAddressRequest.md)|  | 

### Return type

[**BillingAddressResponse**](BillingAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_currencies_get_post**
> CurrenciesGetResponse account_currencies_get_post(request)

Currencies

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AccountApi()
request = payoneer_mobile_api.CurrenciesGetRequest() # CurrenciesGetRequest | 

try: 
    # Currencies
    api_response = api_instance.account_currencies_get_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_currencies_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CurrenciesGetRequest**](CurrenciesGetRequest.md)|  | 

### Return type

[**CurrenciesGetResponse**](CurrenciesGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_payment_method_details_post**
> PaymentMethodDetailsResponse account_payment_method_details_post(request)

Payment Method Details

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AccountApi()
request = payoneer_mobile_api.PaymentMethodDetailsRequest() # PaymentMethodDetailsRequest | 

try: 
    # Payment Method Details
    api_response = api_instance.account_payment_method_details_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_payment_method_details_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PaymentMethodDetailsRequest**](PaymentMethodDetailsRequest.md)|  | 

### Return type

[**PaymentMethodDetailsResponse**](PaymentMethodDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

