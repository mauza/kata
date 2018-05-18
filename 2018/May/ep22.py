f = open('names.txt', 'r')
names = f.readline().replace('"', '').split(',')
names = sorted(names)
total = 0
for i in range(len(names)):
    name_cost = sum([ord(char) - 96 for char in names[i].lower()])
    total = total + (name_cost*(i+1))
print(total)