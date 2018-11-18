<!-- add-breadcrumbs -->
# Billing

Billing is an integral part of any undertaking and ERPNext Healthcare achieves this by making use of the `Sales Invoice` document in the ERPNext Accounts module.

The Healthcare domain links Patient document with `Customer` and all billable services like, Lab Tests, Clinical Procedures, Consulting Fees etc. with the `Item` document _(with Maintain Stock set to false)_. You can set the links manually too.

The Sales Invoice already has the `Get Items` button which helps User to get a list of Items from other related documents. ERPNext Healthcare brings two more option here to fetch all un-billed services for a Patient as well as prescribed medications from Patient Encounter. This way, the billing user can fetch all billable services as well as medications without having to have access to the Patient Encounter or the Healthcare module itself.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/get_items.png">

> Note: All transactions of a Patient are booked against the Customer which it is linked to. You may want to look up various Accounting Reports available in ERPNext Accounts module (like Accounts Receivable) using this Customer link.

{next}
