<!-- add-breadcrumbs -->
# Inpatient ADT

Managing ADT (Admission, Discharge, Transfer) in a busy Hospital is quite a tricky function and ERPNext Healthcare eases this to a great extent. In ERPNext Healthcare every patient admission is managed using the [Inpatient Record](/docs/user/manual/en/healthcare/inpatient_record.html) document.

## Admission
A Practitioner can order a patient for admission from the Patient Encounter screen using the `Order Admission`.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_order_admission.png">

As part of the Admission Order, the practitioner can provide necessary details as to which type of ward bed the Patient needs to be admitted to, and any other admission instructions for the staff.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_admission_order.png">

On ordering a patient for admission, ERPNext Healthcare creates an Inpatient Record for the Patient with all instructions provided by the Practitioner. Any prescribed medications and investigations or procedure orders as part of the ordered Encounter will be carried to the IP record.

> Note: Field Level permissions are by default applied so that Diagnosis information, Admission Instructions and other details are only visible to users with roles Physician and Nursing User enabled

Inpatient admission officer can see the Inpatient Record with status _Admission Scheduled_ and allot the Patient the Ward as per the availability. The `Admit` button in the Inpatient Record will allow the admission officer to select a ward bed for the Patient and process the admission.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_admit_patient.png">

Once a Service Unit is assigned for the patient, the Inpatient Record status will be updated to _Admitted_.

## Discharge

Similar to the Schedule Admission, Patient Encounters for admitted Patients will have the option to `Order Discharge` triggering the status of the impatient Record to _Discharge Scheduled_.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_order_discharge.png">

The Practitioner can order an inpatient's discharge through a Patient Encounter or the Inpatient Record. The Discharge Order allows Practitioner to select the contents of the `Discharge Notes` (or the Discharge Summary) which gets updated in the patient's Inpatient Record document. The practitioner can select the investigations, medications and procedures which were included in the Patient's treatment at the facility which are to be printed in the discharge notes and optionally add his comments to print.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_discharge_order.png">

The admission officer can print the Discharge Notes from the Inpatient Record and use the `Discharge` button to record patient's leave and marking the status to _Discharged_

>Note: ERPNext healthcare validates that all services availed during the stay at the facility are Invoiced to successfully complete the `Discharge` option. However, note that this validation _does not_ consider the Invoice status.

## Transfer
The Inpatient Record holds all data related to the Patient's stay at the facility including all the wards beds (Service Unit) utilized.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_transfer.png">

You can always transfer a patient from one Service Unit to another using the `Transfer` button. This will allow you to select the Service Unit to which the Patient is being transferred.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_transfer_patient.png">

{next}
