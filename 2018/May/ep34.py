import math

def check_fac(n):
    s = 0
    for d in str(n):
        s += math.factorial(int(d))
    if s == n:
        return True
    return False

results = []

for num in range(3, 1000000):
    if check_fac(num):
        results.append(num)

print(results)
print(sum(results))