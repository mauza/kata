import math

def carParkingRoof(cars, k):
    sorted_cars = sorted(cars)
    num_cars = len(sorted_cars)
    spread = k-1
    min_length = sorted_cars[-1] - sorted_cars[0]
    for i in range(num_cars - spread):
        print(sorted_cars[i + spread])
        print(sorted_cars[i])
        roof_length = sorted_cars[i + spread] - sorted_cars[i]
        if min_length > roof_length:
            min_length = roof_length
    return min_length

if __name__ == "__main__":
    cars = [2,6,7,12]
    k = 3
    print(carParkingRoof(cars, k))