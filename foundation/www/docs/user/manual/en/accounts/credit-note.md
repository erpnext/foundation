<!-- add-breadcrumbs -->
## Credit Note

When you submit a sales invoice for $200...

1. 'Income Account' is credited i.e income is increased by $200 and 'Profit and Loss Statement' reflects this.
2. Customer is debited i.e amount the customer owes you is increased by $200 and 'Accounts Receivable' report reflects this.

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/sales_invoice_for_credit_note.gif">


In real world, sometimes you have to **reverse** your sales invoice partially or fully. This can happen for various reasons like...

* All or some of the goods you supplied was damaged in transit
* All or some the goods you supplied does not meet the quality standards of the customer
* You may have actually over billed the customer
* You agree to replace an item you sent with other item as a good will

In order to **reverse** the sales invoice you need to create a 'Credit Note'.  

A credit note is a document sent by a seller to the customer, notifying that a credit has been made to their account against the goods returned by the buyer.

A credit note is issued for the value of goods returned by the customer, it may be less than or equal to total amount of the order.

#### How to make credit note in ERPNext

1. If the 'Sales Invoice' against which you need to issue the 'Credit Note' exists in ERPNext, then you can open the sales invoice and click on 'Make' > 'Return / Credit Note' and update the quantity and rate and submit.
  Please note 'Is Return' is checked automatically and also the quantity needs to be in negative.

2. If the 'Sales Invoice' against which you need to issue the 'Credit Note' does not exist in ERPNext, then you can goto Accounts > Sales Invoice > New,  manually check 'Is Return' checkbox, set the quantity in negative, add other details like item, rate and finally submit.

Note: For 'Credit Note' it is mandatory that 'Is Return' is checked and quantity is in negative.

#### Example

Customer Mr. Sagar Malhotra has purchased Nokia Lumia worth Rs 42,400 and at the time of delivery, customer noticed that the item is damaged. Now Mr. Malhotra would like to return the product and get a refund. The 'Credit Note' and subsequent 'Payment Entry' needs to be prepared as shown below...

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/credit_note_example1.gif">

{next}
