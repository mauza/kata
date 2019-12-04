import math

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [[x.replace('\n', '') for x in i.split(',')] for i in f.readlines()]
    return result

def file_as_list2(filename):
    with open(filename, 'r') as f:
        result = [i.replace('\n', '') for i in f.readlines()]
    return result

def process(list_in):
    coords = (0,0)
    all_coords = []
    for direction in list_in:
        coords_list = process_direction(direction, coords)
        coords = coords_list[-1]
        all_coords += coords_list
    return all_coords


def process_direction(d, coords):
    if d[0] == "R":
        result_x = coords[0]+ int(d[1:])
        result_y = coords[1]
        return [(x, result_y) for x in range(coords[0]+1, result_x + 1)]
    if d[0] == "U":
        result_y = coords[1]+ int(d[1:])
        result_x = coords[0]
        return [(result_x, y) for y in range(coords[1]+1, result_y + 1)]
    if d[0] == "L":
        result_x = coords[0]- int(d[1:])
        result_y = coords[1]
        return [(x, result_y) for x in range(coords[0]-1, result_x-1, -1)]
    if d[0] == "D":
        result_y = coords[1]- int(d[1:])
        result_x = coords[0]
        return [(result_x, y) for y in range(coords[1]-1, result_y-1, -1)]

def get_distance(coord):
    return abs(coord[0]) + abs(coord[1])

def main():
    f = file_as_list('input.txt')
    r1 = process(f[0])
    r2 = process(f[1])
    result = set(r1).intersection(set(r2))
    t = s(r1, r2, result)
    print(t)

def process_results(r1, r2):
    r1 = r1[1:]
    r2 = r2[1:]
    result = set(r1).intersection(set(r2))
    min_r = None
    min_d = 1000000000
    for r in result:
        d = get_distance(r)
        if d < min_d:
            min_d = d
            min_r = r
    return min_r


def s(r1, r2, inters):
    min_steps = 100000000
    for i in inters:
        s1 = r1.index(i) + 1
        s2 = r2.index(i) + 1
        tmp_steps = s1+s2
        if tmp_steps < min_steps:
            min_steps = tmp_steps
    return min_steps


def test():
    s1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    s2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
    f1 = s1.split(',')
    f2 = s2.split(',')
    r1 = process(f1)
    r2 = process(f2)
    result = set(r1).intersection(set(r2))
    t = s(r1, r2, result)
    print(t)


if __name__ == "__main__":
    main()
    #test()
