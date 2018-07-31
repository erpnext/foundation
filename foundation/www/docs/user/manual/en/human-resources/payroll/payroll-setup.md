<!-- add-breadcrumbs -->
# Payroll Setup

Salary is a fixed amount of money or compensation paid to an employee by an employer in return for the work performed.

Payroll is the administration of financial records of employees' salaries, wages, bonuses, net pay, and deductions.

To process Payroll in ERPNext,

1. Define [Payroll Period](/docs/user/manual/en/human-resources/payroll/payroll-period.html) (optional)
2. Create Salary Structure with Salary Components (Earnings and Deductions)
3. Assign Salary Structures to each Employee via Salary Structure Assignment
4. Generate Salary Slips via [Payroll Entry](/docs/user/manual/en/human-resources/payroll/payroll-entry.html).
5. Book the Salary in your Accounts.

## Payroll Period
[Payroll Period](/docs/user/manual/en/human-resources/payroll/payroll-period.html), in ERPNext, is a period for which Employees get paid for their occupation with the Company. Payroll period helps you define Tax slabs applicable for the period, making it easier to manage changing laws.

> Note: Configuring Payroll Period is optional if you do not intend to use Flexible Benefits or Tax Slabs

## Salary Component
This document allows you to define each Earning and Deduction component which can be used to create a Salary Structure and subsequently create Salary Slip or Additional Salary. You can also configure the type, condition and formula as well as other settings which are discussed below. You should be able to enable various combinations of the following options to configure each component as it fits your Company / Regional policies.

* Depends on Leave Without Pay: Leave Without Pay (LWP) happens when an Employee runs out of allocated leaves
or takes a leave without an approval (via Leave Application). If enabled, ERPNext will automatically deduct the
pay in proportion of LWP days divided by the total working days for the month (based on the Holiday List).

	> Note: If you don’t want ERPNext to manage LWP, don’t turn on this flag in any of the Salary Components

* Do not include in total: If this option is enabled, the component wont be added to the total of the Earnings or Deductions of the Salary Slip

#### Earning

<img class="screenshot" alt="Salary Component Earnings"
	src="{{docs_base_url}}/assets/img/human-resources/salary-component.png">

* Is Additional Component: This option specify that the component can only be paid as Additional Salary. Examples of this component could be Performance Bonus or pay received for on-site deputation etc. Such components are not considered to be part of normal Salary Structure. Instead, Additional Salary with these components can be submitted as required which will be added to the Salary Slip automatically.

* Is Tax Applicable: If a component needs to be considered for Tax calculations specified as per the Payroll Period you may want to enable this option. It would be required that you have a Payroll Period configured with valid Tax Slabs for payroll processing.

* Is Payable: Such components can be booked against separate payable accounts and the Accounts shall be configured in the Accounts table

* Flexible Benefits: Flexible Benefits are earning components which Employees can choose to receive on a pro-rata basis or annually when they claim for. These are mostly tax exempted, unless the Employee fail to file the claim with adequate bills / documents. If turned on, you can specify the maximum benefit allowed for an employee in a year. Employees can create [Employee Benefit Application](/docs/user/manual/en/human-resources/payroll/employee-benfit-application.html) with the ones they opt for.

	>Note: Employee Benefit Application will only allow Employees to only choose from the flexible components which are present in the Salary Structure assigned to the Employee

	- Pay Against Benefit Claim: Employees can opt to receive flexible benefits annually via Employee Benefit Claim or along with their salary every month. If you enable this, the amount allocated for the component will be paid as the Employee submits an [Employee Benefit Claim](/docs/user/manual/en/human-resources/payroll/employee-benefit-claim.html). Else the amount will be dispersed as part of the Employee's salary on a pro-rata basis.

 - Only Tax Impact (Cannot Claim But Part of Taxable Income): Such components are those which the company has already paid to the Employee in cash or by some other means, for example a car purchased for the Employee's use. The Employee cannot claim but is liable to pay tax. The amount allocated for this component will be considered while calculating the taxable income of the Employee.

 - Create Separate Payment Entry Against Benefit Claim: Some of the flexible benefits may be legally required to be paid via separate vouchers. If you enable this, while posting the bank entry the amount paid for such components will be posted as a separate entry for each Employee.

	<img class="screenshot" alt="Flexible Salary Component"
	src="{{docs_base_url}}/assets/img/human-resources/salary-component-1.png">

	> Note: Normal Tax calculation does not include Flexible Benefits as in most cases these are exempted from Tax. To tax these components anytime before that last payroll, use "Deduct Tax For Unclaimed Employee Benefits" in Payroll Entry / Salary Slip while processing the Salary.

