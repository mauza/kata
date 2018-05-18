from infusionsoft.library import Infusionsoft
from xmlrpc.client import ServerProxy

# Infusionsoft Settings
INFUSION_XMLRPC_ACCT = 'spendingtracker'
INFUSION_XMLRPC_URL = 'https://spendingtracker.infusionsoft.com/api/xmlrpc'
INFUSION_XMLRPC_KEY = 'f4ab7ed93f7dc77b7ee115ebee5d9f53'

class InfusionsoftAlt(Infusionsoft):
    def __init__(self, name, api_key):
        Infusionsoft.__init__(self, name, api_key)
        self.client = ServerProxy("https://" + name + ".infusionsoft.com/api/xmlrpc", use_datetime=True)

def get_infusionsoft_connection():
    infusion_name = INFUSION_XMLRPC_ACCT
    infusion_key = INFUSION_XMLRPC_KEY
    infusionsoft = InfusionsoftAlt(infusion_name, infusion_key)
    return infusionsoft