# 15/07/25
# mjocarroll
# Day 11 of AoC 2024

# time to blink at some stones


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



# perform operation on a given stone
def change_stone(stones, index):
    """
    A function to change a stone as given by the rules indicated in this challenge. Returns any changes needed to the index.
    Parameters
    ----------
    stones : num list
        the stones
    index : num
        location of the stone we're concerned with
    """

    # if a stone is 0, make it a 1
    if stones[index] == 0:
        stones[index] = 1
        return index

    # if a stone has an even number of digits, split it into two stones
    if len(str(stones[index])) % 2 == 0:
        s = str(stones[index])
        mid = int(len(s) / 2)
        stone1 = int(s[0:mid])
        stone2 = int(s[mid:])
        stones[index] = stone1
        stones.insert(index+1, stone2)

        return index+1

    # else, multiply by 2024
    stones[index] = stones[index] * 2024

    return index



# perform operations on all stones for this blink
def blink(stones):
    """
    A function to iterate through each stone in the line (given as a list) and call an operation to change it, making the changes in the blink atomic.
    Parameters
    ----------
    stones : num list
        the stones to change, in order
    """

    i = 0
    while i < len(stones):
        # change stone and amend our current index (in case any splits happened)
        i = change_stone(stones, i)
        i = i + 1



# MAIN
stones = read_stones_from_file("input.txt")

print("Blinking...")
for i in range(25):
    blink(stones)

print("STONES AFTER 25 BLINKS:", len(stones))
