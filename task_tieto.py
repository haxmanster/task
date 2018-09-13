#!/usr/bin python3

import sys


def number_in_memory(number1, number2):
    number1 = str(number1)
    number2 = str(number2)
    print("  ", number1, "\n +", number2, "\n", "-" * 10)
    print("  ", int(number1) + int(number2))

number_in_memory(sys.argv[1], sys.argv[2])


