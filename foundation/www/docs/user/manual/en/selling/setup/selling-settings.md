# Selling Settings

Selling Setting is where you can define properties which will be applied to the masters and transactions involved in the sales cycle.

Let's check into each property one by one.

<img class="screenshot" alt="Selling Settings" src="{{docs_base_url}}/assets/img/selling/selling-settings.png">

####1. Customer Naming By

When a customer is saved, a unique ID is generated for that Customer.

By default, Customer ID is generated based on Customer Name. If you wish to save Customer using a naming series, in the field Customer Naming Series, set value as "Naming Series".

Example of Customer Id's saved in Naming Series - `CUST00001,CUST00002, CUST00003...` and so on.

You can set Naming Series for Customers from:

> Setup > Data > Naming Series

####2. Campaign Naming By

Just like for Customer, you can also configure naming methodology for the Campaign master as well. By default, Campaign will be saved with Campaign Name only.

####3. Default Customer Group and Territory

Select a default [Customer Group](/docs/user/manual/en/CRM/setup/customer-group.html) which will be auto-updated when creating a new Customer.

Quotations can be created for the Customers as well as for the Leads. When converting a Quotation into Sales Order, which is created for a Lead, the system attempts to convert that Lead into Customer. While creating Customer in the backend, values for Customer Group and Territory is picked from Selling Settings. If no default values are found for Customer Group or Territory, then you will receive a validation message asking for Customer Group or Territory. Or you can manually convert a Lead into Customer.

####5. Default Price List

Price List set in this field will be auto-updated in the Price List field of sales transactions like Quotation, Sales Order, Delivery Note and Sales Invoice.

####6. Close Opportunity After Days

If there are many Opportunities having a status other than Open, then they will be auto-closed after the no. of days mentioned in this field.

####7. Default Quotation Validity Days

Quotation Issues to the customer is Valid for certain days only. In the Quotation, you can update Valid Till Date manually. By default, the Valid Till date is auto-set as 30 days from the Quotation's Posting Date. You can change the no. of days in this field as per your business case.

####8. Sales Order Required

If you wish to make Sales Order creation mandatory before the creation of Sales Invoice, then you should set the Sales Order Required field as Yes. By default, this will be "No" for a value.

####9. Delivery Note Required

To make Delivery Note creation as mandatory before Sales Invoice creation, you should set this field as "Yes". By default, this will be "No" for a value.

####10. Maintain Same Rate Throughout Sales Cycle

The system by default validates that item price will be the same throughout the sales cycle (Sales Order - Delivery Note - Sales Invoice). If you could have item price changing within the cycle, and you need to bypass validation of the same rate throughout the cycle, then you should uncheck this field and save.

####11. Allow User to Edit Price List Rate in Transaction

Item table of the sale transactions has a field called Price List Rate. This field is non-editable by default in all the sales transactions. This is to ensure that price of an item is fetched from  Item Price record and the user is not able to edit it.

If you need to enable the user to edit Item Price, fetched from Price List of an item, you should uncheck this field.

####12. Allow multiple Sales Orders against a Customer's Purchase Order

When creating a Sales Order, you can update the Purchase Order ID and Date received from the Customer. You can create only one Sales Order against the Customer's PO No. and Date. However, if you wish to allow the creation of multiple Sales Order's against the same PO No. of the Customer, enable the property of "Allow multiple Sales Orders against a Customer's Purchase Order".

####13. Validate Selling Price for Item against Purchase Rate or Valuation Rate

When making sales, it's important to know if you are not selling it at a loss-making price. Enabling this validation will validate item's Selling Price with its valuation/buying price. If item's selling price is found to be less than it's buying price, then you will get a prompt indicating the same.

####14. Hide Customer's Tax Id from Sales Transactions

As per the statutory requirement, most of the Customers have unique Tax ID assigned to them. They also need to have this tax ID fetched in the selling transactions. However, if you don't wish to use this functionality, you can disable by checking this property.

{next}