

class board():
    layout = []

    def init(self):
        self.layout = [['-','-','-'],['-','-','-'],['-','-','-']]

    def drawboard(self):
        for row in self.layout:
            print("|".join(row))

    def add_token(self, x, y, token):
        self.layout[x][y] = token

    def check_full(self):
        for row in self.layout:
            for pos in row:
                if pos == "-":
                    return False
        return True

    def AI_move(self):
        for y in range(3):
            for x in range(3):
                if self.layout[x][y] == "-":
                    self.add_token(x,y,"O")
                    return True
        raise Exception("AI couldn't move")



test = board()
test.init()

while True:
    test.drawboard()
    print("Your Turn")
    x_y = input("please enter x and y seperated by a comma EI 1,0 ")
    try:
        temp = x_y.split(',')
        x = int(temp[0])
        y = int(temp[1])
    except:
        print("invalid input")
        continue

    test.add_token(x,y, "X")
    test.AI_move()


