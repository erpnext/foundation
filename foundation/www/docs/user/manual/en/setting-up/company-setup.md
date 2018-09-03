# Company

A company is a legal entity made up of an association of people for carrying on a commercial or industrial enterprise.

In ERPNext, first Company is created on completion of account creation. For each Company, you can set a domain as manufacturing, retail, or services depending on the nature of your business activity.

If you have more than one company, you can add them from:

> Accounts > Company > New Company

### Company Tree Structure

> New in Version 11

The company is a tree-structured master. It allows you to define a federated and group company structure.

<img class="screenshot" alt="Company Tree" src="{{docs_base_url}}/assets/img/accounts/company-tree.png">

Once you build a company tree, ERPNext will validate that the accounts of the child companies will match the accounts in the parent company, so that you can consolidate all the accounts in a consolidated chart of accounts statement.

### Chart of Accounts

On each Company, the master for Chart of Account is maintained separately. This allows you to maintain separate accounting for each company as per the legal requirements.

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa.png">

ERPNext has localized Chart of Accounts readily available for some countries. When creating new Company, you can choose to setup Chart of Account for it from one of the following options.

* Standard Chart of Accounts
* Based on Existing Company's Chart of Account

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa-2.png">

### Default Values

Within the Company master, you can set lots of default values for master and accounts. These default account will help you in the quick posting of accounting transactions, where the value for the Account will be fetched from the Company master if provided. Following are the types of values for which default can be set in the Company master.

* Letter Head
* Bank Account
* Holiday List
* Sales Income Account
* Cost of Goods Sold Account
* Control Accounts related to perpetual inventory
* Accounts related to Fixed Asset accounting

{next}
