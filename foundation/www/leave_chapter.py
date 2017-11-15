import frappe

def get_context(context):
	context.no_cache = True
	chapter = frappe.get_doc('Chapter', frappe.form_dict.name)
	# if frappe.session.user!='Guest':
	if frappe.session.user in [d.user for d in chapter.members]:
		user = frappe.session.user
		parent = frappe.form_dict.name
		# leave_reason = frappe.form_dict.leave
		# frappe.db.sql("""UPDATE `tabChapter Member` SET enabled = 0, leave_reason = %s WHERE parent = %s and user = %s ;""", (leave_reason, parent, user))
		# frappe.db.commit()


	context.member_deleted = True

	context.chapter = chapter
