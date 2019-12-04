

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [[x.replace('\n', '') for x in i.split(',')] for i in f.readlines()]
    return result


def file_as_list2(filename):
    with open(filename, 'r') as f:
        result = [i.replace('\n', '') for i in f.readlines()]
    return result


def password_meets_crit(p):
    if p_contains_double(p) and p_ascending(p):
        return True
    return False


def p_contains_double(p):
    counter = 1
    last_d = p[0]
    for d in p[1:]:
        if last_d == d:
            counter += 1
        else:
            if counter == 2:
                return True
            counter = 1
        last_d = d
    if counter == 2:
        return True
    return False


def p_ascending(p):
    last_d = p[0]
    for d in p[1:]:
        if int(last_d) > int(d):
            return False
        last_d = d
    return True


def main(s, e):
    total = 0
    for i in range(s, e+1):
       if password_meets_crit(str(i)):
           print(i)
           total += 1
    print(total)


def test():
    #print(password_meets_crit('123444'))
    #print(password_meets_crit('112233'))
    print(password_meets_crit('111122'))


if __name__ == "__main__":
    #test()
    main(197487, 673251)
