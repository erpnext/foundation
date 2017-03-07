# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

from frappe.utils import getdate
import frappe

def get_last_membership():
	'''Returns last membership if exists'''
	last_membership = frappe.get_all('Membership', 'name,to_date,membership_type',
		dict(member=frappe.session.user), order_by='to_date desc', limit=1)

	return last_membership and last_membership[0]

def is_member():
	'''Returns true if the user is still a member'''
	last_membership = get_last_membership()
	if last_membership and getdate(last_membership.to_date) > getdate():
		return True
	return False