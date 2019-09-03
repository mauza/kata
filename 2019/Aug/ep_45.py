import math

def quadratic_solver(a,b,c):
    d = b**2-4*a*c # discriminant

    if d < 0:
        return []
    elif d == 0:
        return [(-b + math.sqrt(d)) / (2 * a)]
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return [x1, x2]


def is_t_num(n):
    solutions = quadratic_solver(0.5, 0.5, -n)
    for x in solutions:
        if x.is_integer() and x > 0:
            return True

def is_p_num(n):
    solutions = quadratic_solver(1.5, -0.5, -n)
    for x in solutions:
        if x.is_integer() and x > 0:
            return True

def is_h_num(n):
    solutions = quadratic_solver(2, -1, -n)
    for x in solutions:
        if x.is_integer() and x > 0:
            return True


def main():
    for x in range(1, 1000000000):
        if is_t_num(x) and is_p_num(x) and is_h_num(x):
            print(f"We have a winner: {x}")

def test():
    print(is_t_num(40755))
    print(is_p_num(40755))
    print(is_h_num(40755))

def try2():
    for n in range(1, 10000000):
        tri_n = n*(n+1)/2
        if is_p_num(tri_n) and is_h_num(tri_n):
            print(f"we have a winner: {n}|{tri_n}")

if __name__ == "__main__":
    try2()
