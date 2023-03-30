// Copyright (c) 2023, FinByz and contributors
// For license information, please see license.txt

frappe.ui.form.on('EMD', {
	refresh: function(frm) {
		frm.set_query('customer', function(doc) {
			return {
				filters: {
					"disabled": 0,
				}
			};
		});

		if (frm.doc.return_journal_entry) {
			cur_frm.set_df_property("return_account", "read_only", 1);
			cur_frm.set_df_property("interest_amount", "read_only", 1);
			cur_frm.set_df_property("interest_account", "read_only", 1);
			cur_frm.set_df_property("return_date", "read_only", 1);
		}
		else {
			cur_frm.set_df_property("return_account", "read_only", 0);
			cur_frm.set_df_property("interest_amount", "read_only", 0);
			cur_frm.set_df_property("interest_account", "read_only", 0);
			cur_frm.set_df_property("return_date", "read_only", 0);
		}
		if(!frm.doc.__islocal && frm.doc.return_journal_entry){
			frm.set_df_property('returned', 'read_only',1);
			frm.set_df_property('return_account', 'read_only',1);
			frm.set_df_property('return_date', 'read_only',1);
		}
	},

	customer:function(frm){
		frappe.call({
			method:"emd_management.api.get_party_details",
			args:{
				party:frm.doc.customer,
				party_type:"Customer"
			},
			callback:function(r){
				if(r.message){
					frm.set_value('contact_person',r.message.contact_person)
					frm.set_value('contact_display',r.message.contact_display)
					frm.set_value('contact_mobile',r.message.contact_mobile)
					frm.set_value('contact_email',r.message.contact_email)
					frm.set_value('address_display',r.message.address_display)
					frm.set_value('address',r.message.customer_address)
				}
			}
				
		})
	},

	address: function(frm){
		if(cur_frm.doc.address) {
			return frappe.call({
				method: "frappe.contacts.doctype.address.address.get_address_display",
				args: {
					"address_dict": frm.doc.address
				},
				callback: function(r) {
					if(r.message)
						frm.set_value("address_display", r.message);
				}
			});
		}
	},

	
});

// Contact Query Filter
cur_frm.set_query("contact_person", function() {	
	return {
		query: "frappe.contacts.doctype.contact.contact.contact_query",
		filters: { link_doctype: "Customer", link_name: cur_frm.doc.customer } 
	};

});

// Address Filter
cur_frm.set_query("address", function() {
	return {
		query: "frappe.contacts.doctype.address.address.address_query",
		filters: { link_doctype: "Customer", link_name: cur_frm.doc.customer} 
	};

});

cur_frm.fields_dict.bank_account.get_query = function(doc) {
return {
	filters: {
		"account_type": "Bank",
		"company": doc.company
	}
}
};

cur_frm.fields_dict.return_account.get_query = function(doc) {
return {
	filters: {
		"company": doc.company,
		"account_type": "Bank"
	}
}
};

cur_frm.fields_dict.expense_account.get_query = function(doc) {
return {
	filters: {
		"company": doc.company,
		"account_type": "Expense Account"
	}
}
};
cur_frm.fields_dict.interest_account.get_query = function(doc) {
return {
	filters: {
		"company": doc.company,
	"account_type": "Income Account"
	}
}
};



