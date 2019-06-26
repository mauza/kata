

def pent_num(n):
    return 0.5*n*(3*n-1)

def is_pent_num(n):
    x = 1
    while True:
        pent_n = pent_num(x)
        if n == pent_n:
            return True
        if pent_n > n:
            return False
        x += 1

def gen_pent_pairs(limit):
    for a in range(1, limit+1):

def main():
    

if __name__ == "__main__":
    main()