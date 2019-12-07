import time
import sys
import os
i = 8000

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [[int(x.replace('\n', '')) for x in i.split(',')] for i in f.readlines()]
    return result[0]


def handle_op_code(c, debug):
    c = "00000" + str(c)
    p = [int(c[-2:]), int(c[-3]), int(c[-4]), int(c[-5])]
    if debug:
        print(f'{p[0]} - {p[1]}{p[2]}{p[3]}')
    return p


def main(debug=False):
    pos = 0
    #t = file_as_list('input.txt')
    t = [int(s) for s in '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'.split(',')]
    if debug:
        print(t)
    while pos < len(t):
        r = handle_op_code(t[pos], debug)
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
            v3 = t[pos+3]
            t[v3] = v1 + v2
            if debug:
                print(f"{v3} -> {t[v3]}")
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
            v3 = t[pos+3]
            t[v3] = v1 * v2
            if debug:
                print(f"{v3} -> {t[v3]}")
            pos += 4
            continue
        if opp_code == 3:
            v1 = t[pos + 1]
            t[v1] = i
            if debug:
                print(f"{v1} -> {t[v1]}")
            pos += 2
            continue
        if opp_code == 4:
            if r[1] == 1:
                v1 = t[pos + 1]
            else:
                v1 = t[t[pos + 1]]
            print(f"output: {v1}")
            pos += 2
            continue
        if opp_code == 5:
            if r[1] == 1:
                v1 = t[pos + 1]
            else:
                v1 = t[t[pos + 1]]
            if r[2] == 1:
                v2 = t[pos + 2]
            else:
                v2 = t[t[pos + 2]]
            if v1 != 0:
                pos = v2
            else:
                pos += 3
            if debug:
                print(f" -> {pos}")
            continue
        if opp_code == 6:
            if r[1] == 1:
                v1 = t[pos + 1]
            else:
                v1 = t[t[pos + 1]]
            if r[2] == 1:
                v2 = t[pos + 2]
            else:
                v2 = t[t[pos + 2]]
            if v1 == 0:
                pos = v2
            else:
                pos += 3
            if debug:
                print(f" -> {pos}")
            continue
        if opp_code == 7:
            if r[1] == 1:
                v1 = t[pos + 1]
            else:
                v1 = t[t[pos + 1]]
            if r[2] == 1:
                v2 = t[pos + 2]
            else:
                v2 = t[t[pos + 2]]
            if v1 < v2:
                t[pos+3] = 1
            else:
                t[pos+3] = 0
            if debug:
                print(f"{pos+3} -> {t[pos+3]}")
            pos += 4
            continue
        if opp_code == 8:
            if r[1] == 1:
                v1 = t[pos + 1]
            else:
                v1 = t[t[pos + 1]]
            if r[2] == 1:
                v2 = t[pos + 2]
            else:
                v2 = t[t[pos + 2]]
            if v1 == v2:
                t[pos+3] = 1
            else:
                t[pos+3] = 0
            if debug:
                print(f"{pos+3} -> {t[pos+3]}")
            pos += 4
            continue
        print(t)
        return


def test(a):
    t = file_as_list('input.txt')
    print(f"{t[int(a)]}")


if __name__ == "__main__":
    try:
        a = sys.argv[1]
    except:
        a = None
    if a:
        test(a)
    else:
        main(True)
