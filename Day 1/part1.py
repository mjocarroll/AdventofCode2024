## 01/06/2025
## mjocarroll
# Day 1 of AoC 2024

# find the total distance of the two lists
# (pair smallest items and each and find distance, then second smallest of each, etc... and add distances all up)

# makes sense to sort both lists - then stepping through them is O(n).
# sort via radix sort (fast, fun, never implemented one before!)

import pandas as pd


# function to read in a csv column as a list
def read_csv(filename, column):
    """
    A function that reads a csv file and returns the specified column as a list.
    Parameters
    ----------
    filename : str
        the filename of the csv file to open.
    column : int
        the index of the column to return as a list.
    """

    # using pandas to grab the desired column
    df = pd.read_csv(filename, header=None, delimiter="   ", engine="python")
    return df[column].tolist()



# function to sort each list
def radix_sort(list):
    """A function that sorts a given list via the radix sort method. Each element is assumed to have the same number of digits."""

    digits = len(str(list[0]))
    # print(len(list), " ", digits)

    # for every digit, split into 10 buckets (arrays) by ith digit. Consolidate by next step.
    for i in range((digits)-1, -1, -1):
        buckets = [[], [], [], [], [], [], [], [], [], []]
        for n in range(len(list)):
            # print("n = ", n)
            # print(list[n])

            if int(str(list[n])[i]) == 0:
                buckets[0].append(list[n])
            elif int(str(list[n])[i]) == 1:
                buckets[1].append(list[n])
            elif int(str(list[n])[i]) == 2:
                buckets[2].append(list[n])
            elif int(str(list[n])[i]) == 3:
                buckets[3].append(list[n])
            elif int(str(list[n])[i]) == 4:
                buckets[4].append(list[n])
            elif int(str(list[n])[i]) == 5:
                buckets[5].append(list[n])
            elif int(str(list[n])[i]) == 6:
                buckets[6].append(list[n])
            elif int(str(list[n])[i]) == 7:
                buckets[7].append(list[n])
            elif int(str(list[n])[i]) == 8:
                buckets[8].append(list[n])
            elif int(str(list[n])[i]) == 9:
                buckets[9].append(list[n])
            else:
                # filter it out of the sort
                # (this doesn't really matter; we're making a lot of assumptions about the input csv)
                print("Invalid character.")

            
            # print(buckets)

        list.clear()
        list.extend(buckets[0])
        list.extend(buckets[1])
        list.extend(buckets[2])
        list.extend(buckets[3])
        list.extend(buckets[4])
        list.extend(buckets[5])
        list.extend(buckets[6])
        list.extend(buckets[7])
        list.extend(buckets[8])
        list.extend(buckets[9])

        # print(list)
            

    return list




# function to calculate distance
def calculate_distance(l1, l2):
    """A function that calculates the distances between the elements in two given lists."""
    
    # check l1 and l2 are equal length
    if len(l1) != len(l1):
        print("lists are not equal length.")
        return

    total = 0
    for i in range(len(l1)):
        total = total + abs(l1[i] - l2[i])

    print("DISTANCE: ", total)



# MAIN
left_list  = read_csv("input.csv", 0)
right_list = read_csv("input.csv", 1)

left_list  = radix_sort(left_list)
right_list = radix_sort(right_list)
# print(left_list)
# print(right_list)

calculate_distance(left_list, right_list)