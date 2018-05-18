from itertools import permutations

s = ['0','1','2','3','4','5','6','7','8','9']

perms = permutations(s, 10)
print(''.join(list(perms)[999999]))