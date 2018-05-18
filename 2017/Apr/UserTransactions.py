import csv
from datetime import datetime, timedelta


with open('Trans2016.csv', 'r') as f:
    reader = csv.reader(f)
    transaction = list(reader)

with open('tripoutput.csv', 'r') as f:
    reader = csv.reader(f)
    usertrips = list(reader)

users = [user[0] for user in usertrips]

transaction = [[tran[0], datetime.strptime(tran[1][:10], '%m/%d/%Y'), tran[2]] for tran in transaction]

userexpenses = {}
for tran in transaction:
    userexpenses.setdefault(tran[0], []).append([tran[1], tran[2]])

with open('tranOutput.csv', 'w') as output:
    writer = csv.writer(output)
    for user, e in userexpenses.items():
        if user in users:
            writer.writerow([str(user), str(sum([float(expensetotal[1]) for expensetotal in e]))])
