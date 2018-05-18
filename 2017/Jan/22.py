import csv

f1 = "/Users/mauza/Downloads/analytics_b5a3e361c8.csv"
f2 = "/Users/mauza/Downloads/test.csv"

output = {}
fields = ['Name', 'Email', 'Phone', 'Attended Live', 'Watched Replay', '']

with open(f1, 'r') as attend, open(f2, 'r') as act, open("output.csv", 'w') as o:
	attendFileReader = csv.DictReader(attend)
	actFileReader = csv.DictReader(act)
	output = csv.DictWriter(o, fieldnames = fields)
	output.writeheader()
	actEmails = []
	for row in actFileReader:
		actEmails.append(row['Email'])
	for row in attendFileReader:
		if row['Email'] in actEmails:
			output.writerow(row)

