

# Q1.

def triangular(x, y, z):
    """Return whether x, y, and z are triangular.

    >>> triangular(3, 4, 5)
    True
    >>> triangular(3, 14, 5) # 14 is greater than 3 + 5
    False
    >>> triangular(7.5, 3.5, 4) # 7.5 is equal to 3.5 + 4
    False
    >>> result = triangular(5, 4, 3) # Return, don't print
    >>> result
    True
    """
    "*** YOUR CODE HERE ***"
    if x + y > z and y + z > x and z + x > y:
        return True
    else:
        return False

# Q2.

def next_square(x):
    from math import sqrt, floor
    """Return the smallest perfect square greater than x.

    >>> next_square(10)
    16
    >>> next_square(39)
    49
    >>> next_square(100)
    121
    >>> result = next_square(2) # Return, don't print
    >>> result
    4
    """
    "*** YOUR CODE HERE ***"
    def square(n):
        return n * n
    return square(floor(sqrt(x))+1)

# Q3.

def digit_span(x):
    """Return the difference between x's largest and smallest digits.

    >>> digit_span(2013) # 3 - 0 = 3
    3
    >>> digit_span(75) # 7 - 5 = 2
    2
    >>> digit_span(2345678765432) # 8 - 2 = 6
    6
    >>> result = digit_span(6473465) # Return, don't print
    >>> result
    4
    """
    "*** YOUR CODE HERE ***"
    assert x > 0, 'Please input a positive integer.'
    maximum, minimum = 0, 9
    while x > 0:
        temp = x % 10
        x = x // 10
        maximum = max(maximum, temp)
        minimum = min(minimum, temp)
    difference = maximum - minimum
    if x == 0 and difference <= 0:
        return 0
    else:
        return difference
