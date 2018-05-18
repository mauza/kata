import math

a = 1/60
b = 60
answers = []
for i in range (0,12):
    for j in range(0,12):
        x = (-60*j - i)/(a-b)
        hour = i
        minute = math.floor(x)
        second = ((x - minute)*60).as_integer_ratio()
        print("{}:{}:{}".format(hour,minute,second))