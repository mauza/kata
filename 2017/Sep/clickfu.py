import csv
import sys

if len(sys.argv) < 2:
    print("You need to provide a file path")
    sys.exit(1)

path = sys.argv[1]
try:
    result = sys.argv[2]
except:
    result = "output.txt"

with open(path, 'r') as csvfile:
    print(path)
    reader = csv.reader(csvfile, delimiter=',')
    with open(result, "a") as output:
        for row in reader:
            if len(''.join(row)) < 1000:
                continue
            output.write('{} {}'.format(row[9], row[8]) + '\n')
            output.write(row[3] + '\n')
            output.write(row[32] + '\n')
            for thing in row[35].split(" :"):
                if thing.startswith('question'):
                    output.write(thing.split('"')[1] + '\n')
                elif thing.startswith('answer'):
                    output.write(thing.split('"')[1] + '\n')
            output.write('\n\n')
