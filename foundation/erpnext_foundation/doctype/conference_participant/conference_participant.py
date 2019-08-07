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
		self.amount = self.full_conference_tickets * (5000 if self.currency == 'INR' else 80)

	def on_payment_authorized(self, status_changed_to=None):
		self.paid = 1
		self.save(ignore_permissions=True)
		self.create_and_send_invoice()

	def create_and_send_invoice(self):
		transaction = get_integration_request(self.name, self.currency)
		if not transaction:
			return
		series = 'BC-19-20-'
		rate = '5000'
		currency = 'INR'
		customer = 'ERPNext Conference 2019 Participant'
		item_income_account = 'Sales - Event Tickets - EF'
		account_type = 'Debtors - EF'
		taxes = [
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

		if transaction.service == 'Paypal':
			series = 'EXP-19-20-'
			rate = '80'
			currency = 'USD'
			account_type = 'Debtors USD - EF'
			customer = 'ERPNext Conference 2019 Participant International'
			item_income_account = 'Sales - Event Tickets (International) - EF'
			taxes = []

		invoice = frappe.get_doc({
			'doctype': 'Sales Invoice',
			'customer': customer,
			'debit_to': account_type,
			'remarks': json.dumps(transaction),
			'currency': currency,
			'selling_price_list': currency,
			'series': series,
			'payment_mode': transaction.service,
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
			'taxes': taxes
		})

		invoice.insert(ignore_permissions=True)
		invoice.submit()

		self.make_payment_entry(invoice, transaction, currency)
		self.send_email(invoice)

	def make_payment_entry(self, invoice, transaction, currency):
		from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry
		frappe.flags.ignore_account_permission=True
		pe = get_payment_entry(dt='Sales Invoice', dn=invoice.name, bank_amount=invoice.grand_total)
		frappe.flags.ignore_account_permission=False
		pe.paid_to = frappe.get_value("Mode of Payment Account",
					{'parent': transaction.service,
					'parenttype': 'Mode of Payment'},
					['default_account'])

		pe.paid_to_account_currency = currency

		pe.target_exchange_rate = invoice.conversion_rate
		pe.source_exchange_rate = invoice.conversion_rate
		pe.mode_of_paypment = transaction.service

		pe.reference_no = transaction.transaction_id
		pe.reference_date = invoice.posting_date
		pe.save(ignore_permissions=True)
		pe.submit()

	def send_email(self, invoice):
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
		transaction = frappe.get_all('Integration Request', filters=filters, fields=['name', 'data'])[0]
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
