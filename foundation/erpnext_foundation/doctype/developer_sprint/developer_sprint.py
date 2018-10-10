# -*- coding: utf-8 -*-
# Copyright (c) 2018, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class DeveloperSprint(Document):
	def autoname(self):
		autoname = 'DEV-SPRINT-.YYYY.-.###'
		self.name = make_autoname(autoname)

