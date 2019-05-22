import random
import concurrent.futures as cf

class number_memory():
    def __init__(self, number):
        self.value = number
        self.age = 0
        self.time_since_called = 0

    def __eq__(self, rhs):
        if self.value == rhs.value:
            return True
        else:
            return False

def larry_function(memory_list):
    result_num = None
    for number in memory_list:
        if not result_num or number.time_since_called > result_num.time_since_called:
            result_num = number
    return result_num

def robin_function(memory_list):
    result_num = None
    for number in memory_list:
        if not result_num or number.age > result_num.age:
            result_num = number
    return result_num

class memory():

    def __init__(self, name, strat_function):
        self.name = name
        self.strategy = strat_function
        self.score = 0
        self.memory = []
    
    def take_turn(self, call_number):
        number_in_memory = False
        for number in self.memory:
            number.age += 1
            number.time_since_called += 1
            if number.value == call_number:
                self.score +=1
                number.time_since_called = 0
                number_in_memory = True
        if not number_in_memory:
            if len(self.memory) >= 5:
                self.memory.remove(self.strategy(self.memory))
            self.memory.append(number_memory(call_number))

def main():
    # larry = memory("Larry", larry_function)
    robin = memory("Robin", robin_function)
    for x in range(100000000):
        call_num = random.randint(1,11)
        # larry.take_turn(call_num)
        robin.take_turn(call_num)
        # if x%1000000 == 0:
        #     print(f"Turn: {x}\t Larry Score: {larry.score}\t Robin Score: {robin.score}")
    # print(f"Larry: {larry.score}")
    return robin.score

if __name__ == "__main__":
    with cf.ThreadPoolExecutor(101) as pool:
        jobs = []
        for x in range(100):
            jobs.append(pool.submit(main))
        results = [j.result() for j in jobs]
    print(results)
    print(sum(results))

# Larry
# 45454297
# 

# Robin:
# 45459651