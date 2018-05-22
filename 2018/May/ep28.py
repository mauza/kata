import numpy as np

def spiral_ccw(A):
    A = np.array(A)
    out = []
    while(A.size):
        out.append(A[0][::-1])    # first row reversed
        A = A[1:][::-1].T         # cut off first row and rotate clockwise
    return np.concatenate(out)

def base_spiral(nrow, ncol):
    return spiral_ccw(np.arange(nrow*ncol).reshape(nrow,ncol))[::-1]

def to_spiral(A):
    A = np.array(A)
    B = np.empty_like(A)
    B.flat[base_spiral(*A.shape)] = A.flat
    return B

B = np.arange(1,1002002).reshape(1001,1001)
s = to_spiral(B)

total = 0
for x in range(1001):
    total += s[x][x]

for i in range(1001):
    total += s[i][abs(i-1000)]

print(total-1)