from decimal import *
getcontext().prec = 28

one = Decimal('1.0')
for i in range(2,1000):
    some = one/Decimal(i)
    