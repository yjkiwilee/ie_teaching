from functools import reduce

# Part 1

def sum_of_squares(l):
    """
    Calculate the sum of squares of elements in the list.
    """
    return reduce(
        lambda a, b: a + b,
        map(
            lambda x: x**2,
            l
        )
    )

print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

# Part 2

def sum_of_squares(l):
    return reduce(
        lambda a, b: a + b,
        map(
            lambda x: int(x)**2,
            l
        )
    )

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))

# Part 3

def sum_of_squares(l):
    return reduce(
        lambda a, b: a + b,
        map(
            lambda x: int(x)**2 if x[0] != '#' else 0,
            l
        )
    )

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))