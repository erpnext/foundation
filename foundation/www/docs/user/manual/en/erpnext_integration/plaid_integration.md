<!-- add-breadcrumbs -->
# Plaid Integration

ERPNext offers the possibility to synchronize your bank accounts through a service called [Plaid](https://plaid.com/).

If your instance is connected to Plaid, you are able to synchronize your bank account transactions without having to manually import a CSV or XLSX file.


## Settings

In order to give ERPNext access to Plaid, you need to add the following three parameters to your `site_config.json` file.

- plaid_client_id
- plaid_env
- plaid_public_key
- plaid_secret

## Activation

In order to activate Plaid on an instance, click on the button "Enable" in the Plaid Settings DocType.

<img class="screenshot" alt="Enable Plaid" src="{{docs_base_url}}/assets/img/erpnext_integrations/plaid_enable.gif">

Once activated, you can create a new account directly from the Bank Reconciliation dashboard.


## Bank account creation

In order to link one of your existing bank accounts to ERPNext, click on "Link a new bank account" and follow the steps proposed by Plaid.

<img class="screenshot" alt="Link your bank account" src="{{docs_base_url}}/assets/img/erpnext_integrations/new_account_creation.gif">


## Bank synchronization

In order to synchronize a bank account with ERPNext, select an account and click on the "Action" button to select "Synchronize this account".

<img class="screenshot" alt="Synchronize your bank account" src="{{docs_base_url}}/assets/img/erpnext_integrations/plaid_synchronization.gif">

The synchronization is based on the "Last integration date" available in the "Bank Account" doctype.

If, for any reason, you want to redo a synchronization, you can change this date and synchronize the account again.
Since all bank transactions are tagged with a specific transaction ID, the synchronization will only be incremental.


## Automatic Synchronization

You can allow plaid to synchronize your bank account with ERPNex every hour by selecting "Synchronize all accounts every hour" in Plaid Settings.