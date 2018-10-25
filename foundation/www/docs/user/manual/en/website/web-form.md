# Web Forms

> Context: There two types of in-built interfaces available in ERPNext. The 'Desk View' and the 'Web View'. Desk view is for users who regularly interact with ERPNext instance, like employees. It is feature rich and needs a bit of familiarisation. 'Web View' is for users who need to interact with ERPNext instance occasionally. Webforms are similar to the forms you generally fill in various websites on internet. Webforms are part of 'Web View' interface in ERPNext.

Stakeholders who are not part of your organisation may need to interact with your ERPNext instance. You can authorise customers, suppliers, job applicants, students, and guardians to access certain information or even create certain transactions. For example, you can let anyone create an account on your website (created with ERPNext) and apply for job. You can let your customers see the details of complaints they have registered.

This can be done using the Webforms.

### Creating Web Form

To create a new **Web Form** go to:

> Website > Web Form > New

1. Add appropriate 'Title'.
1. 'Route' is set automatically based on the title. You can change it if required.
1. Select the **DocType** in which you want the data filled by user needs to be stored.
1. Select the 'Module' to which this webform belongs.
1. Check 'Published' once your webform is complete and ready to be accessed.
1. Check 'Login Required' if the web form has to be accessible to only those users who have an account and are logged in.
1. Check 'Allow Edit' to make the web form editable, if you leave it unchecked the forms become read-only once it is saved.
1. Check 'Show as Grid' if the data should be displayed in a table format.
1. Check 'Allow Delete' if the user can delete the webforms that he/she has created.
1. Check 'Allow Print' if the user can take a print out.
1. Select the applicable 'Print Format'.
1. Check 'Allow Comments' checkbox if user can add comments.
1. Check 'Allow Incomplete Forms' if user is allowed to save the webforms with partial data.
1. Finally add the fields from DocType in 'Fields Table'.


### Introduction

You can add a small text here to set the context for the web form.

<img class="screenshot" alt="Web Form Introduction" src="{{docs_base_url}}/assets/img/website/webform_introduction.png">

### Fields in Web Form

You can only select the fields available in the DocType. You cannot create new fields directly in the webform.

You can click on 'Get Fields' button on the top to add all fields in the DocType to the web form.

<img class="screenshot" alt="Web Form Entry" src="{{docs_base_url}}/assets/img/website/webform-1.png">

Once you create the web form, you can view it on the URL(Route) and test it out!

### Creating Web Forms with Child Table

You can add child tables to your web forms, just like regular forms.

<img class="screenshot" alt="Web form Grid" src="{{docs_base_url}}/assets/img/website/grid-in-webform.png">

### Pagination

To help your users fill out long new forms, you can insert page breaks that will appear on new sections. This way the user to focus on only filling one section at a time.

<img class="screenshot" alt="Web form paging" src="{{docs_base_url}}/assets/img/website/paging-in-webform.png">

### Sidebar Settings

Check 'Show Sidebar' if the sidebar needs to be displayed along with the web form.

And add the links to be shown in the sidebar of the web form by adding the details in the table.

<img class="screenshot" alt="Sidebar" src="{{docs_base_url}}/assets/img/website/sidebar.png">

### Payment Gateway Integration

You can now add a Payment Gateway to the web form, so that you can ask users to pay against a web form. A good example for this is a conference ticket :)

<img class="screenshot" alt="Web form payment" src="{{docs_base_url}}/assets/img/website/payment-in-webform.png">

### Portal User

We have also introduced roles for Website users. Before version 11, if you assigned any 'Role' to a user he would get access to 'Desk View'. From version 11 you can assign a 'Role' but still disallow access to 'Desk View' by unchecking 'Desk Access' in Role.

<img class="screenshot" alt="Disallow Desk Access" src="{{docs_base_url}}/assets/img/website/disallow_desk_access.png">

In Portal Settings, you can set a role against each menu item so that only users with that role will be allowed to see that item.

<img class="screenshot" alt="portal settings" src="{{docs_base_url}}/assets/img/website/portal-settings.png">

### Custom Script

You can write code in javascript to implement custom logic and set the URL to the webpage to which the user must be redirected after successful submission of webform.

### Actions

You can add the text in 'Success Message' field and this text will be shown to user once he successfully submits the web form . And the user is redirected to the URL given at 'Success URL' when clicked on 'Continue' button. This is only applicable to webforms accessible without the user login(webforms with 'Login Required' checkbox unchecked).

<img class="screenshot" alt="Success Message" src="{{docs_base_url}}/assets/img/website/success_message.png">


### Result

When website user submits the form, the data will be stored in the document/doctype for which web form is created.

### Customizing

For customising web forms, see the [Frappe Documentation of Web Forms](https://frappe.io/docs/user/en/guides/portal-development/web-forms)


{next}
