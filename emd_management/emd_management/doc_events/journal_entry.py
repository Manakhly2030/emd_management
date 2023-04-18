import frappe

def on_cancel(self, method):
    doc = frappe.get_doc("EMD", {'reference_num': self.cheque_no})
    if doc.return_journal_entry or doc.return_forfeited_entry:
        # frappe.throw("test")
        frappe.db.set_value("EMD", {'reference_num': self.cheque_no}, 'journal_entry', None)

