# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.utils import get_comment_list

class Bounty(WebsiteGenerator):
	def get_context(self, context):
		context.no_cache = True

	def validate(self):
		self.bounty_collected = sum([backer.amount for backer in self.bounty_backer if backer.paid])

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Bounties'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<p>ERPNext feature requests</p>'
