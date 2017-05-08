# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class Chapter(WebsiteGenerator):
	pass

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Chapters'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<p>All ERPNext Chapters</p>'
