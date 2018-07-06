<!-- add-breadcrumbs -->
#Employee Tax Exemption Proof Submission
Employees are required to submit proofs for all the spendings they claim tax exemption for. This is usually done at the end of a Payroll Period, but employees can submit any number of proofs unlike Employee Tax Exemption Declaration.

To create a new Employee Tax Exemption Proof Submission, go to

> Human resources > Payroll > Employee Tax Exemption Proof Submission > New Employee Tax Exemption Proof Submission

<img class="screenshot" alt="Employee Tax Exemption Proof Submission"
	src="{{docs_base_url}}/assets/img/human-resources/employee-tax-exemption-proof-submission.png">

The the **Total Exemption Amount** will be exempted from annual taxable earnings of the employee while calculating the tax deductions in the last payroll.

> Note: Even if employees submit exemption proofs anytime during the payroll period, ERPNext will only consider this in the last payroll of the Payroll Period for adjusting the final taxes based on the proof submitted. If you need to adjust any additional tax collected or consider proof submission of employees anytime before the last payroll, while processing Payroll Entry (or in the Salary Slip of the employee) check the **Deduct Tax For Unsubmitted Tax Exemption Proof** option.

### Regional - India
For the current fiscal year, in India, House Rent Allowance (HRA) exemption from taxable earnings is the minimum of:
 * The actual amount allotted by the employer as the HRA.
 * Actual rent paid less 10% of the basic salary.
 * 50% of the basic salary, if the employee is staying in a metro city (40% for a non-metro city).

As part of the Employee Tax Exemption Proof Submission, employees shall also submit proof for HRA Exemption.

 > Note: HRA component shall be configured in Company for HRA exemption to work
