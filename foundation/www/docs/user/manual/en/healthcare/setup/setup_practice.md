<!-- add-breadcrumbs -->
# Setting Up Clinic / Practice

You can easily configure the masters for setting up ERPNext Healthcare for your practice. Below are a list of documents which helps you speed up data entry. Also read [Healthcare Settings](/docs/user/manual/en/healthcare/setup/healthcare_settings.html) for setting up the Healthcare module.

## Medical Department
To organize your clinic into departments, you can create multiple Medical Departments.

`Healthcare > Setup > Medical Department > New Medical Department`

## Appointment Type
You can create masters for various type of Appointments. Appointment Type allows you to predefine the duration of the appointment so that while selecting Appointment Type, the duration gets set in the Appointment automatically. This will allow you to override the duration of appointments set by the Practitioner Schedule and the time slots will adjust to the next available time automatically.

>Note: To disable this behavior, you can enable `Always Use Slot Duration as Appointment Duration` in the Practitioner master. This is will always set the slot duration configured in the Practitioner Schedule as the Appointment duration. 

You can also set a color for each Appointment Type which will help you identify the appointments of a particular type in the Calendar view.

`Healthcare > Setup > Appointment Type > New Appointment Type`

## Healthcare Service Unit Type
While setting up the schedule for Healthcare Practitioner, you can optionally select a [Healthcare Service Unit](/docs/user/manual/en/healthcare/Healthcare healthcare_service_unit.html) at which the Practitioner will be conducting his consultations. You should have `Allow Appointments` option checked for Healthcare Service Unit for booking appointments. You can also define the properties of service units in `Healthcare Service Unit Type`, also read about [Setting up Inpatient Facility](/docs/user/manual/en/healthcare/setup/setup_inpatient.html) for more details.

## Masters to Ease Data Input
ERPNext Healthcare allows you to configure some of the frequently used masters to make the data entry more easy.

#### Dosage Forms
Dosage Forms help you configure the form in which the medications are packaged, for example Capsules, Syrups etc.

`Healthcare > Setup > Complaints > New Dosage Form`

#### Route of Administration
The Route of Administration corresponds to the path by which the medication is induced into to Patient. For example, Oral, Intravenous etc.

`Healthcare > Setup > Complaints > New Route of Administration`

#### Prescription Dosage & Duration
You can configure different dosages to be used while prescribing medication to patients. You can name the Prescription dosage in anyway you want (for example, BID or I-0-I), and then set the strength of the drug and the times at which it should be administered.

`Healthcare > Setup > Prescription Dosage > New Prescription Dosage`

`Healthcare > Setup > Prescription Duration > New Prescription Duration`

#### Complaint and Diagnosis
To ease the data entry while recording the encounter impression, ERPNext Healthcare allows you to save every Complaint / Diagnosis data you enter, from the Patient Encounter screen itself. This way, the database keeps building a list of all complaints and diagnosis you entered. Later on, every time you start keying in, you will be able to select the previously entered word / sentence from the search field. You can also configure the masters manually by going to,

`Healthcare > Setup > Complaints > New Complaint`

`Healthcare > Setup > Diagnosis > New Diagnosis`

# Clinical Procedures Templates
ERPNext Healthcare allows you to configure templates with the various properties of Clinical Procedures to ease the Procedure creation process. You can create new Clinical Procedure Templates by going to,

`Healthcare > Setup > Clinical Procedure Template`

Templates allow you to manage the billable Item, rate etc. for a particular procedure. The `Consumables` section lets you set the consumable stock Items, default quantities etc. so that these items will preloaded in the Clinical Procedures created based on the template. This allows the performing practitioner can easily input the consumed quantities or add additional items which in reality has been consumed as part of the procedure.

If the `Invoice Consumables Separately` option is turned on, the charges for the consumable Items will be added to the Sales Invoice separately in addition to the `Billing Rate` of the procedure.

Note that you can also enable `Sample Collection` for a Clinical Procedure if applicable. Also, possible is to add multiple stages to the Template so that the Clinical Procedure can be tracked by the various stages as configured in the template.

{next}
