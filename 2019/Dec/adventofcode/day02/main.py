

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [int(i.replace('\n', '')) for i in f.read().split(',')]
    return result

def process(i):
    offset = 0
    while offset < len(i):
        code = i[offset]
        if code == 99:
            return i
        pos1 = i[offset+1]
        pos2 = i[offset+2]
        result = i[offset+3]
        i[result] = run_code(code, i[pos1], i[pos2])
        offset += 4

def run_code(code, num1, num2):
    if code == 1:
        return num1 + num2
    elif code ==2:
        return num1 * num2

def main():
    for i in range(1, 100):
        for j in range(1, 100):
            s = file_as_list('input.txt')
            s[1] = i
            s[2] = j
            result = process(s)
            if result[0] == 19690720:
                print(f"{i}   {j}")

def test():
    t = [1,9,10,3,2,3,11,0,99,30,40,50]
    result = process(t)
    print(result)


if __name__ == "__main__":
    main()
    #test()
