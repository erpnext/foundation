<!-- add-breadcrumbs -->
# Patient Encounter
ERPNext Healthcare allows you to record every encounter with patients through the Patient Encounter document. You can create a Patient Encounter based on a previously booked Appointment or directly by creating a new Patient Encounter

`Healthcare > Patient Care > Patient Encounter`

You can also create and record encounter details for a patient from Patient Appointment, the Patient Encounter or the Patient master documents by using the `Create > Patient Encounter` button. If creating a Patient Encounter manually, you can search for a Patient by name, email phone number etc. In the Patient Encounter document, all Patient related details will automatically be populated enabling easy access to relevant data. The Patient Details section will list the latest Vital Signs record of the patient and other information captured in the Patient screen. You can also look up the Patient Health History by using the `View > Medical Record` button.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_1.png">

### Assessment
Encounter Impression section allows you to select (or create new) Complaints and your Diagnosis based on the presented complaints. You can opt to include the captured data in Patient Encounter print by selecting the "In Print" flag

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_2.png">

### Order Entry
You can prescribe medicines in the Drug Prescription section by selecting the drug codes (Stock Item) and appropriate dosages. If you are not managing Stock and Items are not configured, you can simply enter the Medicine name and strength in the Strength field which will printed.

Ordering a laboratory investigation is similar and if you have Lab Tests configured, you can select from the list. Or key in the Lab Test name to be printed as part of the Prescription. You can also order a Clinical Procedure to performed in a similar fashion.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_3.png">

The Pharmacy (Sales / Accounts) User can fetch medication and investigation orders from Patient Encounter using the _Get items from > Prescription_ made available in the sales Invoice. Lab Tests can be configured to be created automatically on Sales Invoice submission in [Healthcare Settings](/docs/user/manual/en/healthcare/setup/healthcare_settings.html). Procedure Orders can be fetched using the `Get Prescribed Procedures` while booking the Appointment for the procedure. These will then be available for billing via the _Get items from > Healthcare Services_.

### Medical Coding
You can also attach one or more Medical Codes to designate the Diagnosis in the Medical Coding Section. You will have to select the Medical Code Standard you wish to encode the diagnosis and then select the Code by searching the Code itself or the Code Description.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_4.png">

{next}
