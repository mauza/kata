# import itertools

# currency = [1,2,5,10,20,50,100,200]

# # combs = itertools.combinations_with_replacement(currency, 200)

# # result = [a for a in combs if sum(a) == 200]

# combinations = []

# current_list = []
# for c1 in currency:
#     for c2 in currency:
#         while sum(current_list) < 200:
#             current_list.append(c1)

import time
import random

currency = [1,2,5,10,20,50,100,200]
start = time.time()

results = set()

while time.time() - start < 6000:
    tmp = []
    while sum(tmp) < 200:
        tmp.append(random.choice(currency))
    if sum(tmp) == 200:
        results.add(''.join([str(t) for t in sorted(tmp)]))

print(len(results))