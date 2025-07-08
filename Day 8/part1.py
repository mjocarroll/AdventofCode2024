# 08/07/25
# mjocarroll
# Day 8 of AoC 2024

# given a map of some antennae, count all the antinodes they can create

# read map from file
def read_map_from_file(filename):
    """
    A function to read a file and store it as a 2D list of its characters (to be used as a map in count_antinodes()).
    Parameters
    ----------
    filename : str
        the file to read from.
    """

    map = []
    with open(filename, "r") as file:
        for line in file:
            map.append(list(line.strip()))
            print(list(line.strip()))

    return map



# find all antinodes for a given frequency
def determine_antinodes(map, freq):
    """
    A function that works out all antinodes for a given frequency and returns the number present.
    Parameters
    ----------
    map : 2D list
        the map to search for antinodes
    freq : char
        the frequency to consider
    """

    return 0



# antennae are 0-9, a-zA-Z. 
# iterate through every possible frequency and if it exists on the map, determine any antinodes
def count_antinodes(map):
    """
    A function to count all antinodes present in a map of antennae of 0+ frequencies.
    Parameters
    ----------
    map : 2D list
        the map to search for antinodes
    """

    count = 0


    print("TOTAL ANTINODES:", count)



## MAIN
map = read_map_from_file("sample.txt")
count_antinodes(map)