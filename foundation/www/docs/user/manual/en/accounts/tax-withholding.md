<!-- add-breadcrumbs -->
# Tax Withholding
Withholding tax is a tax that is deducted by the payer of the income. This withholding tax is also called retention tax. Under withholding tax, the taxable amount is deducted at source by the payer i.e. the payer of the income is liable to deduct the withholding tax before making payment to the payee.
The withholding tax sounds similar to Tax deducted at source (TDS).

 tax withholding can be setup based on Supplier.

To use Tax Withholding feature in ERPNext, first, you need to create Tax Withholding Category record. Here, you can mention percent of tax withheld and threshold amount (if any). Here, the threshold amount means tax will be deducted only if the order value is greater than or equal to the threshold value. You also need to link related accounts to the Tax Withholding Category record.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category.png">

To enable Tax Withholding for any Supplier, you need to mention applicable percent against tax withholding category.

<img class="screenshot" alt="Tax Withholding for Supplier" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-for-supplier.png">


