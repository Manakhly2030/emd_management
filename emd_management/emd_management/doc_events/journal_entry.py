import frappe

def on_cancel(self, method):
    frappe.db.set_value("EMD", {'reference_num': self.cheque_no}, 'journal_entry', None)
