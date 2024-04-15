#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from .fizzbuzz import fizzbuzz
from .parse import parse_positive_integer


def usage():
    print("Usage: heiwa4126_fizzbuzz <positive number>", file=sys.stderr)
    exit(1)


def main():
    if len(sys.argv) != 2:
        usage()

    end = parse_positive_integer(sys.argv[1])

    if end is None:
        usage()

    print("\n".join(fizzbuzz(end)))


if __name__ == "__main__":
    main()
