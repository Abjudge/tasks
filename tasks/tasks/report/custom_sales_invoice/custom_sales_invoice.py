import frappe

def execute(filters=None):
    columns = [
        {"label": "Invoice Number", "fieldname": "invoice_number", "fieldtype": "Link", "options": "Sales Invoice"},
        {"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date"},
        {"label": "Due Date", "fieldname": "due_date", "fieldtype": "Date"},
        {"label": "Company", "fieldname": "company", "fieldtype": "Link", "options": "Company"},
        {"label": "Currency", "fieldname": "currency", "fieldtype": "Link", "options": "Currency"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Select", "options": "Draft\nSubmitted\nPaid\nOverdue\nCancelled"},
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Link", "options": "Customer"},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency"},
        {"label": "Total Tax", "fieldname": "total_tax", "fieldtype": "Currency"},
        {"label": "Total Discount", "fieldname": "total_discount", "fieldtype": "Currency"},
        {"label": "Grand Total", "fieldname": "grand_total", "fieldtype": "Currency"},
        {"label": "Total Qty", "fieldname": "total_qty", "fieldtype": "Float"},
    ]

    data = []
    conditions = ""
    if filters.get("from_date"):
        conditions += f" and si.posting_date >= '{filters.get('from_date')}'"
    if filters.get("to_date"):
        conditions += f" and si.posting_date <= '{filters.get('to_date')}'"

    invoices = frappe.db.sql(f"""
        SELECT  si.name, si.posting_date, si.due_date, si.company, si.currency, si.status, si.customer, si.base_total, si.base_total_taxes_and_charges, si.base_discount_amount, si.base_grand_total, si.total_qty
        FROM `tabSales Invoice` si
        WHERE si.docstatus = 1 {conditions}
    """, as_dict=True)

    for invoice in invoices:
        data.append({
            "invoice_number": invoice.name,
            "posting_date": invoice.posting_date,
            "due_date": invoice.due_date,
            "company": invoice.company,
            "currency": invoice.currency,
            "status": invoice.status,
            "customer": invoice.customer,
            "total_amount": invoice.base_total,
            "total_tax": invoice.base_total_taxes_and_charges,
            "total_discount": invoice.base_discount_amount,
            "grand_total": invoice.base_grand_total,
            "total_qty": invoice.total_qty,
            
        
        })

    return columns, data
 