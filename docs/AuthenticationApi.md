# payoneer_mobile_api.AuthenticationApi

All URIs are relative to *https://mobileapi.payoneer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_challenge_authenticate_post**](AuthenticationApi.md#authentication_challenge_authenticate_post) | **POST** /Authentication/ChallengeAuthenticate | ChallengeAuthenticate
[**authentication_challenge_cancel_post**](AuthenticationApi.md#authentication_challenge_cancel_post) | **POST** /Authentication/ChallengeCancel | ChallengeCancel
[**authentication_challenge_get_post**](AuthenticationApi.md#authentication_challenge_get_post) | **POST** /Authentication/ChallengeGet | ChallengeGet
[**authentication_challenge_refuse_sms_post**](AuthenticationApi.md#authentication_challenge_refuse_sms_post) | **POST** /Authentication/ChallengeRefuseSms | ChallengeRefuseSms
[**authentication_challenge_sms_post**](AuthenticationApi.md#authentication_challenge_sms_post) | **POST** /Authentication/ChallengeSms | ChallengeSms


# **authentication_challenge_authenticate_post**
> ChallengeAuthenticateResponse authentication_challenge_authenticate_post(request)

ChallengeAuthenticate

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AuthenticationApi()
request = payoneer_mobile_api.ChallengeAuthenticateRequest() # ChallengeAuthenticateRequest | 

try: 
    # ChallengeAuthenticate
    api_response = api_instance.authentication_challenge_authenticate_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_challenge_authenticate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ChallengeAuthenticateRequest**](ChallengeAuthenticateRequest.md)|  | 

### Return type

[**ChallengeAuthenticateResponse**](ChallengeAuthenticateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_challenge_cancel_post**
> BaseResponse authentication_challenge_cancel_post(request)

ChallengeCancel

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AuthenticationApi()
request = payoneer_mobile_api.BaseRequest() # BaseRequest | 

try: 
    # ChallengeCancel
    api_response = api_instance.authentication_challenge_cancel_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_challenge_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BaseRequest**](BaseRequest.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_challenge_get_post**
> GetChallengeResponse authentication_challenge_get_post(request)

ChallengeGet

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AuthenticationApi()
request = payoneer_mobile_api.GetChallengeRequest() # GetChallengeRequest | 

try: 
    # ChallengeGet
    api_response = api_instance.authentication_challenge_get_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_challenge_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetChallengeRequest**](GetChallengeRequest.md)|  | 

### Return type

[**GetChallengeResponse**](GetChallengeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_challenge_refuse_sms_post**
> BaseResponse authentication_challenge_refuse_sms_post(request)

ChallengeRefuseSms

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AuthenticationApi()
request = payoneer_mobile_api.BaseRequest() # BaseRequest | 

try: 
    # ChallengeRefuseSms
    api_response = api_instance.authentication_challenge_refuse_sms_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_challenge_refuse_sms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BaseRequest**](BaseRequest.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_challenge_sms_post**
> SmsChallengeResponse authentication_challenge_sms_post(request)

ChallengeSms

### Example 
```python
from __future__ import print_statement
import time
import payoneer_mobile_api
from payoneer_mobile_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = payoneer_mobile_api.AuthenticationApi()
request = payoneer_mobile_api.SmsChallengeRequest() # SmsChallengeRequest | 

try: 
    # ChallengeSms
    api_response = api_instance.authentication_challenge_sms_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_challenge_sms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SmsChallengeRequest**](SmsChallengeRequest.md)|  | 

### Return type

[**SmsChallengeResponse**](SmsChallengeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

