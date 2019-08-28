# swagger_client.DefaultApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repositories_scan_all_post**](DefaultApi.md#repositories_scan_all_post) | **POST** /repositories/scanAll | Scan all images of the registry.


# **repositories_scan_all_post**
> repositories_scan_all_post(project_id=project_id)

Scan all images of the registry.

The server will launch different jobs to scan each image on the regsitry, so this is equivalent to calling  the API to scan the image one by one in background, so there's no way to track the overall status of the \"scan all\" action.  Only system adim has permission to call this API.   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | When this parm is set only the images under the project identified by the project_id will be scanned. (optional)

try:
    # Scan all images of the registry.
    api_instance.repositories_scan_all_post(project_id=project_id)
except ApiException as e:
    print("Exception when calling DefaultApi->repositories_scan_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| When this parm is set only the images under the project identified by the project_id will be scanned. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

