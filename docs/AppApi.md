# payoneer_mobile_api.AppApi

All URIs are relative to *https://mobileapi.payoneer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_app_start_post**](AppApi.md#app_app_start_post) | **POST** /App/AppStart | App Start
[**app_get_sign_documents_post**](AppApi.md#app_get_sign_documents_post) | **POST** /App/GetSignDocuments | Get Sign Documents
[**app_resource_get_post**](AppApi.md#app_resource_get_post) | **POST** /App/ResourceGet | Get Resource
[**app_resources_post**](AppApi.md#app_resources_post) | **POST** /App/Resources | Resources
[**app_sign_documents_post**](AppApi.md#app_sign_documents_post) | **POST** /App/SignDocuments | Sign Documents


# **app_app_start_post**
> AppStartResponse app_app_start_post(request)

App Start

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AppApi()
request = payoneer_mobile_api.AppStartRequest() # AppStartRequest | 

try: 
    # App Start
    api_response = api_instance.app_app_start_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_app_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AppStartRequest**](AppStartRequest.md)|  | 

### Return type

[**AppStartResponse**](AppStartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_get_sign_documents_post**
> GetSignDocumentsResponse app_get_sign_documents_post(request)

Get Sign Documents

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AppApi()
request = payoneer_mobile_api.GetSignDocumentsRequest() # GetSignDocumentsRequest | 

try: 
    # Get Sign Documents
    api_response = api_instance.app_get_sign_documents_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_get_sign_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetSignDocumentsRequest**](GetSignDocumentsRequest.md)|  | 

### Return type

[**GetSignDocumentsResponse**](GetSignDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_resource_get_post**
> ResourceGetResponse app_resource_get_post(request)

Get Resource

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AppApi()
request = payoneer_mobile_api.ResourceGetRequest() # ResourceGetRequest | 

try: 
    # Get Resource
    api_response = api_instance.app_resource_get_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_resource_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ResourceGetRequest**](ResourceGetRequest.md)|  | 

### Return type

[**ResourceGetResponse**](ResourceGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_resources_post**
> ResourcesResponse app_resources_post(request)

Resources

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AppApi()
request = payoneer_mobile_api.ResourcesRequest() # ResourcesRequest | 

try: 
    # Resources
    api_response = api_instance.app_resources_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_resources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ResourcesRequest**](ResourcesRequest.md)|  | 

### Return type

[**ResourcesResponse**](ResourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_sign_documents_post**
> SignDocumentsResponse app_sign_documents_post(request)

Sign Documents

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AppApi()
request = payoneer_mobile_api.SignDocumentsRequest() # SignDocumentsRequest | 

try: 
    # Sign Documents
    api_response = api_instance.app_sign_documents_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_sign_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SignDocumentsRequest**](SignDocumentsRequest.md)|  | 

### Return type

[**SignDocumentsResponse**](SignDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

