

def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            if not i in factors:
                factors[i] = 0
            factors[i] += 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    yield from generate(0)

abundant_numbers = []
# print(list(divisors(28)))
for num in range(28124):
    if sum(list(divisors(num))[:-1]) > num:
        abundant_numbers.append(num)

sum_an = []

for x in abundant_numbers:
    for y in abundant_numbers:
        san = x + y
        sum_an.append(san)

nums = set(sum_an)
s = 0
for num in range(28124):
    if num not in nums:
        s += num

print(s)
