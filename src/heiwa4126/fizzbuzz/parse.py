#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parse_positive_integer(arg):
    num = int(arg)
    return num if isinstance(num, int) and num > 0 else None
