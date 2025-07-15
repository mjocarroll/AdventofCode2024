# 15/07/25
# mjocarroll
# Day 11 of AoC 2024

# too many blinks to brute force this method; good idea to rely on caching to speed up computation

from functools import cache

# read stones in as a list
def read_stones_from_file(filename):
    """
    A function to read a file and store its contents as a list of nums (the stones).
    Parameters
    ----------
    filename : str
        the file to read from.
    """

    stones = []
    with open(filename, "r") as file:
        line = file.read()
        stones = list(map(int, line.split()))

    return stones



# because a stone never really cares about its neighbors, we can compute each stone individually
# for n blinks
# For part 2, we can cache this result so if this stone is ever found again, we don't have to recompute.
@cache
def blink_n_times(stone, n):
    """
    A function to change a stone as given by the rules indicated in this challenge. Returns how many stones are there after blinking n times at the given stone
    Parameters
    ----------
    stone : num
        the number on the stone we're currently looking at
    n : num
        the number of blinks (recursions) we still need to do
    """

    # base case: no more blinks
    if n <= 0:
        return 1
    
    # else, we need to blink again
    # apply rules and recurse
    # 0 -> 1
    if stone == 0:
        return blink_n_times(1, n-1)

    # even digit nm -> n, m
    if len(str(stone)) % 2 == 0:
        s = str(stone)
        mid = int(len(s) / 2)
        
        return blink_n_times(int(s[0:mid]), n-1) + blink_n_times(int(s[mid:]), n-1)

    # else, * 2024
    return blink_n_times(stone * 2024, n-1)



# MAIN
stones = read_stones_from_file("input.txt")
stone_count = 0

print("Blinking...")
for i in range(len(stones)):
    stone_count = stone_count + blink_n_times(stones[i], 75)

print("STONES AFTER 75 BLINKS:", stone_count)
