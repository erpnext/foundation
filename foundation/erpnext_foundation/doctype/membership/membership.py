# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Membership(Document):
	def validate(self):
		member_name = frappe.get_value('Member', dict(email=frappe.user.name))

		if not member_name:
			member = frappe.get_doc(dict(
				doctype='Member',
			))
