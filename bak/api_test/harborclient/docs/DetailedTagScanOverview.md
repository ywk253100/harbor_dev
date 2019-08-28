# DetailedTagScanOverview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | The digest of the image. | [optional] 
**scan_status** | **str** | The status of the scan job, it can be \&quot;pendnig\&quot;, \&quot;running\&quot;, \&quot;finished\&quot;, \&quot;error\&quot;. | [optional] 
**job_id** | **int** | The ID of the job on jobservice to scan the image. | [optional] 
**severity** | **int** | 0-Not scanned, 1-Negligible, 2-Unknown, 3-Low, 4-Medium, 5-High | [optional] 
**details_key** | **str** | The top layer name of this image in Clair, this is for calling Clair API to get the vulnerability list of this image. | [optional] 
**components** | [**DetailedTagScanOverviewComponents**](DetailedTagScanOverviewComponents.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


