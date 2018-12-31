<!-- add-breadcrumbs -->
# Inpatient Record
ERPNext Healthcare captures the all details about a Patient Admission using this document.

Inpatient Record is automatically created when a practitioner order an admission, you can find the document by going to,

`Healthcare > Patient Care > Inpatient Record`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/ip_admission_order.png">

Healthcare Practitioner can order a patient admission from the Patient Encounter document using the `Schedule Admission` button. This will automatically create an Inpatient Record for the Patient in _Admission Scheduled_ status. The IP admission officer can then allot a vacant room to the Patient as recommended by the referring practitioner in the admission order.

All details as provided by the Practitioner in the admission order will be made available in the Inpatient record, and the dashboard will link to all other documents which are created in the admission period, you also allowed to create new documents from the dashboard.

> Note: Field Level permissions are by default applied so that Diagnosis information, Admission Instructions and other details are only visible to users with roles Physician and Nursing User enabled

Patient ADT is also managed within the Inpatient Record as described in the [Inpatient ADT](/docs/user/manual/en/healthcare/inpatient_adt.html) section.

{next}
