from itertools import permutations

def gen_pandigitals(num_digits):
    if num_digits > 10 or num_digits < 1:
        raise Exception("You entered a bad digit")
    digits = list(range(0,num_digits))
    for perm in permutations(digits):
        yield list(map(str, perm))

def check_pan_num(digits):
    if len(digits) != 10:
        return False
    if int(digits[1]+digits[2]+digits[3]) % 2 != 0:
        return False
    if int(digits[2]+digits[3]+digits[4]) % 3 != 0:
        return False
    if int(digits[3]+digits[4]+digits[5]) % 5 != 0:
        return False
    if int(digits[4]+digits[5]+digits[6]) % 7 != 0:
        return False
    if int(digits[5]+digits[6]+digits[7]) % 11 != 0:
        return False
    if int(digits[6]+digits[7]+digits[8]) % 13 != 0:
        return False
    if int(digits[7]+digits[8]+digits[9]) % 17 != 0:
        return False
    return True

def main():
    result_list = []
    for digits in gen_pandigitals(10):
        if check_pan_num(digits):
            result_list.append(int("".join(digits)))
    print(sum(result_list))

if __name__ == "__main__":
    main()