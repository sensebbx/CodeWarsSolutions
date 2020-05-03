"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def first_move_zeros(array):
    result = []
    zeroes_amount = 0
    for x in array:
        if x == 0 and type(x) in [int, float]:
            zeroes_amount += 1
            continue
        result.append(x)

    result.extend([0 for i in range(zeroes_amount)])

    return result


def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
