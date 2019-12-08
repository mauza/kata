from itertools import permutations

from lib import program

f = 'input.txt'
initial_input = 0

def run_amps(amp_list, i):
    amp_list[0].add_input(i)
    output = amp_list[0].run()
    if not output:
        return
    for amp in amp_list[1:]:
        amp.add_input(output)
        output = amp.run()
        if not output:
            return
    return output

def run_loop_phase_setting(setting):
    amplifiers = [program.from_file(f, [s]) for s in setting]
    output = run_amps(amplifiers, initial_input)
    last_output = output
    if not output:
        for a in amplifiers:
            print(f"{a.input_val}")
    while output:
        last_output = output
        output = run_amps(amplifiers, output)
    return last_output


def main():
    phase_settings = permutations([5,6,7,8,9])
    max_thrust = 0
    for setting in phase_settings:
        output = run_loop_phase_setting(setting)
        if output and output > max_thrust:
            max_thrust = output
            print(f"New max thrust: {max_thrust} with {setting} settings")
    print(f"Final Output = {max_thrust}")

def test():
    setting = [4,3,2,1,0]
    amplifiers = [program.from_file(f, [s]) for s in setting]
    output = run_amps(amplifiers, initial_input)
    #output = run_loop_phase_setting([9,8,7,6,5])
    print(output)

if __name__ == "__main__":
    #test()
    main()
