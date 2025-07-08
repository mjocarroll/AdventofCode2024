# 08/07/25
# mjocarroll
# Day 8 of AoC 2024

import re

# given a map of some antennae, count all the antinodes they can create


# print map (helper function)
def print_map(map):
    """A function for printing a 2D list with each internal list on its own line."""
    for i in range(len(map)):
        print(map[i])



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

    return map



# antennae are 0-9, a-zA-Z. 
# return a set of all present frequencies in the map
def find_present_frequencies(map):
    """
    A function to find all frequencies used by antennae on a given map.
    Parameters
    ----------
    map : 2D list
        the map to search for frequencies
    """

    freqs = set()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if re.search("[0-9a-zA-Z]", map[i][j]):
                freqs.add(map[i][j])

    print("frequencies", freqs, "found!")
    return freqs



# find all antinodes for a given frequency
def determine_antinodes(map, anti_map, freq):
    """
    A function that works out all antinodes for a given frequency and returns the number present.
    Parameters
    ----------
    map : 2D list
        the map to search for antinodes
    anti_map : 2D list
        the map one which to mark any found antinodes
    freq : char
        the frequency to consider
    """

    tenna = []
    # step through map and determine coords of all antennae of that frequency
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == freq:
                tenna.append([i, j])
    
    # for all antennae, determine difference between it and all remaining locations in the tenna list
    # if its antinodes can exist on the map, mark it on anti_map
    for i in range(len(tenna)):
        for j in range(i+1, len(tenna)):
            # if tenna 1 is farther left than 2
            if tenna[i][0] < tenna[j][0]:
                x1 = tenna[i][0] - (tenna[j][0] - tenna[i][0])
                x2 = tenna[j][0] + (tenna[j][0] - tenna[i][0])
            else:
                x1 = tenna[i][0] + (tenna[i][0] - tenna[j][0])
                x2 = tenna[j][0] - (tenna[i][0] - tenna[j][0])
            # if tenna 1 is higher up than 2
            if tenna[i][1] < tenna[j][1]:
                y1 = tenna[i][1] - (tenna[j][1] - tenna[i][1])
                y2 = tenna[j][1] + (tenna[j][1] - tenna[i][1])
            else:
                y1 = tenna[i][1] + (tenna[i][1] - tenna[j][1])
                y2 = tenna[j][1] - (tenna[i][1] - tenna[j][1])

            # mark antinodes
            if x1 >= 0 and x1 < len(map) and y1 >= 0 and y1 < len(map):
                anti_map[x1][y1] = '#'
            if x2 >= 0 and x2 < len(map) and y2 >= 0 and y2 < len(map):
                anti_map[x2][y2] = '#'



# iterate through every present frequency and determine any antinodes
def count_antinodes(map):
    """
    A function to count all antinodes present in a map of antennae of 0+ frequencies.
    Parameters
    ----------
    map : 2D list
        the map to search for antinodes
    """

    anti_map = [x[:] for x in map]
    for freq in find_present_frequencies(map):
        # will continually update anti_map with unique locations
        determine_antinodes(map, anti_map, freq)
 
    count = 0   
    for i in range(len(anti_map)):
        for j in range(len(anti_map[i])):
            if anti_map[i][j] == '#':
                count = count + 1
    
    print("TOTAL ANTINODES:", count)



## MAIN
map = read_map_from_file("input.txt")
count_antinodes(map)