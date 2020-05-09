
width = 25
height = 6

def file_as_list(filename):
    with open(filename, 'r') as f:
        result = f.read().strip()
    return result


def main():
    i = file_as_list('input.txt')
    layers = []
    pos = 0
    per_layer = width*height
    while pos < len(i):

        layers.append(i[pos:pos+per_layer])
        pos += per_layer
    min_l = 0
    min_zeros = 10000000
    for layer in layers:
        zeros = sum([1 for d in layer if d == "0"])
        if zeros < min_zeros:
            min_zeros = zeros
            min_l = layers.index(layer)
    final = [2]*per_layer
    for i in range(per_layer):
        for layer in layers:
            if layer[i] in ['1', '0']:
                final[i] = layer[i]
                break
    pos = 0
    while pos < len(final):
        print(''.join(final[pos:pos+25]))
        pos += 25


if __name__ == "__main__":
    main()
