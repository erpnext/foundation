# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

from frappe.utils import getdate
import frappe

def get_last_membership():
	'''Returns last membership if exists'''
	last_membership = frappe.get_all('Membership', 'name,to_date,membership_type',
		dict(member=frappe.session.user, paid=1), order_by='to_date desc', limit=1)

	return last_membership and last_membership[0]

def get_all_memberships_of_one_member():
	'''Returns last membership if exists'''
	all_memberships = frappe.get_all('Membership', filters={'member'='asbasawaraj@gmail.com','paid': '1'}, fields=['name', 'to_date', 'membership_type'])
	return all_memberships

def is_member():
	'''Returns true if the user is still a member'''
	last_membership = get_last_membership()
	if last_membership and getdate(last_membership.to_date) > getdate():
		return True
	return False
