import csv
from sets import Set

trips = 'data/trip.csv'
tripsunclas = 'data/tripunclas.csv'
expense = 'data/expense.csv'

emails = Set()
with open(trips, 'r') as t, open(tripsunclas, 'r') as tu, open(expense, 'r') as e:
	treader = csv.reader(t)
	tlist = list(treader)
	conv = [tconv[0] for tconv in tlist]
	emails.update(conv)

	tureader = csv.reader(tu)
	tulist = list(tureader)
	conv = [tconv[0] for tconv in tulist]
	emails.update(conv)

	ereader = csv.reader(e)
	elist = list(ereader)
	conv = [tconv[0] for tconv in elist]
	emails.update(conv)

print(len(emails))