import csv

activeusers = 12631.0

with open('output2.csv', 'r') as f:
    reader = csv.reader(f)
    expenses = list(reader)

total_expenses = sum([float(expense[1]) for expense in expenses if float(expense[1]) < 10000000])

print("Active users: {}".format(activeusers))
print("Total expenses: {}".format(total_expenses))
print("average: {}".format(total_expenses / activeusers))
