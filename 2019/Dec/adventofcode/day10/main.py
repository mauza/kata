import traceback
import os
import time
# Day 10

def clean_data(data):
    result = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 1:
                result.append((x,y))
    return result

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = [[1 if c == "#" else 0 for c in line] for line in f.readlines()]
    return clean_data(result)

f = "input.txt"
data = file_as_list(f)
angle = 90

def get_slope(point1, point2):
    try:
        slope = (point1[1] - point2[1])/(point1[0] - point2[0])
    except ZeroDivisionError:
        if (point1[1] - point2[1]) < 0:
            slope = -100000
        else:
            slope = 100000
    if slope == 0:
        if (point1[0] - point2[0]) < 0:
            slope = -0.0000001
        else:
            slope = 0.0000001
    return slope

def get_in_sight(point):
    slopes = {}
    total = 0
    for p in data:
        slope = get_slope(point, p)
        if slopes.get(slope) == None:
            slopes[slope] = [p]
        else:
            slopes[slope].append(p)
    #print(sorted(slopes.keys()))
    for slope, points in slopes.items():
        total += handle_slope_list(point, points)
    return total

def get_slopes(point):
    slopes = {}
    for p in data:
        slope = get_slope(point, p)
        if slopes.get(slope) == None:
            slopes[slope] = [p]
        else:
            slopes[slope].append(p)
    return sorted(slopes.keys()), slopes

def handle_slope_list(point, point_list):
    above = False
    below = False
    total = 0
    for p in point_list:
        if p[0] > point[0]:
            above = True
        if p[0] < point[0]:
            below = True
        if p[0] == point[0]:
            if p[1] > point[1]:
                above = True
            if p[1] < point[1]:
                below = True
    if below:
        total += 1
    if above:
        total += 1
    return total

def next_astroid(point, slope, raw_points):
    #print(f"{point} - {slope} - {raw_points}")
    if abs(slope) < 0.00001:
        if slope > 0:
            points = [p for p in raw_points if p[0] > point[0]]
            if not points:
                return None
            result = points[0]
            for p in points:
                if p[0] < result[0]:
                    result = p
            return result
        if slope < 0:
            points = [p for p in raw_points if p[0] < point[0]]
            if not points:
                return None
            result = points[0]
            for p in points:
                if p[0] > result[0]:
                    result = p
            return result
        return None
    if slope > 0:
        points = [p for p in raw_points if p[1] > point[1]]
        if not points:
            return None
        result = points[0]
        for p in points:
            if p[1] < result[1]:
                result = p
        return result
    if slope < 0:
        points = [p for p in raw_points if p[1] < point[1]]
        if not points:
            return None
        result = points[0]
        for p in points:
            if p[1] > result[1]:
                result = p
        return result


def print_points(center, points_list, deleted):
    os.system('clear')
    for y in range(42):
        for x in range(41):
            if (x, y) in points_list:
                print('#', end='')
            elif (x, y) == center:
                print('O', end='')
            elif (x, y) in deleted:
                print(f'{deleted.index((x,y))}', end='')
            else:
                print('.', end='')
        print('\n', end='')


def main():
    point = (28, 29)
    i = 0
    data.remove(point)
    slopes_list, slopes_dict = get_slopes(point)
    direction = -1
    deleted = []
    while True:
        direction *= -1
        for slope in slopes_list:
            p = next_astroid(point, direction*slope, slopes_dict[slope])
            if not p:
                continue
            try:
                #print(slopes_dict[slope])
                #print_points(point, data, deleted)
                #time.sleep(0.1)
                data.remove(p)
                deleted.append(p)
                slopes_dict[slope].remove(p)
                if not slopes_dict[slope]:
                    slopes_dict.pop(slope)
                    slopes_list.remove(slope)
                i += 1
                print(f"{i}: {p}")
                if i > 200:
                    return
            except Exception as e:
                traceback.print_exc()
                print(data)
                print(p)
                pass

def test():
    point = (28, 29)
    i = 0
    data.remove(point)
    slopes_list, slopes_dict = get_slopes(point)


def get_max_count():
    max_count = 0
    for point in data:
        count = get_in_sight(point)
        if count > max_count:
            print(point)
            max_count = count
    print(max_count)

if __name__ == "__main__":
    #get_max_count()
    main()
