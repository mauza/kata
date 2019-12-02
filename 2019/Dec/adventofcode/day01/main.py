import math

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [i.replace('\n', '') for i in f.readlines()]
    return result

def get_fuel_amt(mass):
    result = math.floor(mass/3) - 2
    if result <=0:
        return 0
    return result

def get_total_amt(mass):
    total = 0
    current_extra = mass
    while current_extra > 0:
        current_extra = get_fuel_amt(current_extra)
        total += current_extra
    return total


def main():
    l = file_as_list('input.txt')
    print(sum([get_total_amt(int(i.replace('\n', ''))) for i in l]))

def test():
    get_total_amt(100756)


if __name__ == "__main__":
    main()
