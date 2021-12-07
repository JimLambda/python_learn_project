def sum_function(num_a, num_b):
    print(num_a + num_b)
    print(__name__)
    return num_a + num_b


def sum_function(num_a, num_b):
    print(num_a - num_b)
    print(__name__)
    return num_a + num_b


if __name__ == '__main__':
    sum_function(2, 3)
