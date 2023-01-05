#!/usr/bin/python3

left_digit, right_digit = 0, 0

while left_digit < 10:
    right_digit = left_digit + 1

    while right_digit < 10:
        if left_digit == 8 and right_digit == 9:
            print(f"{left_digit:d}{right_digit:d}")
        else:
            print(f"{left_digit:d}{right_digit:d}", end=", ")

        right_digit += 1
    left_digit += 1
