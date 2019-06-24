from itertools import permutations

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

def gen_pandigitals(num_digits):
    if num_digits > 9 or num_digits < 1:
        raise Exception("You entered a bad digit")
    digits = list(range(1,num_digits+1))
    for perm in permutations(digits):
        yield int("".join(list(map(str, perm))))

def main():
    max_prime = 3
    for i in range(1,10):
        for perm in gen_pandigitals(i):
            if isprime(perm) and perm > max_prime:
                max_prime = perm
    print(max_prime)

if __name__ == "__main__":
    main()