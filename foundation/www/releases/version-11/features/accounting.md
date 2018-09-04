# Finance + Accounting Enhancements

ERPNext in Version 11 accounting has a lot of enhancements that make it an Enterprise-Ready ERP system. Here is a summary of the highlights

### Company Tree

ERPNext already supports multi-company, in Version 11, the company is now a tree structure so you can create holding companies and consolidate financial reports within a group of companies. ERPNext also ensures that the chart of accounts of the child company is mapped to the parent Company

<img class="screenshot" alt="Marketplace" src="/assets/foundation/img/version-11/company-tree.png">

### Multiple Finance Books

With the new concept of **Finance Book**, you can now make journal entries that are only posted to specific Financial Books. This is useful if you have to report depreciation and other values in different ways based on regulatory requirements. You can also use this to post alternate balance sheets for your internal reporting.

### Bank Statement Upload

Bank Statement Import allows you to define the standard format of your Bank's statement export and then allows you to import the your bank statement. The tool will also help you reconcile payments, make new payments and match them with invoices.

### Tax Witholding

ERPNext will now automatically calculate tax to be witheld from suppliers based on rules, so now operators don't have to manually look up rules and calculate tax to be witheld before making payments.

### Subscriptions and Deferred Revenue

If you are servicing subscriptions or contracts that go across financial periods, it makes sense to book revenue in the correct period so you can defer the tax liability to the actual period where you deliver the service. ERPNext will now let you setup subscriptions and automatically book revenue monthly or quarterly based on your settings.

[Learn about Deferred Revenue](https://erpnext.org/docs/user/manual/en/accounts/deferred-revenue)

<img class='screenshot' alt='Setting up Deferred Revenue' src=
'https://erpnext.org/docs/assets/img/accounts/deferred-invoice.gif'>

### Inter Company Transactions

Inter-company transactions allow you to post validated back-to-back transactions across companies. These include Journal Entries, Sales and Purchase Invoices. In the company master you have to specify which companies are allowed to transact with each other and then you can make inter company transactions on those companies.

[Learn more about Inter Company Journal Entry](https://erpnext.org/docs/user/manual/en/accounts/inter-company-journal-entry) and [Inter Company Invoice](https://erpnext.org/docs/user/manual/en/accounts/inter-company-invoices)

### Standalone Credit / Debit Note

Debit and Credit notes can now be made as stand alone documents. In Version 10 and earlier, these could be made only against an existing Sales or Purchase.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WIF0aJSY06o" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Reverse Journal Entry

You can now automatically pass a reverse Journal Entry to that will swap the debits and credits in order to reverse a particular transaction.

### Enhanced Bank Guarantee

You can now track Bank Guarantees in given to customers and track its expiry via Email Alert

[Learn more about Bank Guarantee](https://erpnext.org/docs/user/manual/en/accounts/bank-guarantee)

### Cost Center Numbering

Account Numbering System has now been extended to Cost Centers.



