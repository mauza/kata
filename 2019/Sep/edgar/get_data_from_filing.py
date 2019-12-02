from bs4 import BeautifulSoup

filename = "data/0000712515/10-q/0000712515-14-000063.txt"

def main():
    with open(filename, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    print(soup)


if __name__ == "__main__":
    main()
