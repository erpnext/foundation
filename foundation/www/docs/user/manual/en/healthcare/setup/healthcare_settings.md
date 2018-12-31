<!-- add-breadcrumbs -->
# Healthcare Settings

Most of the global settings for the Healthcare module can be done via the Healthcare Settings page.

`Healthcare > Setup > Healthcare Settings`

> Note: Ensure that you have `Healthcare Administrator` role enabled for your User to access this page.

### Outpatient Settings
<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_settings_1.png">

* **Patient Auto Name**: By default Patient document uses naming series for naming but you can also opt to change this to Patient Name if required.

* **Link Patient with Customer**: The `Manage Customer` option will enable the system to create and link a Customer whenever a new Patient is created. This Customer is used while booking all transactions. If you do not enable this, you wont be able to ling the Patient with a Customer while invoicing any of the services.

* **Default Medical Code Standard**: ERPNext Healthcare allows you to use multiple Medical Code Standards - here, you can also select the default Medical Code Standard.

* **Collect Fee for Patient Registration**: If you enable this, all new Patients you create will be _Disabled_ by default and will be only be enabled after Invoicing the Registration Fee. To create Invoice and record the payment receipt, you can use the `Invoice Patient Registration` button in the Patient document. Also note that all ERPNext Healthcare documents, filters out Patient records that are disabled. You can also set the registration fee to be collected here.

* **Manage Appointment Invoice Automatically**: If you wish to automatically create an Invoice (with the selected Practitioner's consultation charges), you can enable this option. This feature is particularly helpful if your facility collects payment while booking an appointment. The Patient Appointment form will allow you to select the Payment Method and amount received.

* **Validity for Followups**: Many healthcare facilities do not charge for follow up consultations within a time period after the first visit. You can configure the number of free follow ups (_Patient Encounters in valid days_) allowed as well as the time period (_Valid number of days_) for free consultations here.

### Healthcare Service Items
<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_settings_2.png">

ERPNext Healthcare utilizes the Accounts module for billing Patients. You can configure default `Items` for billing consultation charges, procedure consumption items etc. here.

### SMS Alerts
<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_settings_3.png">

You can enable sending SMS alerts on Patient appointment Booking etc. and also configure SMS text in this section.

### Income Account and Receivable Account
<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_settings_4.png">

If you wish to override default accounts settings and set custom Income and receivable accounts, you can do so here.

### Laboratory Settings
<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_settings_5.png">

* **Create Lab Test(s) on Sales Invoice Submit**: If your facility creates Invoices and collect payments from Patients before performing the Lab Test, you can enable this option to create Lab tests automatically for all the Tests that are billed. If you have enabled `Manage Sample Collection` and has a _Sample_ configured in the Lab Test Template, a Sample Collection document will also be created.

* **Manage Sample Collection**: If this flag is enabled, every time you create a Lab Test, a Sample Collection document will be created.

* **Require Lab Test Approval**: Turning this on will restrict printing and emailing of Lab Tests only if the documents are in Approved status. You can use this flag to ensure that every Test result leaves your facility after verification.

* **Employee name and designation in print**: Enable the third option if you want the name and designation of the Employee associated with the User who submits the document to be printed in the Lab Test Report.

* **Laboratory SMS Alerts**: You can configure ERPNext Healthcare to alert Patients via SMS when the Lab Test result gets ready (Submit) and when you Email the result. You can configure the templates for the SMS as registered with your provider here.

{next}
