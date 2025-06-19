## 19/06/2025
## mjocarroll
# Day 5 of AoC 2024

# store all rules in a dictionary (X as key, Ys as value)
# then check the pages in each update. If X appears, does Y appear in the update too, and if so: is it after it?
# then an extra function to sum all the middle pages

# using a class so we only have to read the file once
class Update_Info:
    def __init__(self, rules, updates):
        """
        A class that stores the rules for an update and the pages involved in updates as attributes.
        Attributes
        ----------
        rules : dict
            a dictionary of a page number and the pages that, if both appear, cannot appear before it
        updates : 2D list
            a 2D list of updates (the pages of each update are given as a list)
        """

        self.rules   = rules
        self.updates = updates



def collate_dict_and_updates(filename):
    """
    A function which reads a given file and creates an Update_Info object to store the file info in, which it then returns.
    Parameters
    ----------
    filename : str
        the filename of the file to read.
    """

    flag = False
    Updates = Update_Info({}, [])
    with open(filename, "r") as file:
        for line in file:
            # regex into X | Y until we see a blank line
            # then switch into parsing as lists
            print(">>", line)
            if not line.rstrip():
                flag == True
            elif flag == False:
                Updates.rules.update(parse_rule(line))
            else:
                print("here!")
                Updates.updates.append(parse_update(line))

    
    print(Updates.rules)
    print(Updates.updates)
    return Updates




def parse_rule(line):
    """A function for parsing a line (str) into a rule for the updates."""

    print("pr")
    x = line.rstrip("\n")
    nums = x.split("|")

    if len(nums) == 2:
        print(nums)
        return {nums[0] : nums[1]}
    
    print("wu oh")
    return {0 : 0}



def parse_update(line):
    """A function for parsing a line (str) into a list of pages for an update."""
    
    print("pu")

    return [1, 2, 3]




def determine_correct_rules(Updates):
    """
    A function to collate all valid updates into a 2D lis (of updates and their pages).
    Parameters
    ----------
    Updates : Update_Info
        the object containing all rules and updates given by the input file.
    """




def sum_middle_pages(updates):
    """
    Sum the middle element from a series of lists (given as a 2D array)
    Parameters
    ----------
    updates : 2D list
        a 2D list of valid updates (the pages of each update are given as a list)
    """





# MAIN
Updates = collate_dict_and_updates("sample.txt")
# valid_updates = determine_correct_rules(updates)
# sum_middle_pages(valid_updates)