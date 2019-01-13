<!-- add-breadcrumbs -->
# Setting Up Taxes

One of the primary motivator for compulsory use of accounting tools is
calculation of Taxes. You may or may not make money but your government will
(to help your country be safe and prosperous). And if you don’t calculate your
taxes correctly, they get very unhappy. Ok, philosophy aside, ERPNext allows
you to make configurable tax templates that you can apply to your sales or
purchase.

### Tax Accounts

For Tax Accounts that you want to use in the tax templates, you must go to
Chart of Accounts and mention them as type “Tax” in your Chart of Item.

## Sales Taxes and Charges Template

You must usually collect taxes from your Customer and pay them to the
government. At times, you may have to pay multiple taxes to multiple
government bodies like local government, state or provincial and federal or
central government.

The way ERPNext sets up taxes is via templates. Other types of charges that
may apply to your invoices (like shipping, insurance etc.) can also be
configured as taxes.

Select template and modify as per your need.

To create a new Sales Taxes and Charges Template, you
have to go to:

> Accounting > Taxes > Sales Taxes and Charges Template

<img class="screenshot" alt="Sales Taxes and Charges Template" src="{{docs_base_url}}/assets/img/taxes/sales-taxes-and-charges-template.png">

When you are creating a Taxes and Charges template, you have to add a row for each type of tax or charge.

The tax rate you define here will be the standard tax rate for all Items. If
there are Items that are supposed have different rates, you can override the standard tax rate by setting an
Item Tax Template to the Item or Item Group.

In each row, you have to mention:

  * **Calculation Type**:

    * **On Net Total**: A tax rate will be applied as a percentage of the net total (total amount without taxes).
    * **On Previous Row Total/Amount**: A tax rate will be applied as a percentage of a previous tax row (in the tax table) total or amount.
    In the Reference Row # Field, mention row number on which you want to apply the current tax.
    If you want to apply the tax on the 3rd row, mention "3" in the Reference Row # field.

    * **Actual**: A fixed tax amount will be applied.

  * **Account Head**: The Account ledger under which this tax will be booked

  * **Cost Center**: If the tax / charge is an income (like shipping) it needs to be booked against - a Cost Center.
  * **Description**: Description of the tax (that will be printed in invoices / quotes).
  * **Rate**: Tax rate.
  * **Amount**: Tax amount.
  * **Total**: Cumulative total to this point.
  * **Reference Row #**: If based on "Previous Row Total/Amount" you can select the row number which will be taken as a base for this calculation (default is the previous row).
  * **Is this Tax included in Basic Rate?**: If you check this,
  it means that this tax will be considered as already included in the amount in the Item table of a transaction.
  This is useful when you want to give tax inclusive price to your customers. To account for tax inclusive rates,
  the system calculates the Net Amount by deducting the amount of tax to be applied then calculates the tax on it.
  

<img class="screenshot" alt="Inclusive Tax" src="{{docs_base_url}}/assets/img/taxes/taxes-and-charges-detail.png">

Once you setup your template, you can select this in your sales transactions.

## Purchase Taxes and Charges Template

Similar to your Sales Taxes and Charges Template is the Purchase Taxes and
Charges Template.

To create a new Purchase Taxes and Charges Template, you have to go to:

> Accounting > Taxes > Purchase Taxes and Charges Template

This is the tax template that you can use in your Purchase Orders and Purchase
Invoices. If you have value added taxes (VAT), where you pay to the government
the difference between your incoming and outgoing taxes, you can select the
same Account that you use for sales taxes.

The columns in this table are similar to the Sales Taxes and Charges Template
with the difference as follows:

**Consider Tax or Charge for**: In this section you can specify if the tax /
charge is only for valuation (not a part of total) or only for total (does not
add value to the item) or for both.

## Item Tax Template

If some of your Items require tax rates different from the standard tax rate assigned in the Taxes and Charges table,
then you can create an Item Tax Template and assign it to an Item or Item Group.
The rate assigned in the Item Tax Template will get preference over the standard tax rate assigned in the Taxes and Charges table.
The Item Tax Template rate will be applied on that Item instead.

To create an Item Tax Template, go to
> Accounting > Taxes > Item Tax Template

Select the Account Head of the tax and set its overriding rate
<img class="screenshot" alt="Item Tax in Item Master" src="{{docs_base_url}}/assets/img/taxes/item-tax-template.png">

You can assign Item Tax Templates to an Item Master by modifying the Item Tax table in the Item Tax section within the Item Master document.
<img class="screenshot" alt="Item Tax in Item Master" src="{{docs_base_url}}/assets/img/taxes/item-tax.png">

You can assign the Item Tax Template to an Item Group by modifying the Item Tax table in the Item Tax section within the Item Group document.
<img class="screenshot" alt="Item Tax in Item Group" src="{{docs_base_url}}/assets/img/taxes/item-group-tax.png">

If you set the Tax Category as empty, it will be considered the default Item Tax Template will be applied to items in transactions by default.
You can apply different Item Tax Templates for different Tax Categories.

For an Item Tax Template to override taxes, there must be a row in the Taxes and Charges table with the same tax Account Head with a standard tax rate.
If you wish to apply taxes only on the items with an Item Tax Template then you can set the standard tax rate as 0.
By default ERPNext will automatically set the Taxes and Charges table for you, however, you can change this by changing the Accounts Settings:

> Accounting > Setup > Accounts Settings > Automatically Add Taxes and Charges from Item Tax Template

## Tax Category
If you want to apply different kinds of taxes based on Tax Categories, create Tax Categories from:

> Accounting > Taxes > Tax Category

Tax Category is automatically determined in a transaction by either the Party Address or Party Master.

  * You can assign Tax Category to specific Parties (Customers and Suppliers).
  * You can assign Tax Category to specific Billing or Shipping Address
  * You can select whether Billing Address or Shipping Address gets preference by changing the Accounts Settings.
  * Tax Category is determined from Party Address first. If the Address is not assigned any Tax Category, then the Party's Tax Category is used.
  * You can also manually select the Tax Category in a transaction.
  
What effect does the Tax Category has in a transaction?

  * Specific Item Tax Templates for that Tax Category are automatically set for items.
  * You can create [Tax Rules]({{docs_base_url}}/user/manual/en/accounts/setup/tax-rule)
  to automatically set a specific Sales / Purchase Taxes and Charges Template based on different Tax Categories
  in transactions.


<div>
  <div class="embed-container">
    <iframe src="https://www.youtube.com/embed/a8Eh4zLIrkU?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
  </div>
</div>

{next}

