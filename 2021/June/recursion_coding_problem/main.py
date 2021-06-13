import random
import datetime

CUSTOMER_NUM = 0
max_time = 60*8


def convert_time(int_time):
    hours = int(int_time/60)
    minutes = int_time % 60
    return f"{hours}:{minutes}"


def get_available_stylist(stylists):
    for s in stylists:
        if s.available:
            yield s


def check_for_done_stylists(stylists, time):
    for s in stylists:
        s.check_done(time)

def check_long_waiting_customers(waiting_queue, time):
    customers_to_remove = []
    for c in waiting_queue:
        if time - c.arrive_time > 10:
            print(f"{time} {c} left unfulfilled")
            customers_to_remove.append(c)
    for c in customers_to_remove:
        waiting_queue.remove(c)


class Stylist():

    def __init__(self):
        self.available = True
        self.start_time = None

    def give_haircut(self, customer, time):
        self.available = False
        self.haircut_customer = customer
        self.start_time = time

    def check_done(self, time):
        if self.start_time and time - self.start_time >= 30:
            print(f"{time} {self.haircut_customer} left satisfied")
            self.available = True
            self.start_time = None


class Customer():

    def __init__(self, time):
        global CUSTOMER_NUM
        self.customer_name = f"Customer-{CUSTOMER_NUM}"
        CUSTOMER_NUM += 1
        self.arrive_time = time
        self.satisfied = True

    def __str__(self):
        return self.customer_name

def main():
    time = 0
    print(f"{time} Hair salon opened")
    stylists = [Stylist() for i in range(4)]
    waiting_room = []

    for t in range(1, max_time+1):
        time += 1
        if random.random() * 10 <= 1:
            c = Customer(time)
            print(f"{time} {c} entered")
            if len(waiting_room) >= 10:
                print(f"{time} {c} left impatiently")
            else:
                waiting_room.append(c)
        for s in get_available_stylist(stylists):
            try:
                customer = waiting_room.pop(0)
            except IndexError:
                break
            s.give_haircut(customer, time)
        check_long_waiting_customers(waiting_room, time)
        check_for_done_stylists(stylists, time)
    while len(list(get_available_stylist(stylists))) != len(stylists):
        time += 1
        check_for_done_stylists(stylists, time)

    for c in waiting_room:
        print(f"{time} {c} left furious")



    print(f"{time} Hair salon closed")



if __name__ == "__main__":
    main()