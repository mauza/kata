

def isprime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def euquad(n, a, b):
    return n*n + n*a + b

b_list = []
for i in range(-999, 1000):
    if isprime(i):
        b_list.append(i)

best_a = 1
best_b = 1
max_consec = 1
for a in range(-999, 1000):
    for b in b_list:
        for n in range(1000):
            prime = isprime(euquad(n,a,b))
            if not prime:
                if n > max_consec:
                    max_consec = n
                    best_a = a
                    best_b = b
                break

print(best_a)
print(best_b)
print(max_consec)
