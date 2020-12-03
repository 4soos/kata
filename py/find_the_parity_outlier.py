def find_outlier(integers):
    even_count = 0
    for i in integers:
        if i % 2 == 0:
            even_count += 1
    if even_count >= 2:
        return [val for val in integers if val % 2 != 0][0]
    else:
        return [val for val in integers if val % 2 == 0][0]


def find_outlier_best_version(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


def find_outlier_bit_version(integers):
    assert len(integers) >= 3

    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False
