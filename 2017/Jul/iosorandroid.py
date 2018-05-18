import xmlrpc.client as xmlrpclib
import csv

INFUSION_XMLRPC_URL = "https://spendingtracker.infusionsoft.com/api/xmlrpc"
INFUSION_XMLRPC_KEY = 'e49b6d0134917af89568c39d8d6ba1cb'

def has_ios_tag(id):
    proxy = xmlrpclib.ServerProxy(INFUSION_XMLRPC_URL)
    groups = proxy.DataService.findByField(
                INFUSION_XMLRPC_KEY,
                'ContactGroupAssign',           # Table name
                10,                             # Limit
                0,                              # Page
                'ContactId',                    # Identification type
                str(id),      # Identification
                ['GroupId', 'ContactGroup'])    # Requested info
    tags = [str(group['ContactGroup']) for group in groups]
    for tag in tags:
        if "ios" in tag.lower():
            return True
    return False

filereader = csv.reader(open("users.csv"), delimiter=",")

header = next(filereader)
with open("iosUsers.csv", "w") as output:
    writer = csv.writer(output, delimiter=',')
    for id, infusion, email, created, expiration in filereader:
        if not infusion:
            continue
        if has_ios_tag(int(infusion.replace(',',''))):
            writer.writerow((id,email,created,expiration))
