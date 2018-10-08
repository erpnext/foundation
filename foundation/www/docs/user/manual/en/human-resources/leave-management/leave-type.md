# Leave Type

> Human Resources > Leaves and Holiday > Leave Type > New Leave Type

Leave Type refers to types of leave allotted to an employee by a company. An employee can select a particular Leave Type while requesting for a leave. You can create any number of Leave Types based on your company’s
requirement.

<img class="screenshot" alt="New Leave Type"
	src="{{docs_base_url}}/assets/img/human-resources/new-leave-type.png">

* Max Leaves Allowed: This field allows you to set the maximum number of leaves of this Leave Type that Employees can apply within a Leave Period.

* Applicable After (Working Days): Employees who have worked with the company for this number of days are only allowed to apply for this Leave Type. Do note that any other leaves availed by the Employee after her joining date is also considered while calculating working days.

* Maximum Continuous Days Applicable: It refers to maximum number of days this particular Leave Type can be availed at a stretch. If an employee exceeds the maximum number of days under a particular Leave Type, his/her extended leave may be considered as ‘Leave Without Pay’ and this may affect his/her salary calculation.

* Is Carry Forward: If checked, the balance leave will be carried forwarded to the next allocation period.

* Is Leave Without Pay: This ensures that the Leave Type will be treated as leaves without pay and salary will get deducted for this Leave Type.

* Allow Negative Balance: If checked, system will always allow to approve leave application for the Leave Type, even if there is no leave balance.

* Include holidays within leaves as leaves: Check this option if you wish to count holidays within leaves as a ‘leave’. Such holidays will be deducted from the total number of leaves.

* Is Compensatory: Compensatory leaves are leaves granted for working overtime or on holidays, normally compensated as an encashable leave. You can check this option to mark the Leave Type as compensatory. An Employee can request for compensatory leaves using [Compensatory Leave Request](/docs/user/manual/en/human-resources/leaves_and_holiday/compensatory-leave-request.html) and on approval of such requests, Leave Allocation for this leave type is updated allowing her to apply for leaves of this type later on.

* Is Optional: Check this Optional Leaves are holidays which Employees can choose to avail from a list of holidays published by the company. The Holiday List for optional leaves can have any number of holidays but you can restrict the number of such leaves granted to an Employee in a Leave Period by setting the Max Days Leave Allowed field.

* Encashment: It is possible that Employees can receive cash from their Employer for unused leaves granted to them in a Leave Period. Not all Leave Types need to be encashable, so you should set "Allow Encashment" for Leave Types which are encashable. Leave encashment is allowed only in the last month of the Leave Period.

	<img class="screenshot" alt="Leave Encashment"
		src="{{docs_base_url}}/assets/img/human-resources/leave-type-encashment.png">

	You can set the _Encashment Threshold Days_ field so that the Employees wont be able to encash that many days. These days should be carry forwarded to the next Leave Period so that it can be either encashed or availed. You may also want to set the _Earning Component_ for use in Salary Slip while paying out the encashed amount to Employees as part of their Salary.

	>Note: On submitting a [Leave Encashment](/docs/user/manual/en/human-resources/leaves_and_holiday/leave-encashment.html) for an Employee, ERPNext automatically creates an [Additional Salary](/docs/user/manual/en/human-resources/payroll/additional-salary.html) which will get added to the Salary Slip of the Employee when processing the next payroll

* Earned Leave: Earned Leaves are leaves earned by an employee after working with the company for a certain amount of time. Checking "Is Earned Leave" will allot leaves pro rata by automatically updating Leave Allocation for leaves of this type at intervals set by _Earned Leave Frequency_. For example, if an employee earns 2 leaves of type Paid Leaves monthly, ERPNext automatically increments the Leave Allocation for Paid Leave at the end of every month by 2. The leave allotment process (background job) will only allot leaves considering the max leaves for the leave type, and will round to _Rounding_ for fractions.

	<img class="screenshot" alt="Earned Leave"
		src="{{docs_base_url}}/assets/img/human-resources/earned-leave.png">

### Default Leave Types
There are some pre-loaded Leave Types in the system, as below:

- Leave Without Pay: You can avail these leaves for different purposes, such as, extended medical issues, educational purpose or unavoidable personal reason. Employee does not get paid for such leaves.
- Privilege leave: These are like earned leaves which can be availed for the purpose of travel, family vacation and so on.
- Sick leave: You can avail these leaves if you are unwell.
- Compensatory off: These are compensatory leave allotted to employees for overtime work.
- Casual leave: You can avail this leave to take care of urgent and unseen matters.

{next}
