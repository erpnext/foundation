# -*- coding: utf-8 -*-
# Copyright (c) 2019, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from frappe.website.render import clear_cache as clear_website_cache

class FoundationProject(Document):
	def validate(self):
		clear_website_cache()
