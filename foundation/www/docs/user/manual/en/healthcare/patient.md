<!-- add-breadcrumbs -->
# Patient

In ERPNext Healthcare, the Patient document corresponds any individual who is the recipient of healthcare services you provide. For every document ERPNext Healthcare, it is important to have a Patient associated with it. You can create a new Patient from

`Healthcare > Masters > Patient > New Patient`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/patient_1.png">

The Patient document holds most details that are required to identify and qualify a patient. You can enter as much information available while creating the Patient. All information in the patient document is presented on the Consultation screen for easy lookup and you can always update this information. Other data like observations, vital signs etc. are all linked to the Patient document. These could be recorded during patient encounters and will be available as part of the Patient Medical History.

The Patient document holds the Patient barcode and can be used in any the default print formats or any [Custom Print Formats](docs/user/manual/en/customize-erpnext/print-format.html) that you create for printing patient identification tags.

### Patient as a Customer

ERPNext, especially the Accounts module, makes use of **Customer** document for booking all transactions. So, you may want to associate every Patient to be associated with a Customer in ERPNext. By default, ERPNext Healthcare creates a Customer alongside a Patient and links to it - every transaction against a Patient is booked against the associated Customer. If, for some reason you do not intend to use the ERPNext Accounts module you can turn this behavior off by unchecking this flag

`Healthcare > Setup > Healthcare Settings > Manage Customer`

In many cases, you may want to associate multiple Patients to a single Customer against whom you want to book the transactions. For instance, a Veterinarian would require the care services provided to different pets of an individual invoiced against a single Customer.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/patient_2.png">

### Registration Fee
Many clinical facilities collect a registration fee during Registration. You can turn this feature on and set the registration fee amount by checking this flag

`Healthcare > Setup > Healthcare Settings > Collect Fee for Patient Registration`

If you have this option enabled, all new Patients you create will be in _Disabled_ mode by default and will only be enabled after Invoicing the Registration Fee. To create Invoice and record the payment receipt, you can use the `Invoice Patient Registration` button in the Patient document.

> Note: "Disabled" Patients are filtered out in all ERPNext Healthcare documents.

### Grant access to Patient Portal
ERPNext Healthcare allows you to create a portal user associated with a Patient by simply entering the user email id. A welcome email will be sent to the Patient email address to "Complete" registration.

### Actions
You can use the document links in the dashboard to traverse the linked document list with Patient filter applied, or use the + icons to create new records. Apart from this, the Patient document allows you to,

* Jump to the Patient's Health History, using `View > Medical Record` button.

* `Create > Vital Signs` to record the vitals of the Patient.

* Manually add data to a Patient's Medical Record, for instance a scanned copy of a Lab Test performed in an external Laboratory or a quick note on the Patient's condition, using `Create > Medical Record` button.

* Record the details of an encounter by using `Create > Patient Encounter` button

> Note: User should have appropriate privileges (User Role) to view the buttons

{next}
