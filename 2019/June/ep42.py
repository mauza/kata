
def tri_num(n):
    return 0.5*n*(n+1)

def is_tri_num(n):
    x = 1
    while True:
        tri_n = tri_num(x)
        if n == tri_n:
            return True
        if tri_n > n:
            return False
        x += 1

def get_word_value(word):
    total_val = 0
    for c in word:
        total_val += (ord(c) - 64)
    return total_val

def get_word_list():
    with open('words.txt', 'r') as f:
        contents = f.read()
    return [s.replace('"','') for s in contents.split(',')]

def main():
    total_tri_nums = 0
    for word in get_word_list():
        if is_tri_num(get_word_value(word)):
            total_tri_nums += 1
    print(total_tri_nums)

if __name__ == "__main__":
    main()