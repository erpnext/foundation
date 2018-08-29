# Web Forms

Portal Views are viewed by external users, but the community that interacts with the organization, but is not a part of the organization. These are customers, suppliers, job applicants, or students, guardians etc. 

The standardized way these users can add or edit records is called "Web Forms".

You can add Web Forms to your ERPNext website that will allow addition/updation of new records for the external users.

You can add forms in your website for example, Contact Us, Inquiry, Complaint and other forms as per your requirement. Following is the help on adding new Web Form on ERPNext.

### Creating Web Form

To create a new **Web Form** go to:

> Website > Web Form > New

1. Set the Web Form title and url.
1. Select the **DocType** in which you want the user to store the records.
1. Select if you require the user to login, edit records, manage multiple records etc.
1. Add the fields you want in the record.

<img class="screenshot" alt="Web Form Entry" src="{{docs_base_url}}/assets/img/website/webform-1.png">

--

## Web Form View

### Form with Child Table

Once you create the web form, you can view it on the url and test it out! You can add child tables to your web forms, just like regular forms 

<img class="screenshot" alt="Web form Grid" src="{{docs_base_url}}/assets/img/website/grid-in-webform.png">

### Pagination

To help your users fill out long new forms, you can insert page breaks that will appear on new sections. This way the user can focus on only filling one section at a time. 

<img class="screenshot" alt="Web form paging" src="{{docs_base_url}}/assets/img/website/paging-in-webform.png">

### Payment Gateway Integration

You can now add a Payment Gateway to the web form, so that you can ask users to pay against a web form. A good example for this is a conference ticket :) 

<img class="screenshot" alt="Web form payment" src="{{docs_base_url}}/assets/img/website/payment-in-webform.png">

### Portal User

We have also introduced roles for Website users. Now the for each standard Role you can optionally disallow "Desk Access" to that user. 

In Portal Settings, you can set a role against each menu item so that only users with that role will be allowed to see that item. 

<img class="screenshot" alt="portal settings" src="{{docs_base_url}}/assets/img/website/portal-settings.png">

---

### Results

When website user submits the form, the data will be stored in the document/doctype for which web form is creaeted.

{next}