from lib import program

def main():
    s = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
    i = 5
    #p = program.from_string(s, i)
    p = program.from_file('input.txt', i)
    p.run()


if __name__ == "__main__":
    main()
