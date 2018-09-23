### Depreciations

The system automatically creates a schedule for depreciation based on depreciation method and other related inputs in the Asset record. It is also possible to create multiple depreciation schedule for different Finance Book.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/depreciation-schedule.png">

On the scheduled date, system creates depreciation entry by creating a Journal Entry and the same Journal Entry is updated in the depreciation table for reference. Next Depreciation Date and Current Value are also updated on submission of depreciation entry.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/depreciation-entry.png">

In the depreciation entry, the "Accumulated Depreciation Account" is credited and "Depreciation Expense Account" is debited. The related accounts can be set in the Asset Category or Company.

You can enable booking of depreciaiton entry automatically from "Account Settings". This will create depreciation entry automatically on scheduled date via scheduler. Otherwise, you have to create Journal Entry manually by clicking "Make Depreciation Entry" in corresponding Depreciation Schedule row.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/book-asset-depreciation-accounting-automatically.png">

The system will automatically set the fiscal year end date as the next depreciation date and calculate the depreciation amount prorata temporis based on the Available-for-use Date (IFRS16)

<img class="screenshot" alt="Asset" src="/docs/assets/img/asset/asset_prorated_depreciation.png">

For better visibility, net value of the asset on different depreciation dates are shown in a line graph.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-graph.png">

{next}
