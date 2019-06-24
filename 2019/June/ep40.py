

def get_digit_at(digit_place):
    digits = 0
    n = 1
    while digits < digit_place:
        digits += len(str(n))
        if digits >= digit_place:
            digit = int(str(n)[-(digits-digit_place + 1)])
            print(f"{digits} - {digit_place} - {n} - {digit}")
            return digit
        n += 1

def main():
    # digit_num = get_digit_at(12)
    # print(f"{digit_num}")
    # print(f"{get_digit_at(998)}")
    ans = 1*1*5*get_digit_at(1000)*get_digit_at(10000)*get_digit_at(100000)*get_digit_at(1000000)
    print(ans)


if __name__ == "__main__":
    main()
