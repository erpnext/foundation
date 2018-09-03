<!-- add-breadcrumbs -->
# Human Resource Setup

The HR module has a setup process where you create the masters for all the major activities.

### Organization Setup

To setup your Employee master you must first create:

* Employment Type (like Permanent, Temp, Contractor, Intern etc).
* Branch (if there are multiple offices).
* Department (if any, like Accounting, Sales etc).
* Designation (CEO, Sales Manager etc).
* Grade (A, B, C etc, usually based on seniority).

Check [Setup](/docs/user/manual/en/human-resources/setup/) for more details on each of masters, global _HR Settings_ and other configurations.

### Leave Setup

To setup Leaves, create:

* Leave Type (like Sick Leave, Travel Leave etc)
* Holiday List (list of annual holidays for the year - these days will not be considered in Leave Applications)
* Leave Policy to effectively track and manage Employee leaves across the company

You can read [Leaves - Overview](/docs/user/manual/en/human-resources/leave.html) for a detailed description about how you can configure and manage Leaves.

### Payroll (Salary) Setup

In ERPNext, salaries have two types of components, earnings (basic salary, expenses paid by the company, like telephone bill, travel allowance etc) and deductions (amounts deducted for taxes, social security etc). You can create and assign salary structures to employees and ERPNext simplifies most of the payroll processing for you.

Read more about setting up your payroll and how ERPNext simplifies payroll processing in [Salary and Payroll](/docs/user/manual/en/human-resources/salary-and-payroll.html).

If you intend to configure ERPNext to calculate Income Tax deductions automatically based on multiple Salary Slabs, [Setting Up Income Tax Deduction]((/docs/user/manual/en/human-resources/setting-up-tax.html)) will help you understand how you can set this up properly.

### Recruitment

It is important for enterprises to plan their manpower recruitment for future periods. ERPNext allows you to define recruitment plans at group company level. Subsidiary companies can create and publish job openings based on the group company plans, making it easy to manage your hiring process. To understand how you can set this up, check [Staffing Plan](/docs/user/manual/en/human-resources/setup/staffing-plan.html)

If you have an active Staffing Plan, every time you create a new _Job Opening_ ERPNext will validate the open positions and current employment count with the Staffing Plan.

{next}