#### Deduction

<img class="screenshot" alt="Salary Component Deduction"
	src="{{docs_base_url}}/assets/img/human-resources/salary-component-2.png">

* Variable Based On Taxable Salary: If you enable this, the component will be considered as the standard Tax deduction component. Tax will be calculated based on the Tax slabs configured in Payroll Period on all the total taxable salary.

## Salary Structure

Salary Structure represents how Salaries are structured and calculated based on Earnings and Deductions. Salary structures are used to help organizations:

1. Maintain pay levels that are competitive with the external labor market,
2. Maintain internal pay relationships among jobs,
3. Recognize and reward differences in the level of responsibility, skill, and performance, and manage pay expenditures.

Usual components of a salary structure (in India) include:

* Basic Salary: It is the taxable base income and generally not more than 40% of CTC.

* House Rent Allowance: The HRA constitutes 40 to 50% of the basic salary.

* Special Allowances: Makes up for the remainder part of the salary, mostly smaller than the basic salary which is completely taxable.

* Leave Travel Allowance: The non-taxable amount paid by the employer to the employee for vacation/trips with family within India.

* Gratuity: It is basically a lump sum amount paid by the employer when the employee resigns from the organization or retires.

* PF: Fund collected during emergency or old age. 12% of the basic salary is automatically deducted and goes to the employee provident fund.

* Medical Allowance: The employer pays the employee for the medical expenditures incurred. It is tax-free up to Rs.15,000.

* Bonus: Taxable part of the CTC, usually a once a year lump sum amount, given to the employee based on the individual’s as well as the organizational performance for the year.

* Employee Stock Options: ESOPS are Free/discounted shares given by the company to the employees. This is done to primarily increase employee retention.

<img class="screenshot" alt="Submitted Salary Structure" src="{{docs_base_url}}/assets/img/human-resources/salary-structure.png">
A submitted Salary Structure

### Creating a New Salary Structure
To create a new Salary Structure go to:

> Human Resources > Payroll Setup > Salary Structure > New Salary Structure

In the new Salary Structure,

1. Name the salary Structure and set the company, letterhead for Salary Slip printing and frequency of payroll etc.
2. Set the starting date from which this is valid (Note: There can only be one Salary Structure that can be “Active” for an Employee during any period).
3. Configure Leave Encashment Amount per Day which will be the amount payable to Employees on Leave Encashment requests.
4. Max Benefits amount is the maximum amount eligible as Flexible Components to employees.

#### Salary Slip Based on Timesheet

Salary Slip based on Timesheet is applicable if you have timesheet based payroll system

1. Check "Salary Slip Based on Timesheet"
2. Select the salary component and enter Hour Rate (Note: This salary component gets added to earnings in Salary Slip)

<img class="screenshot" alt="Salary Slip based on Timesheet" src="{{docs_base_url}}/assets/img/human-resources/salary-timesheet.png">

#### Earnings and Deductions in Salary Structure

In the “Earnings” and “Deductions” tables, you can select the earnings and deductions components The condition and formula configured in Salary Component will be copied by default, but you may change this if required. You may also want to select the Base component in the Earnings table. Note that the amount eligible for each employee should be configured in Salary Structure Assignment.

If the condition and formula for any of the earnings or deductions are not configured in Salary Component, you can calculate the values of Salary Components based on,

#### Condition and Formula

<img class="screenshot" alt="Condition and Formula" src="{{docs_base_url}}/assets/img/human-resources/condition-formula.png">

#### Condition and Amount

<img class="screenshot" alt="Condition and Amount" src="{{docs_base_url}}/assets/img/human-resources/condition-amount.png">


In conditions and formulas,

  * Use field "base" for using base salary of the Employee
  * Use Salary Component abbreviations. For example: BS for Basic Salary
  * Use field name for employee details. For example: Employment Type for employment_type

#### Account Details

<img class="screenshot" alt="Salary Structure Account" src="{{docs_base_url}}/assets/img/human-resources/salary-structure-account.png">  

  * Select Mode of Payment and Payment Account for the Salary Slips which will be generated using this Salary Structure

Finally, *Save* the Salary Structure.

### Leave Without Pay (LWP)

Leave Without Pay (LWP) happens when an Employee runs out of allocated leaves or takes a leave without an approval (via Leave Application). If you want ERPNext to automatically deduct salary in case of LWP, then you must check on
the “Apply LWP” column in the Earning Type and Deduction Type masters. The amount of pay cut is the proportion of LWP days divided by the total working days for the month (based on the Holiday List).

