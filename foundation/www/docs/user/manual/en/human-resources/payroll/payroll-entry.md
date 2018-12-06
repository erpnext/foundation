<!-- add-breadcrumbs -->
# Payroll Entry

Payroll Entry enables bulk processing of payroll for employees company wide or employees of a particular branch, department or designation. Payroll Entry helps you create Salary Slips _in bulk_ for selected employees, submit the created Salary Slips at once, submit salary accrual entry and finally post bank entry for recording the salary payment, automating almost every step involved in payroll processing. Here's how you can use Payroll Entry to simplify your payroll processing.

> Human Resources > Payroll > Payroll Entry > New Payroll Entry

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-entry.png">

> Note: Read [Payroll Setup](/docs/user/manual/en/human-resources/payroll/payroll-setup.html) to know how you can configure Payroll to take the full advantage of ERPNext Human Resources.

In Payroll Entry,

1. Select the Company for which you want to create the Salary Slips. You can also select the other fields like Branch, Department, Designation or Project to be more specific.
2. Check _Salary Slip based on Timesheet_ if you want to process timesheet based Salary Slips.
3. Select the Posting Date and the frequency of payroll which you want to create the Salary Slips.
4. Click on _Get Employee Details_ to get a list of Employees for which the Salary Slips will be created based on the selected criteria.
5. Enter the Start and End dates for the payroll period.
6. You can check _Deduct Tax For Unclaimed Employee Benefits_ if you want to deduct taxes for all benefits (Salary Components which are _Is Flexible Benefit_) paid to employees till the current payroll
7. Similarly, _Deduct Tax For Unsubmitted Tax Exemption Proof_ allows you to deduct taxes for the earnings which were exempted in the previous payrolls as declared in [Employee Tax Exemption Declaration](/docs/user/manual/en/human-resources/payroll/employee-tax-exemption-declaration.html) but the Employee has not submitted sufficient proof [Employee Tax Exemption Proof Submission](/docs/user/manual/en/human-resources/payroll/employee-tax-exemption-proof-submission.html)
8. Select the Cost Center and Payment Account.
9. Save the form and Submit it to create Salary Slip records for each active Employee for the time period selected. If the Salary Slips are already created, the system will not create any more Salary Slips. You can also just save the form as Draft and create the Salary Slips later.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/created-payroll.png">

Once all Salary Slips are created, you can use _View Salary Slips_ to verify if they are created correctly or edit it if you want to deduct Leave Without Pay (LWP).

### Booking Salary Accrual and Payment

After verifying the Salary Slips, you can _Submit_ them all together by clicking on `Submit Salary Slip`. This will also book the default Payroll Payable account against respective Expense Heads (as configured in Salary Components) to record the accrual of salary to employees.

> Note: Submitting Salary Slips one by one manually will _not_ create the Journal Entry to record salary accrual.

The final step is to book the Salary Payment.

Salaries in businesses are usually dealt with extreme privacy. In most cases, the companies issues a single payment to the bank combining all salaries and the bank distributes the salaries to each employee’s salary account. This way there is only one payment entry in the company’s books of accounts and anyone with access to the company’s accounts will not have access to the individual salaries.

The salary payment entry is a Journal Entry that debits the total of the earning type salary component and credits the total of deduction type salary component of all Employees to the default account set at Salary Component level for each component.

To generate your salary payment voucher from Payroll Entry, click on -
> Make > Bank Entry

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-make-bank-entry.png">

Payroll Entry will route you to Journal Entry with relevant filters to view the draft Journal Vouchers created. You shall set reference number and date for the transactions and Submit the Journal Entries.

>Note: For Salary Components which are Flexible Benefits and has _Create Separate Payment Entry Against Benefit Claim_ checked, ERPNext will book separate draft Journal Entries.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-journal-entry.png">

{next}
