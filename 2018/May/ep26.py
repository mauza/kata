
def find_repeat(n):
    for x in range(1,1000):
        nines = '9'*x
        if int(nines)%n == 0:
            return len(nines)
    return 1

num = 1
max_repeat = 0
for i in range(1,1000):
    tmp_max = find_repeat(i)
    if tmp_max > max_repeat:
        max_repeat = tmp_max
        num = i

print(num)
print(max_repeat)