## 02/06/2025
## mjocarroll
# Day 1 of AoC 2024

# calculate similarity score
# make a series of all elements in the right list and how many times they appear
# we can build the similarity score by performing a lookup for every element in the left list

import pandas as pd
# import part 1 for its read_csv() method
from part1 import read_csv

# turn the right column into a pandas series we can use for lookup
def get_column_as_series(filename, column):
    """
    A function to save a list as a series of all its elements and how often they appear.
    Parameters
    ---------
    filename : str
        the filename of the csv file to open.
    column : int
        the index of the column to return as a list.
    """

    df = pd.read_csv(filename, header=None, delimiter="   ", engine="python")
    return df[column].value_counts()



# calc the similarity score
def calc_similarity(list, ser):
    """
    A function to calculate the similarity score for the elements in a list against a given series.
    Parameters
    ---------
    list: list
        the left column of the csv (to step through)
    ser : pandas series
        the right column of the csv (to compare to)
    """

    score = 0
    for i in range(len(list)):
        count = ser.get(list[i])
        if count != None:
            score = score + (list[i] * count)
    

    return score



# MAIN
right_col = get_column_as_series("input.csv", 1)
left_col = read_csv("input.csv", 0)

print("SIMILARITY SCORE: ", calc_similarity(left_col, right_col))

