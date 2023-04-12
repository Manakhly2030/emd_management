# Copyright (c) 2023, FinByz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt
from frappe.utils.background_jobs import enqueue
from erpnext.accounts.utils import get_fiscal_year, now , getdate



class EMD(Document):  
    def set_status(self):
        if not self.returned and not self.forfeited:
            self.status = "Paid"
        current_date = now()
        if self.due_date > str(getdate()):
            self.status ="Due"
        # if self.forfeited:
        #     self.status = "Forfeited"

    def on_submit(self):
        self.set_status()
        jv = frappe.new_doc("Journal Entry")
        jv.posting_date = self.posting_date
        jv.voucher_type = "EMD Entry"
        jv.company = self.company
        abbr = frappe.db.get_value("Company", self.company, 'abbr')
        naming_series = f"{abbr}/EMDJV/"
        jv.naming_series = naming_series
        jv.cheque_no = self.reference_num
        jv.cheque_date = self.reference_date
        jv.append('accounts', {
            'account': self.deposit_account,
            'party_type': 'Customer',
            'party': self.customer,
            'debit_in_account_currency': self.amount,
            'cost_center': self.cost_center
        })
        if self.expense_account:
            jv.append('accounts', {
            'account': self.expense_account,
            'debit_in_account_currency': self.extra_charges,
            'cost_center': 'Main - ' + abbr
        })
        if self.is_opening == "Yes":
            jv.append('accounts', {
                'account': "Temporary Opening - " + abbr,
                'credit_in_account_currency': flt(self.amount),
                'cost_center': 'Main - ' + abbr
            })
            jv.is_opening = "Yes"
        else:
            jv.append('accounts', {
                'account': self.bank_account,
                'credit_in_account_currency': flt(self.amount + self.extra_charges),
                'cost_center': 'Main - ' + abbr
            })
        jv.save()
        self.db_set('journal_entry', jv.name)
        jv.submit()
        self.send_email()

    @frappe.whitelist()
    def cancel_return(self):
        if self.return_journal_entry:
            jv = frappe.get_doc("Journal Entry", self.return_journal_entry)
            self.returned = 0
            self.return_account = None
            self.return_date = None
            self.db_set('return_journal_entry', None)
            jv.cancel()
        
    def on_update_after_submit(self):
        if self.returned == 1 and not self.return_journal_entry:
            jv = frappe.new_doc("Journal Entry")
            jv.posting_date = self.return_date
            jv.voucher_type = "EMD Entry"
            jv.company = self.company
            
            abbr = frappe.db.get_value("Company", self.company, 'abbr')
            naming_series = f"{abbr}/EMDJV/"
            jv.naming_series = naming_series
            jv.cheque_no = self.reference_num
            jv.cheque_date = self.reference_date
            
            jv.append('accounts', {
                'account': self.deposit_account,
                'party_type': 'Customer',
                'party': self.customer,
                'credit_in_account_currency': self.amount,
                'cost_center': 'Main - ' + abbr
            })

            if self.interest_account and self.interest_amount > 0:
                jv.append('accounts', {
                'account': self.interest_account,
                'credit_in_account_currency': self.interest_amount,
                'cost_center': 'Main - ' + abbr		
                })
                jv.append('accounts', {
                    'account': self.return_account,
                    'debit_in_account_currency': flt(self.amount+self.interest_amount),
                    'cost_center': 'Main - ' + abbr
                })
            else:
                jv.append('accounts', {
                    'account': self.return_account,
                    'debit_in_account_currency': flt(self.amount),
                    'cost_center': 'Main - ' + abbr
                })
            jv.save()
            self.db_set('return_journal_entry', jv.name)
            jv.submit()
            self.db_set("status", "Refunded")
        elif self.forfeited == 1:
            self.db_set("status", "Forfeited")
        else:
            self.db_set("status", "Paid")


        if self.forfeited==1:
            jv = frappe.new_doc("Journal Entry")
            jv.posting_date = self.due_date
            jv.voucher_type = "EMD Entry"
            jv.company = self.company

            abbr = frappe.db.get_value("Company", self.company, 'abbr')
            naming_series = f"{abbr}/EMDJV/"
            jv.naming_series = naming_series
            jv.cheque_no = self.reference_num
            jv.cheque_date = self.reference_date
        
            jv.append('accounts', {
            'account': self.deposit_account,
            'party_type': 'Customer',
            'party': self.customer,
            'credit_in_account_currency': self.amount
            }) 
            jv.append('accounts', {
            'account': self.write_off_account,
            'debit_in_account_currency': self.amount
            })
            
            jv.save()
            # self.db_set('return_journal_entry', jv.name)
            jv.submit()
            self.db_set("status", "Forfeited")
        elif self.returned == 1:
            self.db_set("status", "Refunded")
        else:
            self.db_set("status", "Paid")
            
    def on_cancel(self):
        se = frappe.get_doc("Journal Entry", self.journal_entry)
        if self.get("return_journal_entry"):
            se1 = frappe.get_doc("Journal Entry", self.return_journal_entry)
            se1.cancel()
            self.db_set('return_journal_entry', None)

        se.cancel()
        self.db_set('journal_entry', None)


    def send_email(self):
        email_args = {
            "recipients": self.receipient,
            "cc": self.cc_to,
            "message": self.invitation_message,
            "subject": "Refund Of EMD"
            }
        frappe.sendmail(**email_args)

def send_emails(self):
    data=frappe.db.get_list("EMD" , {'send_weekly_reminder' : 1 , "returned" : 0},fields=["receipient", "cc_to", "invitation_message"])
    for i in data:
        email_args = {
            "recipients": i.receipient,
            "cc": i.cc_to,
            "message": i.invitation_message,
            "subject": "Refund Of EMD"
            }
        
        enqueue(method=frappe.sendmail, queue='long', timeout=5000, **email_args)

@frappe.whitelist()
def set_multiple_status(names, status):
	names = json.loads(names)
	for name in names:
		set_status(name, status)



@frappe.whitelist()
def set_status(name, status):
	st = frappe.get_doc("EMD", name)
	st.status = status
	st.save()
        
def change_status_on_due(self):
    if self.due_date > str(getdate()):
        self.status ="Due"


    