import frappe

def execute():
	for job in frappe.get_all("Portal Job"):
		print (job.name)
		frappe.db.set_value("Portal Job", job.name, "route", "erpnext-job/{0}".format(job.name.encode('utf-8')),
			update_modified=False)

