# Employee Onboarding and Separation

In the process of hiring or relieving an Employee, there are set of standard activities which need to be executed. This feature helps you maintain the master of these activities, and create the set of Task at the time of each Employee hiring or relieving.

Use Case: Let's assume that following are the activities which need to be performed as soon as a job applicant is approved to be hired.

- Perform a legal and professional background check
- Create an Employee master
- Create an Email Account
- Create an identity card
- Allocate leaves

Same way, you can have a different set of activities to be performed when relieving an Employee, like:

- Disable access from the system
- Collect assets from the relieving Employee, if any allocated
- Collect ID card
- Update employee master
- Perform full and final payment process in the payroll

In ERPNext, these standard activities can be tracked in the Employee Onboarding and Separation Template.

### Employee Onboarding Template

> HR > Employee Lifecycle > Employee Onboarding Template

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding-template.png">

You can notice that for each Activity, you can also mention the User or Role, or one of it, to whom this activity will be assigned.

You can also maintain separate master for the Employee Separation Template, based on Department, Designation, and Grade.

### Employee Onboarding

Employee Onboarding is created for a Job Application, who is approved for the hiring.

You can select an applicant from Job Applicant master, and fetch activities from Employee Onboarding master.

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding.png">

### Tasks and Assignments

On submission on Employee Onboarding / Separation, a Project will be created. Within the Project, a Tasks will also be created for each Activity. Again, each Task will be allocated, based on the User or Role selected for that Activity.

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding-tasks.gif">

### Employee Creation

Based on the progress on the Tasks, progress can be updated in the Employee Onboarding and Separation process.

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding-employee.png">

### Video Help (Webinar Recording)

<div class="embed-container">
  <iframe src="https://www.youtube.com/embed/2zbMW1YKtWo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
  </iframe>
</div>

{next}
