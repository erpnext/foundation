# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class FoundationFellowship(WebsiteGenerator):
    website = frappe._dict(
        condition_field = "show_in_website"
    )
    print( "website", website )
    def validate(self):
        if not self.route:
            self.route = 'foundation-fellow/' + self.scrub(self.name)

    def get_context(self, context):
        context.no_cache = True
        context.parents = [dict(label='View All Foundation Fellows',
            route='foundation-fellow', title='View All foundation fellows')]



def get_list_context(context):
    context.allow_guest = True
    context.no_cache = True
    context.no_breadcrumbs = True
    context.order_by = 'creation desc'
    context.introduction = '<p>Following are the Foundation Fellows</p>'
