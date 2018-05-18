

# we will need a is prime function
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


# we need a function that yeilds all numbers with given repeat digits
def repeatdigits(length, digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    del digits[digit]
    digitnumber = [str(digit) for x in range(length)]
    if digit == 0:
        for d1 in digits:
            for d2 in digits:
                temp = digitnumber[:]
                temp[0] = d1
                temp[-1] = d2
                yield int(''.join(temp))
    elif digit == 2 or digit == 8:
        for place1 in range(len(digitnumber)):
            for d1 in digits:
                for place2 in range(1, len(digitnumber)):
                    for d2 in digits:
                        temp = digitnumber[:]
                        temp[place1] = d1
                        temp[place2] = d2
                        yield int(''.join(temp))
    else:
        for place in range(len(digitnumber)):
            for d in digits:
                temp = digitnumber[:]
                temp[place] = d
                result = int(''.join(temp))
                if result > 10**(length - 1):
                    yield result


# primes = [num for num in repeatdigits(4, 0)]

primes = []

for i in range(10):
    for num in repeatdigits(10, i):
        if isprime(num) and num > 1000000000:
            primes.append(num)

print(primes)
print(len(primes))
print(len(set(primes)))
print(sum(set(primes)))
