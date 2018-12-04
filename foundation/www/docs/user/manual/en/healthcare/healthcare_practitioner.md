<!-- add-breadcrumbs -->
# Healthcare Practitioner
ERPNext Healthcare allows you to create multiple practitioners and link to a User with appropriate Roles. You can create a Practitioner by going to,

`Healthcare > Masters > Healthcare Practitioner`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_1.png">

To enable access rights to ERPNext, you may want to attach a User with `Physician` role for the practitioner. Most Patient related documents like the Encounter, Vitals etc. offer only limited access to users with other roles. You should ideally link the User to Employee document for the user to access Human Resources module so as to utilize the many features like Leaves, Payroll etc.

>Note: Selecting the Employee field will fetch in all relevant fields as configured in the Employee document to help you easily setup the Practitioner

### Availability and Charges
You can select multiple schedules for each practitioner and optionally a service unit at which the practitioner will be available.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_2.png">

You can optionally set an `Appointment Type` for each schedule to ensure that only those types of appointments can be booked for the time slots available as per the schedule. Leaving this field blank will allow appointments of any type. Also, enabling `Always Use Slot Duration as Appointment Duration` will override the default behavior of setting appointment duration to the duration configured in the Appointment Type.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_4.png">

You can set the consultation charges which are applicable to the practitioner. If required, you can also select an Income Account for a Physician to book all Consultation charges into separate accounts.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_3.png">

### Referring Physicians
You may also want to manage a list of Doctors who refers Patients to your facility. You can manage such data in the Healthcare Practitioner document itself by leaving out the Employee and User links.

{next}
