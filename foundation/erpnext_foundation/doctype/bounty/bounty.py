# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.utils import get_comment_list
from frappe.utils import date_diff, nowdate, fmt_money
from frappe.website.utils import get_comment_list

class Bounty(WebsiteGenerator):
	def get_context(self, context):
		context.no_cache = True
		context.days_to_go = date_diff(self.end_date, nowdate())

		no_of_backers = len(self.bounty_backer)
		if no_of_backers == 0:
			no_of_backers = 'No backers yet'
		elif no_of_backers == 1:
			no_of_backers = str(no_of_backers) + ' backer'
		else:
			no_of_backers = str(no_of_backers) + ' backers'
		context.no_of_backers = no_of_backers
		context.fmt_money = fmt_money

		bounty_left = self.goal - self.bounty_collected

		if bounty_left > (self.goal * 0.1) or bounty_left < 0:
			bounty_left = self.goal * 0.1

		context.bounty_left = bounty_left
		context.comment_list = get_comment_list(self.doctype, self.name)

	def validate(self):
		self.bounty_collected = sum([backer.amount for backer in self.bounty_backer if backer.paid])
		if not self.route:
			self.published = 1
			self.route = 'bounty/' + self.feature_name.lower().replace(' ', '-')

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Bounties'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<a href="new-bounty" class="btn btn-primary">Start a new Bounty</a>'
	context.fmt_money = fmt_money