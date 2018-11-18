<!-- add-breadcrumbs -->
# Medical Code Standards
Medical Coding are, in many countries, required for regulatory compliance and many of the Medical Insurance companies manage eligibility and coverage based on Medical Code standards. ERPNext Healthcare offers support, however limited, to encode diagnosis and assessments recorded as part of Patient Encounter. You can also codify Clinical Procedures. You can configure Medical Code Standard and related Medical Codes - which usually can be easily done by data import as the code data tends to be quite large. You can create as many Medical Code Standards as you wish if you need to comply with multiple Coding Standards.

`Healthcare > Medical Coding > Medical Code Standard`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/medical_code_1.png">

Medical Code Standard document is used to name the Code Standard and act as a container for all the medical codes which are standardized under it. Medical Codes and descriptions can then be imported to the `Medical Code` document, after ensuring that you set the Medical Code Standard field appropriately.

In the Patient Encounter, practitioner can easily search and select appropriate ones from preconfigured Medical Codes.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_4.png">

It is also possible that you can link appropriate Medical Codes to `Appointment Type`, `Clinical Procedure Template`, `Lab Test Template` etc. to enable codification based on each of the services your facility offer. In many regions this is mandatory for processing patient _Insurance_ eligibility, claim processing and billing.

{next}
