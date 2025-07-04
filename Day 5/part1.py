## 19/06/2025, 26/06/2025
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
            # print(">>", line, "(flag =", flag, ")")
            if not line.rstrip():
                flag = True
            elif flag == False:
                Updates.rules.update(parse_rule(line, Updates.rules))
            else:
                Updates.updates.append(parse_update(line))

    return Updates



def parse_rule(line, rules):
    """
    A function for parsing a line (str) into a rule for the updates, adding to the existing rules.
    Parameters
    ----------
    line : str
        line from the file to parse
    rules : dict
        dictionary of existing rules
    """

    x = line.rstrip("\n")
    nums = x.split("|")

    if len(nums) == 2:
        # print(nums)
        if rules.get(int(nums[0])) is None:
            return {int(nums[0]) : [int(nums[1])]}
        else:
            values = rules.get(int(nums[0]))
            values.append(int(nums[1]))
            return {int(nums[0]) : values}
    
    print("wu oh")
    return {0 : 0}



def parse_update(line):
    """
    A function for parsing a line (str) into a list of pages for an update.
    Parameters
    ----------
    line : str
        line from the file to parse
    """

    x = line.rstrip("\n")
    nums = x.split(",")
    for i in range(len(nums)):
        nums[i] = int(nums[i])

    return nums



def determine_correct_rules(Updates):
    """
    A function to collate all valid updates into a 2D list (of updates and their pages).
    Parameters
    ----------
    Updates : Update_Info
        the object containing all rules and updates given by the input file.
    """

    valid_updates = []

    # for every update we need to validate
    for i in range(len(Updates.updates)):
        valid = True
        # step through each page one by one
        # lookup its values in the dictionary: each page it needs to come before (if both exist)
        # for each value, fail this update if the page exists in this update AND it exists before our current page
        curr_update = Updates.updates[i]
        for j in range(len(curr_update)):
            page = curr_update[j]
            page_rules = Updates.rules.get(page)

            if page_rules is not None:
                for k in range(len(page_rules)):
                    if page_rules[k] in curr_update[0:j]:
                        valid = False
                        break

        if valid:
            valid_updates.append(curr_update)

    return valid_updates



def sum_middle_pages(updates):
    """
    Sum the middle element from a series of lists (given as a 2D array)
    Parameters
    ----------
    updates : 2D list
        a 2D list of valid updates (the pages of each update are given as a list)
    """

    sum = 0
    for i in range(len(updates)):
        # challenge doesn't specify what to do if an update has an even number of pages
        sum += updates[i][len(updates[i]) // 2]

    return sum



# MAIN
Updates = collate_dict_and_updates("input.txt")
# print("RULES   :", Updates.rules)
# print("UPDATES :", Updates.updates)

valid_updates = determine_correct_rules(Updates)
# print("VALID UPDATES : ", valid_updates)

sum = sum_middle_pages(valid_updates)
print("SUM : ", sum)