# Table MultiSelect

Table MultiSelect field is very similar to Link Field. The key difference is Table MultiSelect field allows you to select multiple values.

You may like to assign a 'ToDo' to multiple users as shown below.

<img alt="Table MultiSelect Field" class="screenshot" src="{{docs_base_url}}/assets/img/articles/table-multiselect-field.png">


You can add a Table MultiSelect Field by following below steps.

####Step 1: Create a child DocType.

Create a new DocType, check 'Is Child Table' and 'Editable Grid' checkboxes and add a field with 'Link' type as shown below.

Set the link field as mandatory.

<img alt="DocType for Table MultiSelect" class="screenshot" src="{{docs_base_url}}/assets/img/articles/doctype-for-table-multi-select.png">




####Step 2: Add a field with type 'Table MultiSelect'.

Create a field with type 'Table MultiSelect' and add the DocType created in first step in 'options'.

<img alt="Field with type Table MultiSelect" class="screenshot" src="{{docs_base_url}}/assets/img/articles/multi-select-field.png">

You can remove any selected value by clicking on the cross sign next to selected value or by placing the cursor next to the value and pressing Backspace.

This field allows one value to be selected only once.

{next}
