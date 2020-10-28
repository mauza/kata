import random
import itertools

TESTS = [
    {
        'values': [1,2,3,4,2,6],
        'actual_max_score': 13
    },
    {
        'values': [1,2,3,4,5,4,3,2,1],
        'actual_max_score': 17
    },
]


def getMaximumScore(integerArray):
    score = 0
    # 1st iteration
    iteration = 1
    while len(integerArray) > 0:
        if iteration % 2 == 1:
            score += sum(integerArray)
        else:
            score -= sum(integerArray)
        if True:
            integerArray.pop(-1)
        else:
            integerArray.pop(0)
        iteration += 1
    return score


def run_tests(tests):
    for test in tests:
        test['score'] = run_test(test)
    print(tests)

def run_test(test):
    result = getMaximumScore(test['values'])
    return result

def generate_test():
    array_length = random.randint(6, 10**4)
    test_values = [random.randint(1, 10**4) for i in range(array_length)]
    return {
        'values': test_values,
        'best_guess': sum(sorted(test_values)[int(array_length/2):])
    }

def generate_random_try(list_length, is_one=True):
    right_side = random.randint(0,1) == 1
    if is_one:
        value = [1]
    else:
        value = [0]
    if list_length == 1:
        return value
    if right_side:
        return generate_random_try(list_length-1, not is_one) + value
    else:
        return value + generate_random_try(list_length-1, not is_one)

def group_values(t):
    values = []
    for i in range(0, int(len(t)/2), 2):
        value = sum(t[i:i+2]) + sum(t[-(i+3):-(i+1)])
        values.append(value)
    return values

def try_four_groups(list_length):
    random_try = generate_random_try(list_length)
    print(random_try)
    values = group_values(random_try)
    return values

def main():
    test = generate_test()
    print(test)
    result = run_test(test)
    print(result)

if __name__ ==  "__main__":
    print(try_four_groups(12))

