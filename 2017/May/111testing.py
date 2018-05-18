def repeatdigits(length, digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    del digits[digit]
    digitnumber = [str(digit) for x in range(length)]
    numbers = []
    for place in range(len(digitnumber)):
        for d in digits:
            temp = digitnumber[:]
            temp[place] = d
            result = int(''.join(temp))
            if result > 10**length:
                numbers.append(result)
    return(numbers)

print(repeatdigits(4, 1))
