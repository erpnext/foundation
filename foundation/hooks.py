# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "foundation"
app_title = "ERPNext Foundation"
app_publisher = "EOSSF"
app_description = "Website for ERPNext Foundation"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "foundation@erpnext.org"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/foundation/css/foundation.css"
# app_include_js = "/assets/foundation/js/foundation.js"

# include js, css files in header of web template
web_include_css = "/assets/foundation/css/style.css"
# web_include_js = "/assets/foundation/js/foundation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

website_context = {
	"brand_html": "<img class='navbar-icon' src='/assets/foundation/img/erpnext-foundation-icon.svg' />ERPNext Foundation",
	"top_bar_items": [
	 	{"label": "My Account", "url": "/me", "right":1},
	 	# {"label": "Resources", "url": "/resources", "right":1},
	 	# {"label": "About", "url": "/about", "right":1}
	# 	{"label": "Docs", "url": "http://frappe.github.io/erpnext", "right":1},
	# 	{"label": "Blog", "url": "https://frappe.io/blog", "right":1},
	],
	"footer_items": [
		{"label": "ERPNext", "child_items": [
			{"label": "Resources", "url": "/resources"},
			{"label": "Documentation", "url": "https://frappe.github.io/erpnext", "target": "_blank"},
			{"label": "Frappé Framework", "url": "https://frappe.github.io/frappe", "target": "_blank"},
			{"label": "GitHub", "url": "https://github.com/frappe/erpnext", "target": "_blank"},

		]},
		{"label": "Foundation", "child_items": [
			{"label": "About", "url": "/members"},
			{"label": "Memberships", "url": "/members"},
			{"label": "Contact", "url": "/contact"},
			{"label": "Legal", "url": "/legal"},
			{"label": "Terms", "url": "/terms"}
		]},
		{"label": "Community", "child_items": [
			{"label": "Service Providers", "url": "/service-providers"},
			{"label": "Jobs", "url": "/jobs"},
			{"label": "Events", "url": "/events"},
			{"label": "Forum", "url": "https://discuss.erpnext.com", "target": "_blank"}
		]},
	],
	"hide_login": 1,
	"favicon": "/assets/frappe_theme/img/favicon.ico"
}

website_route_rules = [
	{"from_route": "/jobs", "to_route": "Portal Job"},
	{"from_route": "/events", "to_route": "Portal Event"},
]

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "foundation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Service Provider", 'Portal Job']

portal_menu_items = [
	{'label': 'Service Provider Settings', 'route': '/service-provider-settings'},
	{'label': 'Jobs', 'route': '/my-jobs'},
	{'label': 'Membership', 'route': '/members/details'}
]

# Installation
# ------------

# before_install = "foundation.install.before_install"
# after_install = "foundation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "foundation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"foundation.tasks.all"
# 	],
# 	"daily": [
# 		"foundation.tasks.daily"
# 	],
# 	"hourly": [
# 		"foundation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"foundation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"foundation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "foundation.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "foundation.event.get_events"
# }

