
## Asset

Asset record is the heart of fixed asset management feature. All the transactions related to Asset like purchasing, sales, depreciation, scrapping, movement or maintenance will be managed against the Asset record.


There are two use cases for creating an asset record. The asset can be existing asset which has been bought erlier and it might already been depreciated partially. Or the asset is a newly purchased item.

For the existing asset, you can create the asset record directly checking "Is Existing Asset" field. In this case, you also need to enter already booked depreciation amount and number of booked depreciation. And based on the input, system will create a schedule for remaining depreciation.

<img class="screenshot" alt="Existing Asset" src="{{docs_base_url}}/assets/img/asset/existing-asset.png">

For new asset, you cannot create the asset record directly from Asset master. Asset record will be created automatically on submission of Purchase Receipt / Purchase Invoice for the Asset. And later you can modify the details of the asset record. Find more details in [Purchasing Asset.]({{ docs_base_url }}/user/manual/en/asset/purchasing-asset.html)

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset.png">

Explanation of the fields:

1. Item Code: An Item for the Asset must be a non-stock item, with "Is Asset" field checked.

	<img class="screenshot" alt="Asset Item" src="{{docs_base_url}}/assets/img/asset/asset-item.png">

2. Asset Category: The category of assets it belongs to.
3. Is Existing Asset: Check if the asset is being carried forward from the previous Fiscal Year. The existing assets which are partially / fully depreciated can also be created/maintained for the future reference.
4. Status: The options are - Draft, Submitted, Partially Depreciated, Fully Depreciated, Sold and Scrapped.
5. Location: Set the location of the asset.
6. Gross Purchase Amount: The purchase cost of the asset.
7. Depreciation Start Date: The date from which booking of depreciation will be started.
8. Expected Value After Useful Life: Useful Life is the time period over in which the company expects that the asset will be productive. After that period, either the asset is scrapped or sold. In case it is sold, mention the estimated value here. This value is also known as Salvage Value, Scrap Value or Residual Value.
9. Opening Accumulated Depreciation: The accumulated depreciation amount which has already been booked for an existing asset.
10. Available-for-use Date: The date from which the asset has been started to use. The depreciation for the first period will be calculated from this date.
11. Current Value (After Depreciation): In case you are creating record of an existing asset which has already been partially/fully depreciated, mention the current value of the asset. In case of new asset, mention the purchase amount or leave it blank.
12. Depreciation Method: There are two options: Straight Line and Double Declining Balance.
	- Straight Line: This method spreads the cost of the fixed asset evenly over its useful life.
	- Double Declining Method: An accelerated method of depreciation, it results in higher depreciation expense in the earlier years of ownership.
13. Total Number of Depreciations: The total number of depreciations during the useful life. In case of existing assets which are partially depreciated, mention the number of pending depreciations.
14. Number of Depreciations Booked: Enter the number of already booked depreciations for an existing asset.
15. Frequency of Depreciation (Months): The number of months between two depreciations.
16. Next Depreciation Date: Mention the next depreciation date, even if it is the first one. If the asset is an existing one and depreciation has already been completed, leave it blank.

### Accounting Entry

On submission of an asset, "Capital Work in Progress" account will be credited and the asset account related to the asset will be debited. Submission is only possible after entering "Available-to-use Date". If "Available-to-use Date" is a future date, then accounting entry will be booked automatically on that date via scheduler.

{next}
