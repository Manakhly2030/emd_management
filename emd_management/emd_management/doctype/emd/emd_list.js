let imports_in_progress = [];

frappe.listview_settings['EMD'] = {
	onload:function(listview){
		console.log("chale chhe ke nai")
		var method = "emd_management.emd_management.doctype.emd.emd.set_multiple_status";

		listview.page.add_action_item(__("Set as Open"), function() {
			listview.call_for_selected_items(method, {"status": "Open"});
		});
	},

	add_fields: ['status'],
	get_indicator: function(doc) {
		
		if(doc.status === "Due"){
            return [__("Due"), "orange", "status,=,Due"];
        }
		if(doc.status === "Refunded"){
            return [__("Refunded"), "green", "status,=,Refunded"];
        }
		if(doc.status === "Paid"){
            return [__("Paid"), "blue", "status,=,Paid"];
        }
		if(doc.status === "Forfeited"){
            return [__("Forfeited"), "red", "status,=,Forfeited"];
        }
	},
	hide_name_column: true
};
