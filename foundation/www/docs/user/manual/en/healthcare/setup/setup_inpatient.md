<!-- add-breadcrumbs -->
# Setting Up Inpatient Facility

ERPNext Healthcare allows you to easily configure your Inpatient facility, Admit, Discharge and Transfer (ADT) patients and Invoice the Patient for the care services rendered. Here's how you can setup this.

You can map your facility infrastructure (wards, beds etc.) in ERPNext using the [Healthcare Service Unit](/docs/user/manual/en/healthcare/healthcare_service_unit.html) document.

### Healthcare Service Unit Type
You can define the standard properties of `Healthcare Service Units` you create using the Healthcare Service Unit Type. By configuring various types of the service unit in your facility with respective rates and other properties, you can easily create multiple Healthcare Service Units by merely selecting the type. You can configure various types by going to,

`Healthcare > Setup > Healthcare Service Unit Type > New Healthcare Service Unit Type`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_service_unit_type.png">

ERPNext automatically creates an Item with the details you provide here, for the billing to function.

You can also create Healthcare Service Units to map consulting rooms and other areas where appointment scheduling is possible by checking the `Allow Appointments` option. Such service units are not linked to Item master as billing will make use of the Item selected in the [Healthcare Practitioner](/docs/user/manual/en/healthcare/healthcare_practitioner.html) master or the ones configured in [Healthcare Settings](/docs/user/manual/en/healthcare/setup/healthcare_settings.html)

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_service_unit_type_1.png">

Note that turning on the `Allow Overlap` will allow overlapping appointments for the Healthcare Practitioner available at service unit. This will be handy when you create service units where multiple Patients can be treated at the same time, for instance a yoga center or a physiotherapy room.

{next}
