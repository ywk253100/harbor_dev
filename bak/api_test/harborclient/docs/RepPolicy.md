# RepPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The policy ID. | [optional] 
**name** | **str** | The policy name. | [optional] 
**description** | **str** | The description of the policy. | [optional] 
**projects** | [**list[Project]**](Project.md) | The project list that the policy applys to. | [optional] 
**targets** | [**list[RepTarget]**](RepTarget.md) | The target list. | [optional] 
**trigger** | [**RepTrigger**](RepTrigger.md) |  | [optional] 
**filters** | [**list[RepFilter]**](RepFilter.md) | The replication policy filter array. | [optional] 
**replicate_existing_image_now** | **bool** | Whether to replicate the existing images now. | [optional] 
**replicate_deletion** | **bool** | Whether to replicate the deletion operation. | [optional] 
**creation_time** | **str** | The create time of the policy. | [optional] 
**update_time** | **str** | The update time of the policy. | [optional] 
**error_job_count** | **int** | The error job count number for the policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


