# Subscription

If you offer a service which requires renewal in the certain time period (yearly, monthly, quarterly etc.), you can use Subscription feature to track them. Subscription master captures all the details required for the auto-creation of Sales Invoice on subscription expiry.

Let's consider a use-case of ERPNext subscription itself. Our hosting plans are available on yearly basis. Each customer's account has subscription expiry date, after which customer must renew their subscription with us.

To manage client's subscription expiry and auto-generation of Sales Invoice for the renewal, we use Subscription feature.

### Subscription Validity

**Start Date:** Day from when the subscription will be valid.

**Days Until Due:** Enter no. of days for which subscription will be valid.

Based on the subscription start and end date, actual dates for invoices will be calculated.

### Subscription Plan

The subscription plan is linked to an Item, for which Sales Invoice is created.

<img class="screenshot" alt="Subscription" src="{{docs_base_url}}/assets/img/accounts/item-subscriber.png">

### Taxes

Select Taxes and Charges which will be applicable in the Sales Invoice created against this Subscription.

### Discounts

Mention discounts if any which will be applied on this particular subscription.

### Difference Between Subscription and Auto-Repeat

Before Subscription feature was added in ERPNext, the current Auto-Repeat feature was available as a Subscription only.

The Auto-Repeat feature which is applicable for multiple transactions like Sales Order, Purchase Order, Invoices, Journal Entry etc. Whereas based on Subscription, only Sales Invoices are auto-created.

**Disabled**: It will stop to make auto recurring documents against the subscription

{next}
