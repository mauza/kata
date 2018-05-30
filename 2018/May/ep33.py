from fractions import Fraction

def is_curious(nom, den):
    n = str(nom)
    d = str(den)
    for i in range(2):
        for j in range(2):
            tmp_n = int(n[:i] + n[i+1:])
            tmp_d = int(d[:j] + d[j+1:])
            if nom/den == tmp_n/tmp_d and d[j] == n[i]:
                return True
    return False

l = []

for n in range(11, 100):
    if n%10 == 0:
        continue
    for d in range(11, 100):
        if d%10 == 0 or n >= d:
            continue
        if is_curious(n,d):
            l.append([n,d])

n = 1
d = 1
for f in l:
    n = n*f[0]
    d = d*f[1]
print(Fraction(n,d))