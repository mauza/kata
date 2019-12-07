
def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [i.replace('\n', '') for i in f.readlines()]
    return result


def main():
    s = file_as_list('input.txt')
    r = get_object_set(s)
    you_set = get_orbit_list('YOU', s)
    san_set = get_orbit_list('SAN', s)
    for i in san_set:
        for j in you_set:
            if i == j:
                print(i)
                print(you_set.index(i))
                print(san_set.index(j))
                return




def get_orbits(obj, i):
    direct = 0
    indirect = 0
    for o in i:
        other_o = o.split(')')
        if obj == other_o[1]:
            direct +=1
            indirect =  get_orbits(other_o[0], i)
            break
    return direct + indirect

def get_orbit_list(obj, i):
    result = []
    for o in i:
        other_o = o.split(')')
        if obj == other_o[1]:
            result.append(other_o[0])
            result += get_orbit_list(other_o[0], i)
    return result

def get_object_set(l):
    r = set()
    for o in l:
        t = o.split(')')
        r.add(t[0])
        r.add(t[1])
    return r


def test():
    s = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
    r = get_object_set(s)
    total = 0
    for t in r:
        total += get_orbits(t, s)
    print(total)


if __name__ == "__main__":
    main()
    #test()
