<!-- add-breadcrumbs -->
# Clinical Procedure
You can use this document to map all the clinical procedures, for example, wound cleaning or a cataract surgery. ERPNext allows you to preconfigure Clinical Procedure Templates, so that you do not have to set the default properties like the consumables every time you order a procedure. You can read more on this in the [Setting Up Practice](/docs/user/manual/en/healthcare/setup/setup_practice.html) page.

You can create a Clinical Procedure by going to
`Healthcare > Patient Care > New Clinical Procedure`

### Procedure Actions
The Practitioner can update the procedure status of the Procedure to _In Progress_ by clicking the **Start** button. For the procedure to start, adequate quantity of all consumables in the Healthcare Service Unit's Warehouse. If this fails, you can easily record a _Stock Transfer_ from the same screen.

When the procedure is completed, the practitioner can update the _Consumables_ table with the actual values of the stock quantity that are used. The **Consume and Complete** button will record consumption by booking a stock entry and the update the status of the Clinical Procedure to _Completed_. If the Procedure does not have any stock items in the Consumables table, you can merely **Complete** the procedure.

### Billing
You can create Invoices for procedures performed on a patient by going to Sales Invoice > Get Items From > Healthcare Services. This way the billing officer need not access the Healthcare module documents and the un-billed services for a Patient will be listed which the officer can chose from.

If the **Invoice Consumables Separately** option is turned on, the charges for the consumable Items will be added to the Sales Invoice separately.

{next}
