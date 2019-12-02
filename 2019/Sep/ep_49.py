import itertools

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

def main():
    for n in range(1000, 10000):
        p_list = list(set(list(itertools.permutations(str(n)))))
        num_primes = 0
        results = []
        for pn in p_list:
            num = int(''.join(pn))
            if num < 1000:
                continue
            if isprime(num):
                results.append(num)
                num_primes += 1
        if len(results) >= 3:
            check_results(results)

def check_results(results):
    for n in sorted(results):
        if n+3330 in results and n+6660 in results:
            print(f"{n}{n+3330}{n+6660}")

if __name__ == "__main__":
    main()
