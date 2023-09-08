def sum(x, y):
    """
    >>> sum(10,20)
    30

    >>> sum(-10,5)
    -5

    >>> sum (50,31)
    81

    >>> sum ('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x must be integer or float number
    """
    assert isinstance(x, (int, float)), 'x must be integer or float number'
#  Usually assert is to tell other devs something
    assert isinstance(y, (int, float)), 'y must be integer or float number'
    return x+y

# those three arrows represents a test where we are going to
# call in main function


def minus(x, y):
    """
    >>> minus(10,5)
    5

    >>> minus(-10, -5)
    -5

    >>> minus('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x must be integer or float number

    """
    assert isinstance(x, (int, float)), 'x must be integer or float number'
    assert isinstance(y, (int, float)), 'y must be integer or float number'
    return x-y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
