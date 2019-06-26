import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from itertools import combinations

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
    pent_list = list(map(pent_num, range(1,limit)))
    for c in combinations(pent_list, 2):
        yield c

def check_min_and_add(min_dict, pent_pair, D):
    if not min_dict or D < min_dict["min"]:
        result = {"pair": pent_pair, "min": D}
        print(result)
        return result
    return min_dict

def check_pent_pair(pent_pair):
    D = abs(pent_pair[0]-pent_pair[1])
    if is_pent_num(sum(pent_pair)) and is_pent_num(D):
        result = {"pair": pent_pair, "min": D}
        print(result)
        return result


def main():
    min_dict = None
    with ProcessPoolExecutor(max_workers=(mp.cpu_count())) as processpool:
        results = list(processpool.map(
            check_pent_pair,
            gen_pent_pairs(10000)
        ))
        for r in results:
            if r:
                min_dict = check_min_and_add(min_dict, r["pair"], r["min"])
        # for pent_pair in gen_pent_pairs(10000, 10000):
            # D = pent_check_condition(pent_pair)
            # if D:
            #     min_dict = check_min_and_add(min_dict, pent_pair, D)
    print(min_dict)

def test():
    for p in gen_pent_pairs(10):
        print(p)

if __name__ == "__main__":
    main()