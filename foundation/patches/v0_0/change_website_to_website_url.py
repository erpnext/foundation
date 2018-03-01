import frappe

def execute():
    frappe.db.sql('''
        ALTER TABLE `tabFoundation Fellowship` CHANGE `website` `website_url` varchar(140);
    ''')