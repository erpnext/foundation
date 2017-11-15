import frappe

def get_context(context):
	context.no_cache = True
	chapter = frappe.get_doc('Chapter', frappe.form_dict.name)
	# if frappe.session.user!='Guest':
	if frappe.session.user in [d.user for d in chapter.members]:
		user = frappe.session.user
		parent = frappe.form_dict.name
		leave_reason = frappe.form_dict.leave
		frappe.db.sql("""UPDATE `tabChapter Member` SET enabled = 0, leave_reason = %s WHERE parent = %s and user = %s ;""", (leave_reason, parent, user))
		frappe.db.commit()


	context.member_deleted = True

	context.chapter = chapter

# def leave(title, user_id, leave_reason):
# 	chapter = frappe.get_doc("Chapter", title)
# 	for member in chapter.members:
# 		for x in xrange(1,10):
# 			print(member.user, user_id)
# 		if member.user == user_id:
# 			member.enabled = 0
# 			member.leave_reason = leave_reason
# 	chapter.save()
# 	frappe.db.commit()
# 	return "Thank you for Feedback"