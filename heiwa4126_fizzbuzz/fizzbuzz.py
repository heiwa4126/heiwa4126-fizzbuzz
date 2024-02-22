#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    Generate the FizzBuzz sequence up to a given number.

    Args:
        n (int): The number up to which the FizzBuzz sequence should be generated.

    Yields:
        str: The next element in the FizzBuzz sequence.

    Examples:
        >>> list(fizzbuzz(15))
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)


if __name__ == "__main__":
    for result in fizzbuzz(15):
        print(result)
