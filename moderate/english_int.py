"""
Given any integer, print an English phrase that describes the integer (e.g. "One Thousand, Two Hundred Thirty Four
--------------
let's handle thousand at first.
1-20 are their own words
20, 30, 40, 50 are their own words
100 is its own word
"""
lookup = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Ninteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    # 100: "Hundred",
    # 1000: "Thousand",
}


def convert_to_str(num):
    if num == 0:
        return "Zero"
    str_list = []
    if num >= 1000:
        raise ValueError("Can't do that yet bub")
    if num >= 100:
        # find the largest number that is smaller than num
        remainder = num % 100
