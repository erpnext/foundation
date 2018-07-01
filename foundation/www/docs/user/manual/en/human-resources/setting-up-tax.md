<!-- add-breadcrumbs -->
#Setting Up Income Tax Deduction
Calculating Tax deductions for employees every month is a time consuming activity for most businesses, especially for large enterprises. If setup properly, ERPNext simplifies most of the tax related calculations by automatically calculating tax deductions while generating Salary Slips. Here's how you can configure ERPNext to ease you payroll processing -

#Payroll Period


#Income Tax Exemption

In many countries, especially in India, regulations allow exempting a part (or all) of some type of spendings by individuals from being added to their annual taxable income. Examples of such spendings could be contributions to charitable institutions, amount spent for education of children, specific investments etc. To
avail the exemption from their taxable income, individuals are required to submit proof of such spendings.

ERPNext allows you to configure Tax Slabs as part of every Payroll Period and the applies tax on each Salary based on projected annual earnings of the employee. Tax thus calculated will be added to the Salary Slip for  deduction Salary Component configured **Variable Based On Taxable Salary**. Employees are required to declare the exemption amount they plan to claim at the end of the fiscal year so that the payroll deductions for tax will be calculated based on the projected annual earnings less the exemption. Employees can declare this through [Employee Tax Exemption Declaration](/docs/user/manual/en/human-resources/employee-tax-exemption-declaration.html), the total of which will be exempted from annual taxable earnings of the employee.

If no declaration is submitted by the employee, the monthly deductions will be calculated without any exemption from the employee's annual earnings. However, if the employee submits a declaration in between the payroll period, from the next payroll onwards the exemption will be applied from the next payroll. Any additional tax collected in earlier payrolls will be adjusted in the last payroll or when using **Deduct Tax For Unsubmitted Tax Exemption Proof** in Payroll Entry or Salary Slip.

Also, at the end of the year employees submit the actual proof of the spendings for filing via [Employee Tax Exemption Proof Submission](/docs/user/manual/en/human-resources/employee-tax-exemption-proof-submission.html). In the last payroll of the Payroll Period, ERPNext checks for proof submissions of employees and if not found, tax for the exempted income will be aded to the standard deduction component.

###Employee Tax Exemption Category
Exemptions from taxable salary are usually restricted to spendings on particular categories decided by government or regulatory agencies. ERPNext allows you to configure various categories which are allowed to be exempted. Examples of this could be, for India, 80G, 80C, B0CC etc.

You can configure Employee Tax Exemption Category by going to,
> Human resources > Payroll Setup > Employee Tax Exemption Category > New Employee Tax Exemption Category

<img class="screenshot" alt="Employee Tax Exemption Category" src="/docs/assets/img/human-resources/employee-tax-exemption-category.png">

###Employee Tax Exemption Sub Category
Under each category, there could be many heads for which the exemptions are allowed. For example, in India, sub categories under 80C could be Life Insurance Premium

You can configure Employee Tax Exemption Sub Category by going to,
> Human resources > Payroll Setup > Employee Tax Exemption Sub Category > New Employee Tax Sub Exemption Category

<img class="screenshot" alt="Employee Tax Exemption Sub Category" src="/docs/assets/img/human-resources/employee-tax-exemption-subcategory.png">

###HRA Exemption - Regional, India
For the fiscal year 2018-19, in India, House Rent Allowance (HRA) exemption from taxable earnings is the minimum of:
 * The actual amount allotted by the employer as the HRA.
 * Actual rent paid less 10% of the basic salary.
 * 50% of the basic salary, if the employee is staying in a metro city (40% for a non-metro city).

 As part of the Employee Tax Exemption Declaration, employees shall also fill out the HRA Exemption. ERPNext will calculate the exemption eligible for HRA and exempt it while calculating the taxable earnings.

 > Note: HRA component shall be configured in Company for HRA exemption to work

###Options in Payroll Entry
ERPNext simplifies payroll processing by automatically processing payroll in bulk via [Payroll Entry](/docs/user/manual/en/human-resources/payroll-entry.html).

* Deduct Tax For Unclaimed Employee Benefits: Flexible benefits (Salary Components which are **Is Flexible Benefit**) are not included in the taxable income of the employee. However, the amount received for these components will be included in the taxable earnings of the employee if she fails to submit [Employee Benefit Claim](/docs/user/manual/en/human-resources/employee-benefit-claim.html) while calculating tax in the last payroll of the Payroll Period.

If you wish to collect tax for benefits before the last payroll, check this option and ERPNext will recalculate the tax and add the tax for all untaxed benefits while generating the Salary Slip.

* Deduct Tax For Unsubmitted Tax Exemption Proof: This option allows you to deduct taxes for the earnings which were exempted in previous payrolls as declared in **Employee Tax Exemption Declaration** but the Employee has not submitted sufficient proof **Employee Tax Exemption Proof Submission**. It is to be noted that if this option is checked ERPNext does not consider the Employee Tax Exemption Declaration by employees and will only take into account **Employee Tax Exemption Proof Submission** instead, while calculating exemption from employees' annual earnings.

>Note: If required, you can still process payroll for employees individually, by manually creating a new Salary Slip and both these options are made available in the Salary Slip

{next}
