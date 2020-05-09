from itertools import combinations, chain
import re
import pandas as pd

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = f.readlines()
    return result

def get_data():
    f = file_as_list('input.txt')
    result = [[int(d)for d in re.findall(r'[-]?\d+', moon)] for moon in f]
    return pd.DataFrame(result, columns=['x','y','z'])

def apply_gravity(m, mv):
    m.x#

    return mv

def apply_velocity(m, mv):
    for i in range(len(m)):
        m[i][0] += mv[i][0]
        m[i][1] += mv[i][1]
        m[i][2] += mv[i][2]
    return m

def get_total_energy(m, mv):
    total_energy = 0
    for i in range(len(m)):
        p_energy = sum(abs(value) for value in m[i])
        k_energy = sum(abs(value) for value in mv[i])
        total_energy += p_energy*k_energy
    return total_energy

def energy_after_steps(steps):
    moons = get_data()
    moons_velocity = [[0,0,0] for moon in moons]
    for step in range(steps):
        moons_velocity = apply_gravity(moons, moons_velocity)
        moons = apply_velocity(moons, moons_velocity)
    total_energy = get_total_energy(moons, moons_velocity)
    print(total_energy)

def serialize(moons):
    return ''.join([str(e) for e in chain.from_iterable(moons)])

def main():
    moons = get_data()
    moons_velocity = pd.DataFrame([[0,0,0] for _ in len(moons)], columns=['x','y','z'])
    states = set()
    states.add(serialize(moons))
    step = 0
    while True:
        step += 1
        moons_velocity = apply_gravity(moons, moons_velocity)
        moons = moons.add(moons_velocity)
        serialized_moons = serialize(moons)
        print(step)
        if serialized_moons in states:
            print(f"This one -> {step}")
            break
        states.add(serialized_moons)

if __name__ == "__main__":
    main()
