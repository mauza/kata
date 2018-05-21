
total = 0

for num in range(2, 10000000):
    s = 0
    for digit in str(num):
        s += int(digit)**5
    if s == num:
        print(num)
        total += num
print(total)