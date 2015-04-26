
# Q1.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    a = 1
    b = 2
    c = 3
    count = 3
    while count <= n:
        old_a = a
        old_b = b
        old_c = c
        a = old_b
        b = old_c
        c = 3 * old_a + 2 * old_b + old_c
        count += 1
    if n <= 3:
        result = n
    else:
        result = old_c
    return result

# Q2.

def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    elif k // 10 == 0:
        return False
    else:
        return has_seven(k // 10)

# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"


def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    >>> pingpong(1)
    1
    >>> pingpong(3)
    3
    >>> pingpong(5)
    5
    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    def pongping(n, direction):
        if n == 1:
            return 1
        elif (n-1) % 7 == 0 or has_seven(n-1) == True:
            return pongping(n-1, direction * -1) + direction
        else:
            return pongping(n-1, direction) + direction
    def num(n):
        if n == 1:
            return 0
        elif (n-1) % 7 == 0 or has_seven(n-1) == True:
            return num(n-1)+1
        else:
            return num(n-1)
    return pongping(n, pow(-1,num(n)))

# Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def num_ten_pairs(q, r):
        if q == 0:
            return 0
        elif q % 10 + r == 10:
            return num_ten_pairs(q // 10, r) + 1
        else:
            return num_ten_pairs(q // 10, r)
    if n == 0:
        return 0
    else:
        return num_ten_pairs(n // 10, n % 10)+ten_pairs(n // 10)

# Q5.

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def count(n, m):
        if n == 0:
            return 1
        elif n < 0 or m > n:
            return 0
        else:
            return count(n-m, m) + count(n, m * 2)
    return count(amount, 1)

