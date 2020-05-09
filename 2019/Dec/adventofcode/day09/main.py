from lib import program

f = "input.txt"

def main():
    p = program.from_file(f, [2])
    output = p.run()
    print(output)

def test():
    p = program.from_file(f, [1], debug=True)
    output = p.run()
    print(output)


if __name__ == "__main__":
    #test()
    main()
