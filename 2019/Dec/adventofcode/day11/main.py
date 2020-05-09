from lib import program

class paint_robot():

    white_panels = []
    directions = ['u', 'r', 'd', 'l']
    direction_facing = 0
    robot_position = (0,0)
    painted = []

    def __init__(self, p):
        self.p = p

    def run_step(self):
        #print(f"{self.robot_position} going in {self.directions[self.direction_facing]}")
        output1 = self.get_output()
        #print(f"color output for position {self.robot_position} is {output}")
        self.handle_painting(output1)
        output2 = self.get_output()
        #print(f"direction output is {output}")
        print(f"{output1} - {output2} - {self.robot_position}")
        self.handle_turn(output2)
        self.move()

    def handle_painting(self, output):
        if output == 1:
            self.white_panels.append(self.robot_position)
        elif output == 0:
            self.white_panels.remove(self.robot_position)
        self.painted.append(self.robot_position)

    def get_output(self):
        output = None
        while not output:
            output = self.p.run()
            if not output:
                raise Exception("finished maybe?")
            if output == "input needed":
                self.input_color()
                output = None
        return output

    def input_color(self):
        if self.robot_position in self.white_panels:
            self.p.add_input(1)
        else:
            self.p.add_input(0)

    def move(self):
        if self.directions[self.direction_facing] == 'u':
            self.robot_position = (self.robot_position[0], self.robot_position[1] + 1)
        elif self.directions[self.direction_facing] == 'r':
            self.robot_position = (self.robot_position[0] + 1, self.robot_position[1])
        elif self.directions[self.direction_facing] == 'd':
            self.robot_position = (self.robot_position[0], self.robot_position[1] - 1)
        elif self.directions[self.direction_facing] == 'l':
            self.robot_position = (self.robot_position[0] - 1, self.robot_position[1])

    def handle_turn(self, output):
        if output == 0:
            self.direction_facing = self.direction_facing - 1
            if self.direction_facing < 0:
                self.direction_facing = 3
        elif output == 1:
            self.direction_facing = self.direction_facing + 1
            if self.direction_facing > 3:
                self.direction_facing = 0

    def run(self):
        while True:
            try:
                self.run_step()
            except Exception as e:
                print(e)
                return


def main():
    p = program.from_file('input.txt', [])
    robot = paint_robot(p)
    robot.run()
    print(len(robot.painted))
    print(set(robot.painted))

if __name__ == "__main__":
    main()
