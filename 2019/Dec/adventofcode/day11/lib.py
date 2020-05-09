
class program():

    code = []
    pos = 0
    input_val = None
    debug = False
    halted = False
    relative_base = 0

    opp_code_mapping = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 2,
    }

    @staticmethod
    def from_file(filename, input_val, debug=False):
        with open(filename, 'r') as f:
            code = [int(s.strip()) for s in f.read().split(',')]
        return program(code, input_val, debug)

    @staticmethod
    def from_string(code_string, input_val):
        code = [int(s) for s in code_string.split(',')]
        return program(code, input_val)

    def __init__(self, code, input_val, debug=False):
        self.code = code
        self.input_val = input_val
        self.debug = debug

    def get_current_oppcode(self):
        raw_oppcode = self.get_value_at_location(self.pos)
        if self.debug:
            print(f"position: {self.pos} -> value: {raw_oppcode}")
        return raw_oppcode

    def handle_raw_oppcode(self, raw_oppcode):
        c = "00000" + str(raw_oppcode)
        oppcode = int(c[-2:])
        position_codes = [int(c[-3]), int(c[-4]), int(c[-5])]
        if self.debug:
            print(f"{oppcode} - {position_codes}")
        return oppcode, position_codes

    def get_position_params(self, position_codes, oppcode):
        results = []
        num_params = self.opp_code_mapping[oppcode] - 1
        for i in range(num_params):
            if position_codes[i] == 0:
                value = self.get_value_at_location(self.pos + i + 1)
            elif position_codes[i] == 1:
                value = self.pos + i + 1
            elif position_codes[i] == 2:
                value = self.get_value_at_location(self.pos + i + 1) + self.relative_base
            results.append(value)
        return results

    def add_input(self, _input):
        self.input_val.append(_input)

    def set_value_at_location(self, position, value):
        code_length = len(self.code)
        if code_length < position:
            self.code += [0]*(position - code_length + 2)
        if self.debug:
            print(f"code_length: {code_length} - position: {position}")
        self.code[position] = value

    def get_value_at_location(self, position):
        code_length = len(self.code)
        if code_length < position:
            self.code += [0]*(position - code_length + 2)
        value = self.code[position]
        if self.debug:
            print(f"Got value: {value} at position: {position}")
        return value

    def process_next_instruction(self):
        output = None
        oppcode, position_codes = self.handle_raw_oppcode(self.get_current_oppcode())
        if oppcode == 99:
            self.halted = True
            return
        positions = self.get_position_params(position_codes, oppcode)
        if oppcode == 1:
            self.set_value_at_location(positions[2], self.get_value_at_location(positions[0]) + self.get_value_at_location(positions[1]))
        if oppcode == 2:
            self.set_value_at_location(positions[2], self.get_value_at_location(positions[0]) * self.get_value_at_location(positions[1]))
        if oppcode == 3:
            if len(self.input_val) == 0:
                return "input needed"
            self.set_value_at_location(positions[0], self.input_val.pop(0))
        if oppcode == 4:
            output = self.get_value_at_location(positions[0])
            if self.debug:
                print(f"output: {output}")
        if oppcode == 5:
            if self.get_value_at_location(positions[0]) != 0:
                self.pos = self.get_value_at_location(positions[1])
                return
        if oppcode == 6:
            if self.get_value_at_location(positions[0]) == 0:
                self.pos = self.get_value_at_location(positions[1])
                return
        if oppcode == 7:
            if self.get_value_at_location(positions[0]) < self.get_value_at_location(positions[1]):
                self.set_value_at_location(positions[2], 1)
            else:
                self.set_value_at_location(positions[2], 0)
        if oppcode == 8:
            if self.get_value_at_location(positions[0]) == self.get_value_at_location(positions[1]):
                self.set_value_at_location(positions[2], 1)
            else:
                self.set_value_at_location(positions[2], 0)
        if oppcode == 9:
            self.relative_base += self.get_value_at_location(positions[0])
        self.pos += self.opp_code_mapping[oppcode]
        return output

    def run(self):
        while not self.halted:
            if self.debug:
                #print(self.code)
                print(self.input_val)
                print(self.relative_base)
            output = self.process_next_instruction()
            if output:
                return output
                print(f"Output: {output}")


