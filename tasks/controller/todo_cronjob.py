import frappe

def create_todo():
 
    doc = frappe.get_doc({
    'doctype': 'ToDo',
    'description':  'description',
    "status": "Open",
        
    })
    doc.insert()

