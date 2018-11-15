<!-- add-breadcrumbs -->
# Patient Appointment
ERPNext Healthcare allows you to book Patient appointments for any date and if configured, send them alerts via Email or SMS.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_calendar.png">

You can create a Patient Appointment from
`Healthcare > Appointment Booking > Patient Appointment`

You can book appointments for a registered Patient by searching and selecting the Patient field. The Patient Appointment form allows you to search the Patient by Patient ID, Name, Email or Mobile number. You can also register a new Patient from the Appointment screen by selecting `Create a new Patient` in the Patient field.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_1.png">

If you have a front desk executive to manage your appointments, you can configure a user role to have access to Patient Appointment so that she can do the bookings by selecting the Physician whom the Patient wish to consult and the date for booking.

Note that, selecting the `Appointment Type` will automatically set the duration of the appointment as configured. This will allow you to override the duration of appointments set by the Practitioner Schedule and the time slots will adjust to the next available time automatically.

`Check Availability` button will pop up all the available time slots with status indicators for the selected date. She can select a time slot and `Book` the Appointment for the Patient.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_2.png">

> Note: Appointment booking considers any 'approved' Leave Applications for the Practitioner (Employee linked in the master) are found

Once booked, the scheduled time of the Appointment and the Service Unit as per the Practitioner and appropriate Status will be set in the document. The More Info section of Patient Appointment, user can add *Notes* and also select a *Referring Practitioner* to help you track manage referrals.

Optionally, you can configure ERPNext to automatically send an SMS alert to the Patient about the booking confirmation -

`Healthcare > Healthcare Settings > Out Patient SMS Alerts`

### Invoicing
ERPNext Healthcare allows you to automatically create Invoice as you book an Appointment. To enable this option, you can turn on this option

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
