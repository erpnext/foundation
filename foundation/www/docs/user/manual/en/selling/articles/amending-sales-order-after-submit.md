<!-- add-breadcrumbs -->
#Amending Sales Order after Submit
Rate and Qty in Sales Order can now be amended after Submit using the `Update Items` button.

<img alt="Update Items" class="screenshot" src="{{docs_base_url}}/assets/img/articles/so-update-items.png">

To Update Rate and Qty in a Submitted Sales Order, click on the `Update Items` button. A dialog will pop up to let you make the change.

<img alt="Update Items" class="screenshot" src="{{docs_base_url}}/assets/img/articles/so-update-items-rate-and-qty.gif">

Please Note the following validations and usecases:

- Update Features checks if Sales Order has Delivery Note and Sales Invoice.
- Qty can be updated for undelivered Sales Order and for Partial Delivery Note. For Sales Order with completed Delivery Notes, it cannot be updated.
- Rate can be updated for un-invoiced and partially-invoiced Sales Order. For Sales Order with submitted Sales Invoice, it cannot be updated.
