<!-- add-breadcrumbs -->
# Medical Code Standards
Medical Coding are in many countries required for regulatory compliance and many of the Medical Insurance companies manage eligibility and pricing based on Medical Code standards. ERPNext Healthcare offers support, however limited, to encode diagnosis and assessments recorded as part of Patient Encounter. This can be done if you configure the Medical Code Standard and related Medical Codes - this is easily done by data import as the code data tends to be quite large. You can create as many Medical Code Standards as you wish

`Healthcare > Masters > Medical Code Standard`

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/medical_code_1.png">

Medical Code Standard document is used to name the Code Standard and act as a container for all the medical codes which are standardized under it. Medical Codes and descriptions can then be imported to the Medical Code document, after ensuring that you set the Medical Code Standard field to the appropriate Standard name.

In the Patient Encounter, practitioner can easily search and select appropriate ones from preconfigured Medical Codes

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_4.png">

{next}
