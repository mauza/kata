import time
import sys
import os
i = 1

opp_code_mapping = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
}

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [[int(x.replace('\n', '')) for x in i.split(',')] for i in f.readlines()]
    return result[0]


def handle_op_code(c):
    c = "00000" + str(c)
    p = [int(c[-2:]), int(c[-3]), int(c[-4]), int(c[-5])]
    #print(f'{p[0]} - {p[1]}{p[2]}{p[3]}')
    return p

def get_values(program_list, pos, code_list):
    num_params = opp_code_mapping[code_list[0]] - 1
    results = []
    for i in range(1, num_params):
        if code_list[i]:
            results.append(program_list[pos + i])
        else:
            results.append(program_list[program_list[pos + i]])
    results.append(program_list[pos+num_params])
    return results


def process(program_list, pos, code_list):
    opp_code = code_list[0]
    print(f"opp_code: {opp_code}")
    values = get_values(program_list, pos, code_list)
    print(values)
    if opp_code == 1:
        program_list[values[-1]] = values[0] + values[1]
    if opp_code == 2:
        program_list[values[-1]] = values[0] * values[1]
    if opp_code == 3:
        program_list[values[0]] = i
    if opp_code == 4:
        print(f"output: {values[0]}")
    if opp_code == 5:
        if values[0] != 0:
            pos = values[1]
            return program_list, pos
    if opp_code == 6:
        if values[0] == 0:
            pos = values[1]
            return program_list, pos
    if opp_code == 7:
        if values[0] < values[1]:
            program_list[values[-1]] = 1
        else:
            program_list[values[-1]] = 0
    if opp_code == 8:
        if values[0] == values[1]:
            program_list[values[-1]] = 1
        else:
            program_list[values[-1]] = 0
    pos += opp_code_mapping[opp_code]
    return program_list, pos



def main():
    pos = 0
    t = file_as_list('input.txt')
    #t = [int(s) for s in '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'.split(',')]
    print(t)
    while True:
        print(f"position: {pos}")
        r = handle_op_code(t[pos])
        if r[0] == 99:
            break
        t, pos = process(t, pos, r)


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
        main()
