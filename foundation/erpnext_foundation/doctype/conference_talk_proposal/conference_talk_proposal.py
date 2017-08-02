# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class ConferenceTalkProposal(WebsiteGenerator):
	def get_context(self, context):
		context.show_sidebar = 1
		context.website_sidebar = 'Conference 2017 Sidebar'


def get_list_context(context):
	context.title = 'Talk Proposals'
	context.no_breadcrumbs = 1

