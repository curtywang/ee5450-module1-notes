from typing import Tuple, Union
import math


def add5(a: int) -> int:
    """
    Adds 5 to the input integer a.

    :param a: some integer
    :return: a + 5
    """
    return a + 5


def determinant(a: float, b: float, c: float) -> float:
    """
    Returns the result of sqrt(b^2 - 4ac)
    or raises an exception if the inside is negative.

    :param a: coefficient a in quadratic equation, cannot be 0
    :param b: coefficient b in quadratic equation
    :param c: coefficient c in quadratic equation
    :return:
    """
    inside = b ** 2 - 4 * a * c
    if inside >= 0:
        return math.sqrt(inside)
    else:
        raise ValueError("Result is complex.")


def quadratic_formula(a: float, b: float, c: float) -> Tuple[float, float]:
    """
    Returns the roots of a quadratic equation of form ax^2 + bx + c = y where y = 0.

    TODO: figure out how to handle cases involving non-real numbers

    :param a: coefficient a in quadratic equation, cannot be 0
    :param b: coefficient b in quadratic equation
    :param c: coefficient c in quadratic equation
    :return: x1 ("positive" solution), x2 ("negative" solution)
    """
    if a == 0.0:
        raise ValueError("a cannot be 0.")
    x1 = (-b + determinant(a, b, c)) / (2 * a)
    x2 = (-b - determinant(a, b, c)) / (2 * a)
    return x1, x2

