<!-- add-breadcrumbs -->
# Tax Withholding Category

Tax Withholding Category is simply Tax Deducted at Source. According to this, a person responsible for making payments are required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the govt wants the payers to deduct tax before hand and deposit it with the government.

To create a **Tax Withholding Category** go to:

> Accounts > Taxes > Tax Withholding Category > New

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category.png">

In a Tax Withholding Category, you must select.

  * A unique name for the tax category (for example, "Section 194C Individual").
  * The name or description should be filled in the Category Name field (for example, "Payment to Contractors (Single / Aggregate)").
  * Add rows for the rates applicable in current fiscal year. In each row, you must specify: 
    * The current Fiscal Year.
    * The rate to be applied on the invoice amount.
    * The threshold for a single invoice.
    * The threshold for the sum of amount of invoices.
  * Add rows for the Account head to be used (company wise). In each row, you must specify: 
    * The name of the Company.
    * The Account head where the tax amount will be credited to.

> Note:- Lets say a rate of 5% will be applicable on invoice where Single threshold is 20,000 and Cumulative threshold is 30,000. If an invoice is created with a grand total of 20,000 then the single threshold will be triggered and a 5% tax would be charged. But if the invoce amount totalled up to be 15,000 then no tax will be charged as it didn't cross the threshold. If again an invoice is created with a total of 15,000 then although it didn't cross the Single threshold, charges will be deducted since the sum of last invoice and this invoice adds up to be 30,000 which is equal to the specified Cumulative threshold.

* * *

## Supplier

Select the Tax Category that needs to be applied on the Supplier.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-1.png">

* * *

## Purchase Invoice

If the **Supplier** has the tax withholding field set, then upon selecting that supplier, a checkbox will become visible to select whether to apply tax or not.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-2.png">

* * *

## How it works?

#### Setting up - 

* Firstly, we need to create a **Tax Withholding Category** like -

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-3.png">

<br>

* Go to Supplier master and select the tax category created.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-4.png">

<br>

#### Creating Invoive - 

* Go to **Purchase Invoice** and select the supplier from above.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-5.png">

<br>

* Saving the invoice, automatically calculates tax and appends it in the taxes table.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-6.png">

<br>

* Incase of Cumulative threshold, lets create an invoice with a total of 15,000 and submit it.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-7.png">

<br>

* Now, lets create another invoice same as the above. Although the invoice amount didn't cross the Single threshold, we see that tax has been charged. This is because the previous and the current invoice adds up to be 30,000 which exceeds the Cumulative threshold and hence tax based on the rate provided in the **Tax Withholding Category** are applied accordingly.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-8.png">

> Note: On submitting the invoice, three GL Entry are created i.e. first for debit from the expense head, second for credit in Creditors account and third for credit in the account selected in Tax Withholding Category.

{next}
