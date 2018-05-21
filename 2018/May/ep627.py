import itertools
import functools
import operator

def product(nums):
    return functools.reduce(operator.mul, nums, 1)

def prob(m, n):
    list_m = list(range(1,m+1))
    l = itertools.combinations_with_replacement(list_m, n)
    #products = [product(n) for n in l]
    return len(set(l))

print(prob(30,9))