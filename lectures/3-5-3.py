def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    min_arg = min(a, b)

    if min_arg == 1:
        return 1

    test = min_arg

    while test > 1:
        if a % test == 0 and b % test == 0:
            return test
        else:
            test -= 1

    return test


print gcdIter(4, 10)
