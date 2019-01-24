<!-- add-breadcrumbs -->
#Bulk Editing in Existing Documents

Bulk Update tool helps you in over-writing value of a specific field in existing records.

<img alt="Emailing Attachments" class="screenshot" src="{{docs_base_url}}/assets/img/articles/bulk-update-tool.png">

If you would like to overwrite value of a field based on certain condition you can use bulk update with conditions.

Lets say you have a customer group named 'Commercial' and you would like to change that to 'Retail' for all customer records.

Below are the steps to do so...

#### Step 1: Open Bulk Update

You can open bulk update tool by typing and selecting Bulk Update in Awesome Bar or Search Bar at the top.

#### Step 2: Select the DocType

All the Document Types are listed in 'Document Type' field.

Select Customer in 'Document Type' field.

#### Step 3: Select the field

After selecting the Documnet Type, all the fields in that document are listed in 'Field'. Choose the field which you would like to update.

You can choose 'customer_group'.

#### Step 4: Provide the new value

Type the new value in 'Update Value' field.

Type Retail in Update Value field.

#### Step 5: Add Condition if required

You can add the condition here. If the existing records satisfy this condition, only then the values are overwritten.

Conditions should be entered in SQL format.

* You can use a **EQUAL** condition: customer_group = 'Commercial' in Condition field.

* You can use **LIKE** condition: customer_group LIKE 'Commercial'

* You can use multiple conditions with **AND**: customer_group = 'Commercial' AND territory = 'Karnataka'

* You can use **OR** conditions: customer_group = 'Commercial' OR customer_group = 'Individual'

* You can use **NOT** condition: NOT customer_group = 'Commercial'

Enter customer_group = 'Commercial' in condition field.


#### Step 6: Add a Limit

There maybe thousands of record which meet the condition. It is better to update maximum 500 records at a time.

Enter 10 in Limit field.

#### Step 7: Click on 'Update'

Finally click on Update button and check the records to make sure values are updated.

You can also watch a [Video Tutorial on Bulk Update Tool](http://erpnext:8000/docs/user/videos/learn/bulk-update.md).

> Be cautious while using the Bulk Update Tool as data is overwritten. Use Limit feature and update values in batches.

{next}


<!-- markdown -->
