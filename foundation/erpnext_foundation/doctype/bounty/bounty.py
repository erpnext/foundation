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
		paid_backers = [backer for backer in self.bounty_backer if backer.paid]
		no_of_backers = len(paid_backers)
		if no_of_backers == 0:
			no_of_backers = 'Be the first to back this bounty'
		elif no_of_backers == 1:
			no_of_backers = str(no_of_backers) + ' backer'
		else:
			no_of_backers = str(no_of_backers) + ' backers'

		bounty_left = self.goal - self.bounty_collected
		if bounty_left > (self.goal * 0.1) or bounty_left < 0:
			bounty_left = self.goal * 0.1

		context.no_cache = True
		context.no_breadcrumbs = False
		context.days_to_go = date_diff(self.end_date, nowdate())
		context.paid_backers = ", ".join([backer.full_name or backer.user for backer in paid_backers])
		context.no_of_backers = no_of_backers
		context.fmt_money = fmt_money
		context.bounty_left = bounty_left
		context.comment_list = get_comment_list(self.doctype, self.name)

	def validate(self):
		from frappe.utils.user import get_user_fullname

		self.bounty_collected = sum([backer.amount for backer in self.bounty_backer if backer.paid])
		if not self.route:
			self.published = 1
			self.route = 'bounties/' + self.feature_name.lower().replace(' ', '-')

		bounty_backers = []
		for backer in self.bounty_backer:
			if backer.user and not backer.full_name:
				backer.full_name = get_user_fullname(backer.user)
			bounty_backers.append(backer)
		self.bounty_backer = bounty_backers

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Bounties'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<a href="new-bounty" class="btn btn-primary">Start a new Bounty</a>'
	context.fmt_money = fmt_money