# PaymentMethodDetailsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **int** | 1 - Success; 34 - (Assumption) Terms&amp;Conditions not agreed; | [optional] 
**balance** | [**PaymentMethodBalance**](PaymentMethodBalance.md) |  | [optional] 
**recent_payments** | [**list[PaymentHeaderResponse]**](PaymentHeaderResponse.md) |  | [optional] 
**last_transactions** | [**list[TransactionHeaderResponse]**](TransactionHeaderResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


