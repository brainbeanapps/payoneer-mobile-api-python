# payoneer_mobile_api.TransactionApi

All URIs are relative to *https://mobileapi.payoneer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_pre_auth_transactions_post**](TransactionApi.md#transaction_pre_auth_transactions_post) | **POST** /Transaction/PreAuthTransactions | Pre-Authorization Transactions
[**transaction_transaction_details_post**](TransactionApi.md#transaction_transaction_details_post) | **POST** /Transaction/TransactionDetails | Transaction Details
[**transaction_transactions_post**](TransactionApi.md#transaction_transactions_post) | **POST** /Transaction/Transactions | Transactions


# **transaction_pre_auth_transactions_post**
> PreAuthTransactionsResponse transaction_pre_auth_transactions_post(request)

Pre-Authorization Transactions

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.TransactionApi()
request = payoneer_mobile_api.PreAuthTransactionsRequest() # PreAuthTransactionsRequest | 

try: 
    # Pre-Authorization Transactions
    api_response = api_instance.transaction_pre_auth_transactions_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->transaction_pre_auth_transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PreAuthTransactionsRequest**](PreAuthTransactionsRequest.md)|  | 

### Return type

[**PreAuthTransactionsResponse**](PreAuthTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_transaction_details_post**
> TransactionDetailsResponse transaction_transaction_details_post(request)

Transaction Details

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.TransactionApi()
request = payoneer_mobile_api.TransactionDetailsRequest() # TransactionDetailsRequest | 

try: 
    # Transaction Details
    api_response = api_instance.transaction_transaction_details_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->transaction_transaction_details_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TransactionDetailsRequest**](TransactionDetailsRequest.md)|  | 

### Return type

[**TransactionDetailsResponse**](TransactionDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_transactions_post**
> TransactionsListResponse transaction_transactions_post(request)

Transactions

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.TransactionApi()
request = payoneer_mobile_api.TransactionsListRequest() # TransactionsListRequest | 

try: 
    # Transactions
    api_response = api_instance.transaction_transactions_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->transaction_transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TransactionsListRequest**](TransactionsListRequest.md)|  | 

### Return type

[**TransactionsListResponse**](TransactionsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

