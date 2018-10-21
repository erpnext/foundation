<!-- add-breadcrumbs -->

#Copy Pasting Multiple Records From Excel

From v11, it is now possible to copy and paste multi records into child table field in the form by simply follow the steps below:

1. Prepare the source data in Excel or text editor with each column separated by tab.

<img alt="Preparing data in Excel" class="screenshot" src="{{docs_base_url}}/assets/img/articles/copy-paste-records/prepare-excel-sheet.png">

2. Drag to select the records , and click the copy menu button or by Ctrl + C (Cmd + C) for 

     Case 1. First line as column header, both field name and label supported, hidden columns can be copied

     Case 2. No column header, the data will directly map to the visible columns

<img alt="Dragging the records" class="screenshot" src="{{docs_base_url}}/assets/img/articles/copy-paste-records/drag-records.png">

3. Place the cursor to the target input field of the child table, paste it by Ctrl + V. Uunlike the import via upload file feature which also can batch input the child table, this copy & paste feature will trigger field change event automatically. In other word if only item_code is pasted, the item price, qty and other item code related fields will be auto populated just like user manually input item code and press ENTER. on the other hand, for performance consideration, less than 100 records per paste is allowed.

<img alt="Cancel Doc" class="screenshot" src="{{docs_base_url}}/assets/img/articles/copy-paste-records/copy-paste-excel-to-child-table.gif">