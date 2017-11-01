# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import add_days, add_years, nowdate, getdate, cint, fmt_money
from frappe import _
import foundation

currency_wise_membership_plan_mapper = {
		"Gold": {
			"USD": 5000,
			"INR": 300000,
		},
		"Silver": {
			"USD": 1500,
			"INR": 100000,
		},
		"Individual": {
			"USD": 200,
			"INR": 10000,
		}
	}

class Membership(Document):
	def validate(self):
		member_name = frappe.get_value('Member', dict(email=frappe.session.user))

		if not member_name:
			user = frappe.get_doc('User', frappe.session.user)
			member = frappe.get_doc(dict(
				doctype='Member',
				email=frappe.session.user,
				member_name=user.get_fullname()
			)).insert(ignore_permissions=True)
			member_name = member.name

		if self.get("__islocal"):
			self.member = member_name

		# get last membership (if active)
		last_membership = foundation.get_last_membership()

		# if person applied for offline membership
		if last_membership and not frappe.session.user == "Administrator":
			# if last membership does not expire in 30 days, then do not allow to renew
			if getdate(add_days(last_membership.to_date, -30)) > getdate(nowdate()) :
				frappe.throw(_('You can only renew if your membership expires within 30 days'))

			self.from_date = add_days(last_membership.to_date, 1)
		elif frappe.session.user == "Administrator":
			self.from_date = self.from_date
		else:
			self.from_date = nowdate()

		self.to_date = add_years(self.from_date, 1)

	def on_payment_authorized(self, status_changed_to=None):
		if status_changed_to in ("Completed", "Authorized"):
			self.load_from_db()
			self.db_set('paid', 1)

			self.link_member_with_service_provider()

	def link_member_with_service_provider(self):
		service_provider = frappe.db.get_value("Service Provider", dict(owner=frappe.session.user))

		if service_provider:
			frappe.db.set_value("Service Provider", service_provider, "member", frappe.session.user,
				update_modified=False)
		else:
			# create new service provider for the member
			doc = frappe.get_doc({
				"doctype": "Service Provider",
				"email": frappe.session.user,
				"title": frappe.db.get_value("Member", self.member, "member_name"),
				"member": self.member,
				"show_in_website": 1
			}).insert(ignore_mandatory=True, ignore_permissions = True)

	def validate_payment(self):
		membership_fees = currency_wise_membership_plan_mapper\
					.get(self.membership_type, {}).get(self.currency)

		if cint(membership_fees) != cint(self.amount):
			formated_membership_fees = fmt_money(membership_fees, precision=0, currency=self.currency)

			frappe.msgprint("For Membership Type: {0}, the fees are {1}".format(self.membership_type,
				formated_membership_fees), raise_exception=frappe.ValidationError,
				title="Validate Payment Amount", indicator='red')
