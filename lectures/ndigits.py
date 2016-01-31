def ndigits(x):
    """
    Takes an integer and returns the number of digits
    (recursive method, Python 2.7)
    :param x: Any integer
    :return: Number of digits in x
    """

    x = abs(x)

    if x < 10:
        return 1
    else:
        return 1 + ndigits(x / 10)


print(ndigits(-10))
print(ndigits(0))
print(ndigits(1))
print(ndigits(-25))
print(ndigits(25))
print(ndigits(123))
print(ndigits(321))
print(ndigits(9999))
print(ndigits(-9999))

