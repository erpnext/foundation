<!-- add-breadcrumbs -->
# Bank Reconciliation

### Bank Reconciliation Statement

If you are receiving payments or making payments via cheques, the bank statements will not accurately match the dates of your entry, this is because the bank usually takes time to “clear” these payments. Also you may have mailed a cheque to your Supplier and it may be a few days before it is received and deposited by the Supplier. In ERPNext you can synchronise your bank statements and your Journal Entries using the “Bank Reconciliation” tool.

The Bank Reconciliation Report provide the difference between the bank balance shown in an organisation's bank statement, as provided by the bank against amount shown in the companies Chart of Accounts.

####Bank Reconciliation Statement

<img class="screenshot" alt="Bank Reconciliation statement" src="{{docs_base_url}}/assets/img/accounts/bank-reconciliation-2.png">  

In the report, check whether the field 'Balance as per bank' matches the Bank Account Statement. If it is matching, it means that Clearance Date is correctly updated for all the bank entries. If there is a mismatch, Its because of bank entries for which Cleanrane Date is not yet updated.


ERPNext has two reconciliation tool:

1. A manual reconciliation tool allowing to set clearance dates against payment entries, sales invoice payments or journal entries
2. A semi-automatic reconciliation tool allowing to clear bank transactions against payments entries, sales and purchase invoices payments, journal entries or expense claims.

###Manual Bank Reconciliation Tool

To add clearance entries go to:

`Accounts > Tools > Bank Reconciliation`

Select your “Bank” Account and enter the dates of your statement. Here you
will get all the “Bank Voucher” type entries. In each of the entry on the
right most column, update the “Clearance Date” and click on “Update”.

By doing this you will be able to sync your bank statements and entries into
the system.

__Step 1:__ Select the Bank Account against which you intend to reconcile. For
example; HDFC Bank, ICICI Bank, or Citibank etc.

__Step 2:__ Select the Date range that you wish to reconcile for.

__Step 3:__ Click on 'Get Reconciled Entries'

All the entries in the specified date range will be shown in a table below.

__Step 4:__ Click on the JV from the table and update clearance date.

<img class="screenshot" alt="Bank Reconciliation" src="{{docs_base_url}}/assets/img/accounts/bank-reconciliation.png">

__Step 5:__ Click on the button 'Update Clearance Date'.
 

### Semi-automatic Bank Reconciliation Tool

1. Bank statement upload

You can upload a Bank Statement in CSV or XLX format into ERPNext using the Bank Reconciliation tool.

  a. Download a bank statement from your bank's website

  <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/sample_bank_statement.png">
  Make sure you have at least the date, the debit/credit and the currency on every row of your bank statement.

  b. Configure the import format in the Bank DocType

  <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/bank_configuration.png">

  Your file will be read and then ERPNext will use this mapping to dispatch all information into the corresponding fields in the Bank Transaction DocType.

  c. Upload your file into ERPNext

  <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/bank_transaction_upload.gif">



2. Bank account synchronization

You can use Plaid (see ERPNext Integrations section) to automatically synchronize your bank account with ERPNext.
All your bank transactions will be automatically imported into ERPNext.

3. Bank reconciliation

Once all your bank transactions are imported into ERPNext, you can reconcile them with your existing payments.


If it finds a payment that appear to match with the selected bank transaction, ERPNext will propose you a corresponding payment.
If that payment matches, just click on reconcile to reconcile it with this bank transaction.

<img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/auto_reconciliation.gif">


If ERPNext doesn't propose you any payment, you can always select the corresponding payment manually:

<img class="screenshot" alt="Reconcile bank transactions manually" src="{{docs_base_url}}/assets/img/accounts/manual_reconciliation.gif">


You can also create a new payment or invoice directly from the bank reconciliation dashboard.

<img class="screenshot" alt="New payment entry" src="{{docs_base_url}}/assets/img/accounts/new_payment.gif">


{next}