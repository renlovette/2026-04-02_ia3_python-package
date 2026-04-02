"""
A module that adds numbers together and subtracts numbers from each other.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""

def add_numbers(a, b):
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtract one number from the other and return the result.

    Parameters
    ----------
    a : float
        The number we are subtracting from.
    b : float
        The number we are subtracting by.

    Returns
    -------
    float
        The result of subtracting b from a.

    Examples
    --------
    >>> subtract_numbers(6, 2)
    4
    >>> subtract_numbers(-2, 7)
    -9

    """
    return a - b