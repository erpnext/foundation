# -*- coding: utf-8 -*-
# Copyright (c) 2018, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe
from frappe.model.document import Document

class ESoCApplicant(Document):
	def validate(self):
		self.validate_dob()
		self.validate_email_type(self.email_id)
		self.validate_agreement_check()

	def validate_email_type(self, email):
		from frappe.utils import validate_email_address
		validate_email_address(email.strip(), True)

	def validate_dob(self):
		from frappe.utils import now_datetime, getdate
		today = now_datetime().date()
		if getdate(self.date_of_birth) >= today:
			frappe.throw(_("Invalid Date of Birth."))

	def validate_agreement_check(self):
		from frappe.utils import cint
		if not cint(self.terms_and_conditions):
			frappe.throw(_("You must agree to the terms and consitions."))
