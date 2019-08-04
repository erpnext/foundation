# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ConferenceParticipant(Document):
	def validate(self):
		self.conference = '2019'

	def validate_payment(self):
		self.amount = self.full_conference_tickets * (5000 if self.currency == 'INR' else 70)

	def on_payment_authorized(self, status_changed_to=None):
		self.paid = 1
		self.save(ignore_permissions=True)