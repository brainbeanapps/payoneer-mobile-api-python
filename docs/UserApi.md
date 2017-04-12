# payoneer_mobile_api.UserApi

All URIs are relative to *https://mobileapi.payoneer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get_user_settings_post**](UserApi.md#user_get_user_settings_post) | **POST** /User/GetUserSettings | Get User Settings
[**user_login_post**](UserApi.md#user_login_post) | **POST** /User/Login | User Login
[**user_logout_post**](UserApi.md#user_logout_post) | **POST** /User/Logout | User Logout
[**user_orn_link_post**](UserApi.md#user_orn_link_post) | **POST** /User/OrnLink | User ORN link
[**user_save_user_settings_post**](UserApi.md#user_save_user_settings_post) | **POST** /User/SaveUserSettings | Save User Settings


# **user_get_user_settings_post**
> GetUserSettingsResponse user_get_user_settings_post(request)

Get User Settings

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.UserApi()
request = payoneer_mobile_api.GetUserSettingsRequest() # GetUserSettingsRequest | 

try: 
    # Get User Settings
    api_response = api_instance.user_get_user_settings_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_user_settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetUserSettingsRequest**](GetUserSettingsRequest.md)|  | 

### Return type

[**GetUserSettingsResponse**](GetUserSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login_post**
> LoginResponse user_login_post(request)

User Login

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.UserApi()
request = payoneer_mobile_api.LoginRequest() # LoginRequest | 

try: 
    # User Login
    api_response = api_instance.user_login_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_logout_post**
> LogoutResponse user_logout_post(request)

User Logout

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.UserApi()
request = payoneer_mobile_api.LogoutRequest() # LogoutRequest | 

try: 
    # User Logout
    api_response = api_instance.user_logout_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_logout_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LogoutRequest**](LogoutRequest.md)|  | 

### Return type

[**LogoutResponse**](LogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_orn_link_post**
> OrnResponse user_orn_link_post(request)

User ORN link

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.UserApi()
request = payoneer_mobile_api.OrnRequest() # OrnRequest | 

try: 
    # User ORN link
    api_response = api_instance.user_orn_link_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_orn_link_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**OrnRequest**](OrnRequest.md)|  | 

### Return type

[**OrnResponse**](OrnResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_save_user_settings_post**
> GetUserSettingsResponse user_save_user_settings_post(request)

Save User Settings

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.UserApi()
request = payoneer_mobile_api.SaveUserSettingsRequest() # SaveUserSettingsRequest | 

try: 
    # Save User Settings
    api_response = api_instance.user_save_user_settings_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_save_user_settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveUserSettingsRequest**](SaveUserSettingsRequest.md)|  | 

### Return type

[**GetUserSettingsResponse**](GetUserSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

