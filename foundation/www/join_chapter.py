import frappe

def get_context(context):
	if frappe.session.user!='Guest':
		chapter = frappe.get_doc('Chapter', frappe.form_dict.name)

		if frappe.session.user not in [d.user for d in chapter.members]:
			chapter.append('members', dict(user=frappe.session.user))
			chapter.save()
			frappe.db.commit()

		context.chapter = chapter
