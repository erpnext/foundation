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
# web_include_css = "/assets/foundation/css/style.css"
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

template_apps = ['foundation', 'frappe_theme', 'erpnext', 'frappe']
website_context = {
	# "navbar_search": 1,
	"brand_html": "<img class='mr-2 d-inline-block align-top' width='30px' height='30px' src='/assets/foundation/img/erpnext-logo.svg' alt='Oensource ERP Software'/>ERPNext.org",
	"top_bar_items": [
			{"label": "ERPNext", "child_items":[
				{"label": "Get ERPNext", "url": "/get-started"},
				{"label": "User Manual", "url": "/docs/user"},
				{"label": "Free Trial", "url": "https://erpnext.com"},
			], "right":1},
			{"label": "Community", "child_items":[
				{"label": "Forum", "url": "https://discuss.erpnext.com", "target": "target='_blank'"},
				{"label": "Chapters", "url": "/chapter-list"},
				{"label": "Fellows", "url": "/fellows"}
			], "right":1},
			{"label": "Services", "child_items":[
				{"label": "Service Providers", "url": "/service-providers"},
				{"label": "Freelancer Jobs", "url": "/erpnext-jobs"},
				{"label": "Become a Service Provider", "url": "/faq"}
			], "right":1},
			{"label": "Foundation", "child_items":[
				{"label": "About", "url": "/about"},
				{"label": "Blog", "url": "/blog"},
				{"label": "Memberships", "url": "/members"},
			], "right":1},
	],
	"hide_login": 0,
	"favicon": "/assets/foundation/img/favicon.ico"
}
# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "foundation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Service Provider", 'Portal Job', 'Portal Event']

portal_menu_items = [
	{'label': 'My Profile', 'route': '/service-provider-settings'},
	{'label': 'Module Leader', 'route': '/module-leader-settings'},
	{'label': 'Membership', 'route': '/members/details'},
	{'label': 'Conference Talks', 'route': '/conference-talk-proposal'},
	{'label': 'Jobs', 'route': '/my-jobs'},
	{'label': 'Events', 'route': '/add-event'},
	{'label': 'Apps', 'route': '/submit-app'},
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

scheduler_events = {
	# "all": [
	# 	"foundation.tasks.all"
	# ],
	"daily": [
		"foundation.erpnext_foundation.doctype.service_provider.service_provider.send_alert_to_inactive_service_providers",
		"foundation.erpnext_foundation.doctype.service_provider.service_provider.unpublish_service_provider",
		"foundation.erpnext_foundation.doctype.service_provider.service_provider.publish_service_provider",
	],
	# "hourly": [
	# 	"foundation.tasks.hourly"
	# ],
	# "weekly": [
	# 	"foundation.tasks.weekly"
	# ]
	# "monthly": [
	# 	"foundation.tasks.monthly"
	# ]
}

# Testing
# -------

# before_tests = "foundation.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "foundation.event.get_events"
# }
