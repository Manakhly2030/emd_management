from . import __version__ as app_version

app_name = "emd_management"
app_title = "Emd Management"
app_publisher = "FinByz"
app_description = "Emd Management App"
app_email = "info@finbyz.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/emd_management/css/emd_management.css"
# app_include_js = "/assets/emd_management/js/emd_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/emd_management/css/emd_management.css"
# web_include_js = "/assets/emd_management/js/emd_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "emd_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {"EMD" : "emd_management/emd_management/doctype/emd/emd_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_js = {"Journal Entry": "public/js/journal_entry.js"}


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "emd_management.utils.jinja_methods",
#	"filters": "emd_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "emd_management.install.before_install"
# after_install = "emd_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "emd_management.uninstall.before_uninstall"
# after_uninstall = "emd_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "emd_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	
	# "EMD": {"on_update_after_submit": "emd_management.emd_management.doctype.emd.emd.on_update_after_submit"},
	"Journal Entry":
	{
		"on_cancel": "emd_management.emd_management.doc_events.journal_entry.on_cancel"
	},
	"EMD":
	{
		"validate":"emd_management.emd_management.doctype.emd.emd.validate"
	}
	
	
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"emd_management.tasks.all"
#	],
#	"daily": [
#		"emd_management.tasks.daily"
#	],
#	"hourly": [
#		"emd_management.tasks.hourly"
#	],
#	"weekly": [
#		"emd_management.tasks.weekly"
#	],
#	"monthly": [
#		"emd_management.tasks.monthly"
#	],
# }
scheduler_events = {
	"weekly": [
		"emd_management.emd_management.doctype.emd.emd.send_emails"
	],
	"daily": [
		"emd_management.emd_management.doctype.emd.emd.change_status_on_due"
	]
}

# Testing
# -------

# before_tests = "emd_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "emd_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "emd_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["emd_management.utils.before_request"]
# after_request = ["emd_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["emd_management.utils.before_job"]
# after_job = ["emd_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"emd_management.auth.validate"
# ]


fixtures = [
       {
        "dt": "Property Setter", 
        "filters":[["name", "in", ['EMD-payment_mode-hidden','EMD-payment_mode-reqd','EMD-receipient-fetch_from','EMD-naming_series-options','EMD-cost_center-fetch_from', 'EMD-write_off_account-allow_on_submit', 'EMD-bank_account-depends_on', 'EMD-cancel_forfeited-depends_on', 'EMD-cost_center-fetch_if_empty', 'EMD-reference_date-default', 'Journal Entry-voucher_type-options']]]
      },
]