import math


def polysum(n, s):
    """
    Computes the sum of area and square of the
    perimeter of the regular polygon, rounded
    to 4 decimal places

    :param n: number of sides
    :param s: length of each side
    :return: float
    """

    area = (0.25 * n * s**2) / math.tan(math.pi/n)
    square_perimeter = (s * n)**2

    result_sum = area + square_perimeter

    return round(result_sum, 4)
