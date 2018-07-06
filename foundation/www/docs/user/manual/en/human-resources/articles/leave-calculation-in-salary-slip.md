# Leave Calculation In Salary Slip

There are two types of leave which user can apply for.

* Paid Leave (Sick Leave, Privilege Leave, Casual Leave etc.)
* Unpaid Leave

Paid Leave are firstly allocated by HR manager. As and when Employee creates Leave Application, leaves allocated to him/her are deducted. These leaves doesn't have impact on the employee's Salary Slip.

When Employee is out of paid leave, he create Leave Application for unpaid leave. The term used for unpaid leave in ERPNext is Leave Without Pay (LWP). These leaves does have impact on the Employee's Salary Slip.

<div class="well">Just marking Absent in the Attendance record do not have impact on salary calculation of an Employee, as that absenteeism could be because of paid leave. Hence creating Leave Application should be created incase of absenteeism. Let's consider a scenario to understand how leaves impact employees Salary Slip.

1. Setup Employee
1. Allocate him paid leaves
1. Create Salary Structure for that Employee. In the Earning and Deduction table, select which component of salary should be affected if Employee takes LWP.
1. Create Holiday List (if any), and link it with Employee master.

**Working Days:** Working Days in Salary Slip are calculated based on number of days selected above. If you don't wish to consider holiday in Working Days, then you should do following setting.

> Human Resource > Setup > HR Setting

Uncheck field "Include Holidays in Total No. of Working Days"

Holidays are counted based on Holiday List attached to the Employee's master.

**Leave Without Pay:** Leave Without Pay is updated based on Leave Application made for this Employee, in the month for which Salary Slip is created, and which has Leave Type as "Leave Without Pay".

Payment Days: Following is how Payment Days are calculated:

Payment Days = Working Days - Leave Without Pay

If you have LWP checked for the Salary Component, there will be reduction in Amount based on no. of LWP of an Employee for that month.