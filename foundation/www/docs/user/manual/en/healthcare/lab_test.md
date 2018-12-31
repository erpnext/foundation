<!-- add-breadcrumbs -->
# Lab Test

ERPNext Healthcare allows you to manage a clinical laboratory efficiently by allowing you to enter Lab Tests and print or email test results, manage samples collected, create Invoice etc. ERPNext Healthcare comes pre-packed with some frequently ordered tests, you can reconfigure Lab Test Templates for each Test and its result format or create new ones as explained in [Setting Up Laboratory](/docs/user/manual/en/healthcare/setup/setup_laboratory.html)

Once you have all necessary Lab Test Templates configured, you can start creating Lab Tests by selecting a Test Template every time you create a Test. To create a new Lab Test

`Healthcare > Laboratory > Lab Test > New Lab Test`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/lab_test_1.png">

It is also possible to use the `Create Multiple` option to create all the lab tests ordered / billed for a patient.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/lab_test_3.png">

You can select the Patient and then the Encounter or Invoice from which you need to pull the tests without having to open the Encounter / Sales Invoice to look up the orders.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/lab_test_4.png">

If the Lab Test Template has sample collection enabled, creating Lab Test will automatically create Sample Collection records.

> Note: To create Sample Collection documents for every Lab Test, turn on "Manage Sample Collection" flag in Healthcare Settings *and* select Sample in the Lab Test Template

ERPNext Healthcare also allows creation of Lab Tests automatically when any lab tests are billed (via Sales Invoice). This along with other Laboratory configurations can be setup in [Healthcare Settings](/docs/user/manual/en/healthcare/setup/healthcare_settings.html)

As the results gets ready, you can enter the details of results in the Lab Test document. All presets, Normal Values etc. as configured in the Lab Test Template are made available Lab Test for easy data capture.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/lab_test_2.png">


In many Laboratories, approval of Lab Tests is a must before printing and submitting the document. ERPNext Healthcare allows you to create Users with Role "Lab Test Approver" for this. You will also have to enable this in

`Healthcare Settings > Laboratory Settings > Require Lab Test Approval`

This will ensure that emailing or printing of Lab Tests can only be done after Approval of the Lab Test by the Lab Test Approver.

{next}
