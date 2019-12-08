
class program():

    code = []
    input_val = None
    pos = 0
    debug = False

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

    @staticmethod
    def from_file(filename, input_val):
        with open(filename, 'r') as f:
            code = [int(s.strip()) for s in f.read().split(',')]
        return program(code, input_val)

    @staticmethod
    def from_string(code_string, input_val):
        code = [int(s) for s in code_string.split(',')]
        return program(code, input_val)

    def __init__(self, code, input_val):
        self.code = code
        self.input_val = input_val

    def get_current_oppcode(self):
        return self.code[self.pos]

    def handle_raw_oppcode(self, raw_oppcode):
        c = "00000" + str(raw_oppcode)
        oppcode = int(c[-2:])
        position_codes = [int(c[-3]), int(c[-4]), int(c[-5])]
        if self.debug:
            print(f"{oppcode} - {position_codes}")
        return oppcode, position_codes

    def get_position_params(self, position_codes):
        results = []
        for i in range(3):
            value = self.code[self.pos + i + 1] if position_codes[i] == 0 else (self.pos + i + 1)
            results.append(value)
        return results


    def process_next_instruction(self):
        oppcode, position_codes = self.handle_raw_oppcode(self.get_current_oppcode())
        positions = self.get_position_params(position_codes)
        if self.debug:
            print(positions)
        if oppcode == 99:
            raise Exception('ProgramEnd')
        if oppcode == 1:
            self.code[positions[2]] = self.code[positions[0]] + self.code[positions[1]]
        if oppcode == 2:
            self.code[positions[2]] = self.code[positions[0]] * self.code[positions[1]]
        if oppcode == 3:
            self.code[positions[0]] = self.input_val
        if oppcode == 4:
            output = self.code[positions[0]]
            print(f"output: {output}")
            return output
        if oppcode == 5:
            if self.code[positions[0]] != 0:
                self.pos = self.code[positions[1]]
                return
        if oppcode == 6:
            if self.code[positions[0]] == 0:
                self.pos = self.code[positions[1]]
                return
        if oppcode == 7:
            if self.code[positions[0]] < self.code[positions[1]]:
                self.code[positions[2]] = 1
            else:
                self.code[positions[2]] = 0
        if oppcode == 8:
            if self.code[positions[0]] == self.code[positions[1]]:
                self.code[positions[2]] = 1
            else:
                self.code[positions[2]] = 0
        self.pos += self.opp_code_mapping[oppcode]

    def run(self):
        while self.pos < len(self.code):
            if self.debug:
                print(self.code)
            try:
                output = self.process_next_instruction()
            except Exception as e:
                print(self.pos)
                print(e)
                return
            if output:
                print(output)
                return output


