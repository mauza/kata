import sys
i = 1

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [[int(x.replace('\n', '')) for x in i.split(',')] for i in f.readlines()]
    return result[0]


def handle_op_code(c):
    c = "00000" + str(c)
    p = [int(c[-2:]), int(c[-3]), int(c[-4]), int(c[-5])]
    return p


def main():
    pos = 0
    t = file_as_list('input.txt')
    while pos < len(t):
        r = handle_op_code(t[pos])
        if r[0] == 99:
            break
        opp_code = r[0]
        if opp_code == 1:
            if r[1] == 1:
                v1 = t[pos + 1]
            else:
                v1 = t[t[pos + 1]]
            if r[2] == 1:
                v2 = t[pos + 2]
            else:
                v2 = t[t[pos + 2]]
            t[t[pos+3]] = v1 + v2
            pos += 4
            continue
        if opp_code == 2:
            if r[1] == 1:
                v1 = t[pos + 1]
            else:
                v1 = t[t[pos + 1]]
            if r[2] == 1:
                v2 = t[pos + 2]
            else:
                v2 = t[t[pos + 2]]
            t[t[pos+3]] = v1 * v2
            pos += 4
            continue
        if opp_code == 3:
            t[t[pos + 1]] = i
            pos += 2
            continue
        if opp_code == 4:
            print(t[pos + 1])
            pos += 2
            continue
        print(t)
        return


def test():
    t = file_as_list('input.txt')
    print(f"{t[225]}  +  {t[6]}")


if __name__ == "__main__":
    #test()
    main()
