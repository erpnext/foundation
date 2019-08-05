# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json

class ConferenceParticipant(Document):
	def validate(self):
		self.conference = '2019'

	def validate_payment(self):
		self.amount = self.full_conference_tickets * (5000 if self.currency == 'INR' else 70)

	def on_payment_authorized(self, status_changed_to=None):
		self.paid = 1
		self.save(ignore_permissions=True)

	def on_update(self):
		transaction = get_integration_request(self.name, self.currency)
		if self.paid and transaction:
			self.create_and_send_invoice(transaction)

	def create_and_send_invoice(self, transaction):
		series = 'BC-19-20-'
		rate = '5000'
		currency = 'INR'
		item_income_account = 'Sales - Event Tickets - EF'

		if transaction.service == 'Paypal':
			series = 'EXP-19-20-'
			rate = '70'
			currency = 'USD'
			item_income_account = 'Sales - Event Tickets (International) - EF'


		invoice = frappe.get_doc({
			'doctype': 'Sales Invoice',
			'customer': 'ERPNext Conference 2019 Participant',
			'taxes_and_charges': 'In State GST',
			'debit_to': 'Debtors - EF',
			'remarks': json.dumps(transaction),
			'currency': currency,
			'series': series,
			'items': [
				{
					'item_code': 'ERPNext Conference',
					'rate': rate,
					'qty': self.full_conference_tickets,
					'cost_center': 'Conference - EF',
					'income_account': item_income_account,
					'description': self.name
				}
			],
			'taxes': [
				{
					'charge_type': 'On Net Total',
					'account_head': 'SGST - EF',
					'description': 'SGST',
					'rate': 9,
					'included_in_print_rate': 1,
				},
				{
					'charge_type': 'On Net Total',
					'account_head': 'CGST - EF',
					'description': 'CGST',
					'rate': 9,
					'included_in_print_rate': 1,
				}
			]
		})

		invoice.insert()
		email_args = {
			"recipients": [self.email],
			"message": "Thank you for registering for the ERPNext Conference, Attached herewith is the invoice for the ticket.",
			"subject": 'Invoice for ERPNext Conference',
			"attachments": [frappe.attach_print('Sales Invoice', invoice.name, file_name=invoice.name)],
			"reference_doctype": 'Sales Invoice',
			"reference_name": invoice.name
		}
		frappe.sendmail(**email_args)



def get_integration_request(docname, currency):
	service = 'Paypal'
	transaction_field = 'correlation_id'
	if currency == 'INR':
		service = 'Razorpay'
		transaction_field = 'razorpay_payment_id'

	filters = {
		'reference_doctype': 'Conference Participant',
		'reference_docname': docname,
		'integration_request_service': service,
		'status': ['in', ['Authorized', 'Completed']]
	}

	try:
		transaction = frappe.get_list('Integration Request', filters=filters, fields=['name', 'data'])[0]
	except IndexError:
		return None
	else:
		transaction.data = json.loads(transaction.data)
		return frappe._dict({
			'transaction_id': transaction.data[transaction_field],
			'amount': transaction.data['amount'],
			'name': transaction.name,
			'service': service,
			'ref_ticket': docname,
		})