If you don’t want ERPNext to manage LWP, leave the LWP unchecked in all of the Earning Types and Deduction Types.

## Salary Structure Assignment

Salary Structure Assignment allows you to assign salary structure and specify the base pay eligible for each employee. It is important that you set the base salary for each assignment as this will be the base salary used for calculations as per the Salary Structure.

To create a new Salary Structure Assignment go to:

> Human Resources > Payroll > Salary Structure Assignment > New Salary Structure Assignment

<img class="screenshot" alt="Salary Structure Assignment" src="{{docs_base_url}}/assets/img/human-resources/salary-structure-assignment.png">  

* * *

#Processing Payroll
You can either bulk process payroll for Employees under a department, branch or designation or process payroll individually by creating Salary Slips for each employee.

## Payroll Processing Using Payroll Entry
You can also create salary slip for multiple employees using Payroll Entry:

> Human Resources > Payroll > Payroll Entry > New Payroll Entry

#### Payroll Entry

<img class="screenshot" alt="Payroll Entry" src="{{docs_base_url}}/assets/img/human-resources/payroll-entry.png">

In Payroll Entry,

1. Select the Company for which you want to create the Salary Slips. You can also select the other fields like Branch, Department, Designation or Project to be more specific.
2. Check _Salary Slip based on Timesheet_ if you want to process timesheet based Salary Slips.
3. Select the Posting Date and the frequency of payroll which you want to create the Salary Slips.
4. Click on "Get Employee Details" to get a list of Employees for which the Salary Slips will be created based on the selected criteria.
5. Enter the Start and End dates for the payroll period.
6. You can check _Deduct Tax For Unclaimed Employee Benefits_ if you want to deduct taxes for all benefits (Salary Components which are _Is Flexible Benefit_) paid to employees till the current payroll
7. Similarly, _Deduct Tax For Unsubmitted Tax Exemption Proof_ allows you to deduct taxes for the earnings which were exempted in the previous payrolls as declared in [Employee Tax Exemption Declaration](/docs/user/manual/en/human-resources/payroll/employee-tax-exemption-declaration.html) but the Employee has not submitted sufficient proof [Employee Tax Exemption Proof Submission](/docs/user/manual/en/human-resources/payroll/employee-tax-exemption-proof-submission.html)
8. Select the Cost Center and Payment Account.
9. Save the form and Submit it to create Salary Slip records for each active Employee for the time period selected. If the Salary Slips are already created, the system will not create any more Salary Slips. You can also just save the form as Draft and create the Salary Slips later.

<img class="screenshot" alt="Submitted Payroll Entry" src="/docs/assets/img/human-resources/created-payroll.png">

Once all Salary Slips are created, you can use _View Salary Slips_ to verify if they are created correctly or edit it if you want to deduct Leave Without Pay (LWP).

After checking, you can "Submit" them all together by clicking on "Submit Salary Slip".

>Note: Submitting Salary Slips will also book the default Payroll Payable account to record the accrual of salary.

#### Booking Salaries in Accounts

The final step is to book the Salaries in your Accounts.

Salaries in businesses are usually dealt with extreme privacy. In most cases, the companies issues a single payment to the bank combining all salaries and the bank distributes the salaries to each employee’s salary account. This way there is only one payment entry in the company’s books of accounts and anyone with access to the company’s accounts will not have access to the individual salaries.

The salary payment entry is a Journal Entry that debits the total of the earning type salary component and credits the total of deduction type salary component of all Employees to the default account set at Salary Component level for each component.

To generate your salary payment voucher from Payroll Entry, click on -
> Make > Bank Entry

<img class="screenshot" alt="Payroll Make Entry" src="/docs/assets/img/human-resources/payroll-make-bank-entry.png">

Payroll Entry will route you to Journal Entry with relevant filters to view the draft Journal Vouchers created. You shall set reference number and date for the transactions and Submit the Journal Entries.

>Note: For Salary Components which are Flexible Benefits and has _Create Separate Payment Entry Against Benefit Claim_ checked, ERPNext will book separate draft Journal Entries.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-journal-entry.png">

## Creating Salary Slips Manually

Once the Salary Structure is created and assigned to employees via Salary Structure Assignment, you can make a Salary Slip individually. Go to:

> Human Resources > Payroll > Salary Slip > New Salary Slip

#### Salary Slip

<img class="screenshot" alt="Salary Slip" src="{{docs_base_url}}/assets/img/human-resources/salary-slip.png">

{next}
