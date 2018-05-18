import csv
from datetime import datetime, date, timedelta


with open('TripsU2016.csv', 'r') as f:
    reader = csv.reader(f)
    expenses = list(reader)

expenses = [[expense[0], datetime.strptime(expense[1][:10], '%m/%d/%Y'), expense[2]] for expense in expenses]

userexpenses = {}
for expense in expenses:
    userexpenses.setdefault(expense[0], []).append([expense[1], expense[2]])

activeusers = {}
with open('tripUoutput2.csv', 'w') as output:
    writer = csv.writer(output)
    for user, e in userexpenses.items():
        found = 0
        for month in range(1, 13, 1):
            for expense in e:
                mdate = datetime.strptime("2016," + str(month) + ",7", '%Y,%M,%d')
                delta = expense[0] - mdate
                if delta < timedelta(days=7):
                    found = found + 1
                    break
            for expense in e:
                mdate = datetime.strptime("2016," + str(month) + ",21", '%Y,%M,%d')
                delta = expense[0] - mdate
                if delta < timedelta(days=7):
                    found = found + 1
                    break
        if found > 23:
            writer.writerow([str(user), str(sum([float(expensetotal[1]) for expensetotal in e]))])
