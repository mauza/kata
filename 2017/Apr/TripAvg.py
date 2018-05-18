import csv

activeusers = 8331

with open('tripUoutput3.csv', 'r') as f:
    reader = csv.reader(f)
    expenses = list(reader)

total_expenses = sum([float(expense[1]) for expense in expenses if float(expense[1]) < 10000000])

print("Active users: {}".format(activeusers))
print("Total trip miles: {}".format(total_expenses))
print("average: {}".format(total_expenses / activeusers))
