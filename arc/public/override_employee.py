from frappe.utils import nowdate, getdate

def calculate_num_of_months(doc, method):

    today = nowdate()
    first_exp = doc.custom_first_experience_date
    months_diff = getdate(today).month - getdate(first_exp).month
    doc.custom_experience_in_months = months_diff

    