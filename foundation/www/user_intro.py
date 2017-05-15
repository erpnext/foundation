import frappe

def get_context(context):
	context.no_cache = True
	chapter = frappe.get_doc('Chapter', frappe.form_dict.name)
	print chapter
	if frappe.session.user!='Guest':
		if chapter in [d.name for d in chapter]:
			context.already_member = True
		else:
			chapter.append('members', dict(user=frappe.session.user))
			chapter.save(ignore_permissions=1)
			frappe.db.commit()

	context.chapter = chapter
