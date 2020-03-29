import math


def distance(a=(0, 0), b=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((a[0] - b[0]) ** 2 +
                     (a[1] - b[1]) ** 2)