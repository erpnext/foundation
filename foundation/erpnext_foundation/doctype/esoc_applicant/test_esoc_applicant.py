from __future__ import unicode_literals
from frappe import _
import frappe
import unittest

class TestESoCApplicant(unittest.TestCase):
	def validate(self):
		frappe.throw(_("Test Exception"))
