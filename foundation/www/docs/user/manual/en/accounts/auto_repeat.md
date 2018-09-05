<!-- add-breadcrumbs -->
# Auto Repeat

Auto Repeat feature helps you create certain transaction automatically in a given time period.

## Use Case

Assuming that you follow deferred expense system for some items. It requires you to create same Journal Entry each month to Cr. Deferred Expense a/c to Dr. Expense Account. You can create first Journal Entry manually for it, and then create auto-repeat transaction for it.

<img class="screenshot" alt="Subscription" src="{{docs_base_url}}/assets/img/accounts/subscription.png">

#### Auto Repeat

To set the subscription for the sales invoice Go to Subscription > select base doctype "Sales Invoice" > select base docname "Invoice No" > Save

<img class="screenshot" alt="Subscription" src="{{docs_base_url}}/assets/img/accounts/subscription.gif">

**From Date and To Date**: This defines contract period with the customer.

**Repeat on Day**: If frequency is set as Monthly, then it will be day of the month on which recurring invoice will be generated.

**Notify By Email**: If you want to notify the user about auto recurring invoice.

**Print Format**: Select a print format to define document view which should be emailed to customer.

**Disabled**: It will stop to make auto recurring documents against the subscription.

### Difference between Subscription and Auto Repeat

