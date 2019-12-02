

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

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def main():
    x = 646
    while True:
        num_list = [x, x+1, x+2, x+3]
        x += 1
        trues = 0
        for n in num_list:
            if len(set(prime_factors(n))) == 4:
                trues += 1
        if trues == 4:
            print(num_list)

if __name__ == "__main__":
    main()
