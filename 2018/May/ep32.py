import itertools

nums = '123456789'

num_perms = itertools.permutations(nums)

results = set()

for perm in num_perms:
    p = ''.join(perm)
    for i in range(1,7):
        a = int(p[:i])
        for j in range(1,7-i):
            b = int(p[i:i+j])
            c = int(p[i+j:])
            if a*b == c:
                results.add(c)

print(sum(results))