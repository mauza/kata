


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


def goldbach_guess(p, s):
    return p + 2*(s**2)

def gen_odd_composites(limit_num):
    for i in range(3, limit_num, 2):
        if isprime(i):
            continue
        yield i

def gen_primes_until(n):
    for i in range(3, n+1, 2):
        if isprime(i):
            yield i

def main():
    for oc in gen_odd_composites(10000000):
        conjecture_worked = False
        for p in gen_primes_until(oc):
            if conjecture_worked:
                break
            for s in range(int(oc**0.5)):
                if goldbach_guess(p,s) == oc:
                    conjecture_worked = True
                    break
        if not conjecture_worked:
            print(f"odd composite {oc} does follow goldbach conjecture")


if __name__ == "__main__":
    main()
