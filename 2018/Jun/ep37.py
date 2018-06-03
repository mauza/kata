import math

def primes_up_to(n):
    """Generates all primes less than n."""
    if n <= 2: return
    yield 2
    F = [True] * n
    seq1 = range(3, int(math.sqrt(n)) + 1, 2)
    seq2 = range(seq1[-1] + 2, n, 2)
    for p in filter(F.__getitem__, seq1):
        yield p
        for q in range(p * p, n, 2 * p):
            F[q] = False
    for p in filter(F.__getitem__, seq2):
        yield p

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

results = []

for p in primes_up_to(10000000):
    s = str(p)
    include = True
    for i in range(1,len(s)):
        if not isprime(int(s[i:])):
            include = False
            break
        if not isprime(int(s[:i-len(s)])):
            include = False
            break
    if include:
        results.append(p)

print(results)
print(sum(results))