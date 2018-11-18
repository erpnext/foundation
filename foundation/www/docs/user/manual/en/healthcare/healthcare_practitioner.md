<!-- add-breadcrumbs -->
# Healthcare Practitioner
ERPNext Healthcare allows you to create multiple practitioners and link to a User with appropriate Roles. You can create a Practitioner by going to,

`Healthcare > Masters > Healthcare Practitioner`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_1.png">

To enable access to ERPNext, you may want to attach a User with `Physician` role for the practitioner. Most Patient related documents like the Encounter, Vitals etc. offer only limited access to users with other roles. It's also possible that you can associate a Healthcare Practitioner to an Employee so as to utilize the many features like Leaves, Payroll etc.

>Note: You should ideally link the User to Employee document for the user to access Human Resources module.

### Availability and Charges
You can select multiple schedules for each practitioner and optionally a service unit at which the practitioner will be available. Also, you can set the consultation charges which are applicable to the practitioner. If required you can select an Income Account for a Physician to book all Consultation charges into separate accounts.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_2.png">

### Referring Physicians
You may also want to manage a list of Doctors who refers Patients to your facility. You can manage such data in the Healthcare Practitioner document itself by leaving out the User link.

{next}
