<!-- add-breadcrumbs -->
# Invoicing
Billing is an integral part of any undertaking and ERPNext Healthcare achieves this by making use of the features made available as part of ERPNext Accounts module.

The healthcare domain links Patient document with `Customer` and all billable services like, Lab Tests, Clinical Procedures, Consulting Fees etc. with `Item` document _(with Maintain Stock set to false)_. You can set the links manually too.

The Sales Invoice already has the `Get Items` button which helps User to get a list of Items from other related documents. ERPNext Healthcare brings two more option here to fetch un-billed services for a Patient as well as prescribed medications from Patient Encounter. This way, the billing user can fetch all billable services as well as prescribed medications without having to have access to the Healthcare module.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/get_items.png">

> Note: All transactions of a Patient is booked against the Customer which it is linked to.



{next}
