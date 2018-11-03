from math import tan, pi

def polysum(n, s):
    """
    n = number of sides
    s = length of each side
    area = area of polygon
    perimeter = length of each side * number of sides
    returns the sum (of area and square of perimeter of regular polygon)
    rounded to 4 decimal places
    """
    area = (0.25*n*s**2)/(tan(pi/n))
    perimeter = s*n
    return round(area + perimeter**2, 4)