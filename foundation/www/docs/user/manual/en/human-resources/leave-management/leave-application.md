<!-- add-breadcrumbs -->
# Leave Application

If your company has a formal system where Employees have to apply for leaves
to be able to qualify as paid leaves, you can create Leave Application to
track approval and usage of leaves. The applying employee requires to select their Employee record, Leave
Type and the period for which the leave is taken.

> Human Resources > Leaves and Holiday > Leave Application > New Leave Application

<img class="screenshot" alt="Leave Application" src="{{docs_base_url}}/assets/img/human-resources/new-leave-application.png">

_Basic Workflow:_

- Employee applies for leave through Leave Application
- Approver gets notification via email, "Follow via Email" should be checked for this.
- Approver reviews Leave Application
- Approver approves/rejects Leave Application
- Employee gets notification on the status of his/her Leave Application

<img class="screenshot" alt="Leave Allocation Tool"
	src="{{docs_base_url}}/assets/img/human-resources/new-leave-application.png">

### Setting Leave Approver

* A leave approver is a user who can approve an leave application for an employee. Leave Approvers for each department can be configured in the [Department](/docs/user/manual/en/human-resources/setup/department.html) master.

> Tip : If you want all users to create their own Leave Applications, you can set
their “Employee ID” as a match rule in the Leave Application Permission
settings. See the earlier discussion on [Setting Up Permissions](/docs/user/manual/en/setting-up/users-and-permissions/user-permissions.html)
for more info.

_Notes:_

* Leave Application period must be within a single Leave Allocation period. In case, you are applying for leave across leave allocation period, you have to create two Leave Application records.
* Application period must be in the latest Allocation period.
* Employee can't apply for leave on the dates which are added in the "Leave Block List".

To understand how ERPNext allows you configure leaves for employees, check [Leaves - Setup](/docs/user/manual/en/human-resources/leave.html)

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/fc0p_AXebc8?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

{next}
