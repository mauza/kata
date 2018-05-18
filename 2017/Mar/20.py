from utils import get_infusionsoft_connection


def convert_inf_dict_to_lower(records):
    """
    Converts a list of Infusionsoft query results with the usual key casing like
    'CardType' to something more similar to the model casing like 'card_type'
    """
    for i, record in enumerate(records):
        lowered = {to_lower(k): v for k, v in record.iteritems()}
        records[i] = lowered
    return records


def get_invoices_for_contact(contact_id, exclude_old=False, unpaid_only=False):
    infusion = get_infusionsoft_connection()
    query = {'contactID': contact_id}
    fields = [
        "Id",
        "PayStatus",
        "TotalDue",
        "TotalPaid",
        "DateCreated",
        "Description",
        "JobId"]

    if unpaid_only:
        query = {'contactID': contact_id, 'PayStatus': 0}

    invoices = infusion.DataService('query', 'Invoice', 1000, 0, query, fields, 'DateCreated', False)
    # Infusionsoft won't attempt to charge invoices older than three months, so this allows us to exclude those
    if exclude_old:
        invoices = [invoice for invoice in invoices if invoice['DateCreated'] > datetime.today() - timedelta(days=30*3)]
    return convert_inf_dict_to_lower(invoices)

# infID = 979570

# invoices = get_invoices_for_contact(infID)
# print("invoices:")
# for invoice in invoices:
# 	print(invoice)

infusion = get_infusionsoft_connection()

invoices = infusion.DataService('query', 'Invoice', 1000, 0, {'contactID'})
