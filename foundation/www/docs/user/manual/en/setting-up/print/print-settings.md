<!-- add-breadcrumbs -->
# Print Settings

In Print Settings you can set your default printing preferences like Paper Size, default text size, whether you want output as PDF or HTML etc.

To edit print settings, go to:

> Setup > Printing and Branding > Print Settings

<img class="screenshot" alt="Print Settings" src="{{docs_base_url}}/assets/img/setup/print/print-settings.png">


#### Network Printer

You can enable print server by fill the print server IP and port then chose default printer

Befor enabling this feature you have to install pycups in the env using the command

`./env/bin/pip install pycups`

executed from the `frappe-bench` directory.

And install cups package

For Debian OS Family:

`sudo apt-get install libcups2-dev`

For Redhat OS Family:

`sudo yum install cups-libs`


{next}
