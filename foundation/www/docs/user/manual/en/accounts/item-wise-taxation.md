<!-- add-breadcrumbs -->
# Itemised Taxation

In the sales and purchase transactions, you can apply taxes and other charges on the items. For the ease of applying taxes, you can fetch values from the [Sales Taxes and Charges master](/docs/user/manual/en/setting-up/setting-up-taxes). Taxes and charges are applied equally on all the items. For example, if tax GST 16% is added in the Taxes and Charges table in Sales Order, then it will be applied on all the items in that Sales Order. However, if you need to have different tax rate applied on some of the items, following is how you should setup Items and Sales Taxes and Charges Template master in your ERPNext account. 

Let's assume that we are creating a Sales Order. We have Sales Taxes and Charges Template master for GST 16%. Out of all the Sales Items, on one item, only 5% GST will be applied, while one more item is exempted from the tax.

####Step 1: Mention Tax Applicable in the Item master

Items on which differential tax rate is applied, you should mention the tax, that you would apply in the Sales Order, for that item in the Item master itself and change the Tax Rate (in this case 5). Item master has tax table where you can list taxes which will be applied on it.

> Tax rate mentioned in the item master gets preference over tax rate entered in the transactions.

Here is the example of Item on which 5% GST is applied only.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/item-wise-tax.png">

For the item which is exempted from GST totally, mention 0% as tax rate in the Item master. 

> Note: For Item Tax to work, you need to ensure that the Tax accounts set in Item Tax table (with changed tax rates) in Item master are part of the _default_ Sales / Purhcase Tax Template.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/exempted-item.png">

####Step 2: Setup Taxes and Other Charges

In Sales Taxes and Charges Template master, select GST 16% account and mention Tax Rate as 16. This tax rate will be applied on all the Items selected in the Sales Order, unless specific Tax Rate is defined in the Item master.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-master.png">

<div class="well">If you want to have tax rate always applied from the Item master, then you should update Rate for the tax account as zero in the Taxes and Charges Template master.</div>

####Step 3: Tax Calculation in transaction	

In the Sales Order, we have selected many Items. For the items mentioned in blue, tax rate is applied based on tax rate mentioned in the taxes table. For the items highlighted in red, tax rate has fetched for them from the respective item master.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-calculation.png">

Please note that item's tax rate will be pulled from the item master only if you have selected same tax account (GST 16% in this case) in both Item master and in Sales Order under Taxes and Charges section.

{next}
