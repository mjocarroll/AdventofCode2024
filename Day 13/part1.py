# 18/07/25
# mjocarroll
# Day 13 of AoC 2024

# given a claw machine with a claw that travels along a 2D plane and two buttons A and B that move the claw,
# find the minimal number of button pushes needed to win a prize from a given machine (if it's possible)

# this challenge seems like a mathematical solution exists: brute forcing via iteration is unfeasible
# need a formula to quickly find A + B presses
# we can use simultaneous equations:

# if we let a = num of A pushes; b = num of B pushes, then
# x = ax' + bx'' (where x' and x'' are how A and B change the x value respectively)
# y = ay' + by'' (" for y)
# then a = (x - bx'')/x'
# and   ((x - bx'')/x')y' + by''  = y
#       xy'/x' - bx''y'/x' + by''   = y
#       xy' - bx''y'+ bx'y''     = x'y
#       b(x'y'' - x''y')        = x'y - xy'
#      b = (x'y - xy')/(x'y'' - x''y')
# so our presses are the minimal number of a+b (where neither >100) that satisfies the equations

import re

# read in the input file
# step through 4 lines at a time (aka, machine by machine)
# get the new values of A, B, and the prize location, and plug them into the simultaneous equations
def grab_prizes(filename):
    """
    A function to read in an input file denoting claw machine configurations and determine which machines are winnable.
    Parameters
    ----------
    filename : str
        the name of the file containing the machine information.
    """

    line = 0
    tokens = 0
    with open(filename, "r") as f:
        # storing the x+y values of buttons A + B and the prize location in short arrays
        a, b, p = [0, 0], [0, 0], [0, 0]
        while True:
            next_line = f.readline()
            if line % 4 == 0 and next_line[:8] == "Button A":
                a = re.findall("\\d+", next_line)
                a = list(map(int, a))
            elif line % 4 == 1 and next_line[:8] == "Button B":
                b = re.findall("\\d+", next_line)
                b = list(map(int, b))
            elif line % 4 == 2 and next_line[:5] == "Prize":
                p = re.findall("\\d+", next_line)
                p = list(map(int, p))
            elif line % 4 == 3 and next_line.strip() == "":
                # all our variables should be set: solve out simultaneous equations for number of pushes
                # a = (x - bx'')/x'
                # b = (x'y - xy')/(x'y'' - x''y')
                b_pushes = (p[1] * a[0] - p[0] * a[1]) / (b[1] * a[0] - b[0] * a[1])
                a_pushes = (p[0] - b[0] * b_pushes) / a[0]

                # check it's an integer and check its range
                if a_pushes % 1 == b_pushes % 1 == 0:
                    if a_pushes <= 100 and b_pushes <= 100:
                        tokens = int(tokens + (3 * a_pushes) + b_pushes)
            else:
                break
            
            line = line + 1
                
    print("TOKENS:", tokens)
            


# MAIN
grab_prizes("input.txt")