import frappe
import foundation

no_cache = 1

def get_context(context):
    '''Returns all certified consultants'''
    all_consultants = {}
    all_consultants = frappe.db.sql(""" select website_url,image,name_of_consultant,github_id,discuss_id
        from `tabCertified Consultant`
        where show_in_website = 1""" ,as_dict=True)
    context.all_consultants = all_consultants
