<!-- add-breadcrumbs -->
# Patient Appointment
ERPNext Healthcare allows you to book Patient appointments for any date and alert patients via Email or SMS. You can easily organize appointments for each Practitioner based on their availability schedules.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_calendar.png">

You can create a Patient Appointment from,

`Healthcare > Appointment Booking > Patient Appointment`

You can book appointments for a registered Patient by searching for Patient by Patient ID, Name, Email or Mobile number. It is also possible to register a new Patient from the Appointment screen itself by selecting `Create a new Patient` in the Patient field.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_1.png">

If you need to book appointments for procedures select a Procedure or use `Get Ordered Procedures` to select from a list of Procedures that are ordered for the selected Patient.

`Check Availability` button will allow you to select the Practitioner, Appointment Type and Date for which the appointment is to be booked. On selecting the details, all the available time slots for the practitioner be displayed with status indicators for the selected date. You can select a time slot and `Book` an Appointment for the Patient.

Note that, selecting the `Appointment Type` will automatically set the duration of the appointment as configured in the Appointment Type. This will allow you to override the duration of appointments set by the Practitioner Schedule and the time slots will adjust to the next available time automatically. To disable this behavior, you can enable `Always Use Slot Duration as Appointment Duration` in the Practitioner master. This will always set the slot duration configured in the Practitioner Schedule as the Appointment duration.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_2.png">

> Note: Appointment booking considers any 'approved' Leave Applications for the Practitioner (Employee linked in the master) and does not allow bookings on such days.

Once booked, the scheduled time of the Appointment and the Service Unit as per the Practitioner and appropriate Status will be set in the document. The More Info section of Patient Appointment, user can add *Notes* and also select a *Referring Practitioner* to help you track referrals.

Optionally, you can configure ERPNext to automatically send an SMS alert to the Patient about the booking confirmation -

`Healthcare > Healthcare Settings > Out Patient SMS Alerts`

### Invoicing
ERPNext Healthcare allows you to automatically create an Invoice as you book an Appointment. To enable this option, you can turn on this option

`Healthcare > Healthcare Settings > Invoice Appointments Automatically`

If enabled, the Patient Appointment will prompt you to select the *Mode of Payment* and enter the *Amount* collected as the Consultation Charge.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_3.png">

>Note: If you have not enabled this, you can always use *Get Items From > Healthcare Services* in Sales Invoice

### Actions
  * Vital Signs: `Create > Vital Signs` button will take you to the new Vital Signs screen to record the vitals of the Patient.

  * Encounter: From the Appointment screen you can directly create and record the `Patient Encounter` to record the details of the visit.

  * View `Patient Medical History`.

> Note: User should have appropriate privileges (User Role) to view the buttons

Booking appointments via the ERPNext portal by patients directly checking a Practitioner's availability is not currently available.

{next}
