# Human Resource Management Enhancements

So far the Human Resource Management module in ERPNext was very basic. From our interactions we realized that most larger companies that implemented ERPNext had their own HR implementations. This has changed with Version 11. ERPNext has now a much deeper Human Resource management module and this is by far the biggest improvement in this version.

### Department Hierarchy

With the Department now a tree, you can map your company's organization structure as a tree.

<img class='screenshot' alt='Department Tree' src="/docs/assets/img/human-resources/department-tree.png">

[Learn more about Departments](https://erpnext.org/docs/user/manual/en/human-resources/setup/department)

---

## Leave Management

[Learn more about how Leave Management works](https://erpnext.org/docs/user/manual/en/human-resources/leave-management)

### Leave Period

There is now a Leave Period against which leaves will be granted (allocated). The process of allocation will be done in basis of Leave Policy and these can be directly attached to Employees or their Grades.

<img class="screenshot" alt="Leave Period"
	src="/docs/assets/img/human-resources/leave-period-1.png">

### New Leave Types

Several new leave types have been introduced:

- Optional Leave: Pick leaves from a set of optional holidays (for example religious holidays).
- Earned Leave: Automatically allocate leave based on time served.
- Parental Leave: Long term paternity or maternity leaves.

### Leave Encashment

Employees can now apply for encashment of unused leaves based on the company policy for each leave type and maximum number of encashable leaves.

### Compensatory Leave

If an Employee has worked on a holiday, she can apply for a Compensatory Leave that will allow her to take off on another day.

### Attendance Request

Request for Attendance in case the Employee has worked from home or has been out of office on field duty.


---

## Enhanced Payroll

Along with Leave Management, Payroll has been greately enhanced with tons of new features.

[Learn how Payroll works in EPRNext](https://erpnext.org/docs/user/manual/en/human-resources/payroll)

### New Salary Structure

Salary Structure Assignment is now moved out of Salary Structure so that you can assign a single structure to a large number of Employees

### Additional Salary

Declare Ad-hoc salary components that can be used in case of Incentives or one time bonus or deductions.

### Payroll Period

Salary processing now happens in pre-defined periods (years) where the dates for each month's payroll and freezing of other documents is defined.

### Employee Benefits

Employees can now apply for flexible benefits (like medical, dental, internet etc) offered by the company that form and also submit claims against those benefits.

### Employee Tax Exemptions

Employees can apply for Tax Exemptions based on the categories defined by the government and the system will automatically adjust the tax deducted based on the exemptions applied and the proof submitted.

### Auto Calculation of Tax Deduction

You can define various rates of tax deducation based on thresholds that will be automatically calculated and deducted from the month's salary.

### Enhanced Salary Processing

Payroll run has been enhanced to process a large number of Employees in a go by pushing processing to background jobs via queues.

---

## Employee Lifecycle

In Version 11, you can easily track the lifecycle of Employees right from the time they join the company to the time they leave. There are numberous processes in onboarding, transfer and separation. ERPNext helps you manage these processes by integrating with the Projects module.

[Learn more about Employee Lifecycle](https://erpnext.org/docs/user/manual/en/human-resources/employee_lifecycle)

<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/2zbMW1YKtWo" allowfullscreen></iframe>
</div>

### Employee Onboarding

Prepare a template for Employee onboarding like signing of the contract, NDA, issuing ID card, email id etc and make separate tasks that can be assigned to individuals or Roles.

### Employee Separation

Just like Onboarding, separation helps you prepare a checklist of all the tasks that need to be completed when an Employee leaves the organisation

### Employee Transfer and Promotion

Keep a track of transfers of employees withing departments or group companies and also their promotions.

---

### Shift Planning

ERPNext Version 11 also helps you manage multiple shifts by planning shifts and assigning employees to shifts and also managing requests by employees for various shifts.

 - Shift Type: Manage list of Shifts and their timings and start and end dates and number of openings.
 - Shift Assignment: Assign Employees to Shift Types to track how many Employees are assigned.
 - Shift Request: Manage the process by which Employees can apply for Shifts

[Learn more about Shift Management](https://erpnext.org/docs/user/manual/en/human-resources/shift-management)

---

### Staffing Plan

You can create Staffing Plans and limit the number of openings for each position for each period. When a staffing plan is created, ERPNext will ensure that the number of Job Openings does not cross the budget number of positions.

[Learn more about Staffing Plan](https://erpnext.org/docs/user/manual/en/human-resources/setup/staffing-plan.html)
