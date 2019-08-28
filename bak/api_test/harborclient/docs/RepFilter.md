# RepFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The replication policy filter kind. The valid values are project, repository and tag. | [optional] 
**value** | **str** | The value of replication policy filter. When creating repository and tag filter, filling it with the pattern as string. When creating label filter, filling it with label ID as integer. | [optional] 
**pattern** | **str** | Depraceted, use value instead. The replication policy filter pattern. | [optional] 
**metadata** | **object** | This map object is the replication policy filter metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


