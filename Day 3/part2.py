## 17/06/2025
## mjocarroll
# Day 3 of AoC 2024

# adapt part 1 to compensate for enables/disabled instructions

import re


import re

# read in input and identify all matches
# return list of matches
def find_mul_from_input(filename):
    """
    A function that reads a given file and returns all matches of the form "mul(x,y)", "do()", and "don't()" found in it as a list in order of appearance.
    Parameters
    ----------
    filename : str
        the filename of the file to open.
    """

    with open(filename, "r") as file:
        text = file.read()
        matches = re.findall("mul\(\\d{1,3},\\d{1,3}\)|do\(\)|don't\(\)", text)
    
    print(matches)
    
    return matches



# calculate sum of all mul() operations from a given list
def sum_all_mul_operations(list):
    """
    A function that takes a list with elements of the form mul(x,y), performs each multiplication, then sums the outcome of all elements.
    Parameters
    ----------
    list : list
        the list to iterate over
    """

    total = 0
    enabled = True
    for i in range(len(list)):
        if list[i] == "do()":
            print("enabled.")
            enabled = True
        elif list[i] == "don't()":
            print("disabled.")
            enabled = False
        # skip all mul commands we see when not enabled.
        elif list[i][0:3] == "mul" and enabled:
            nums = re.findall("\\d{1,3}", list[i])
            x = int(nums[0])
            y = int(nums[1])
            print(list[i], " : ", x, " ", y, " = ", (x * y))
            total = total + (x * y)

    print("TOTAL: ", total)



# MAIN
list = find_mul_from_input("input.txt")
sum_all_mul_operations(list)
