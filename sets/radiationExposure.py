def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''

    if start >= stop:
        return 0

    area_width = stop - start
    slice_count = area_width/step

    slice_width = area_width/(slice_count * 1.0)  # force float

    total_radiation = 0

    for integral in range(0, int(slice_count)):
        slice_x = start + (slice_width * integral)
        area = slice_width * f(slice_x)
        total_radiation += area

    return total_radiation


print(radiationExposure(0, 5, 1))   # 39.10318784326239
print(radiationExposure(5, 11, 1))  # 22.94241041057671
print(radiationExposure(0, 11, 1))  # 62.0455982538
print(radiationExposure(40, 100, 1.5))  # 0.434612356115
