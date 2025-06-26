## 26/06/2025
## mjocarroll
# Day 5 of AoC 2024

# extend part 1 to correctly order the invalid updates


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



def determine_incorrect_rules(Updates):
    """
    A function to collate all invalid updates into a 2D list (of updates and their pages).
    Parameters
    ----------
    Updates : Update_Info
        the object containing all rules and updates given by the input file.
    """

    invalid_updates = []

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

        # only difference from part 1 is the word "not"
        if not valid:
            invalid_updates.append(curr_update)

    return invalid_updates



def reorder_invalid_updates(invalid_updates, rules):
    """
    Given a list of invalid updates, reorder them to follow a set of given rules
    Parameters
    ----------
    invalid_updates : 2D list
        a 2D list of invalid updates (the pages of each update are given as a list)
    rules : dict
        a dictionary of page rules an update must adhere to
    """

    # for every invalid update, step through their pages
    # if we find pages out of order, move it to after the current element

    fixed_updates = []
    for i in range(len(invalid_updates)):
        curr_update = invalid_updates[i]
        j = 0
        while j < len(curr_update):
            shuffles = 0
            page = curr_update[j]
            page_rules = rules.get(page)

            # note: page_rules can't be none if a rule made it invalid
            if page_rules is not None:
                for k in range(len(page_rules)):
                    while page_rules[k] in curr_update[0:j]:
                        # move that element to curr_update[j]
                        # (we are assuming pages cannot be mutual rules for one another - otherwise that makes an infinite loop)
                        # print("<<", curr_update, "RULE : ", page, page_rules)
                        for l in range(len(curr_update[0:j])):
                            if curr_update[l] == page_rules[k]:
                                curr_update.remove(page_rules[k])
                                curr_update = curr_update[0:j] + [page_rules[k]] + curr_update[j:]
                                shuffles += 1
                        # print(">>", curr_update)

            # resume j from the new position of the element we just handled the rules for
            # in case our shuffling makes new rules relevant
            j -= shuffles
            # increment for next loop
            j += 1
            
                
        fixed_updates.append(curr_update)

    return fixed_updates



def sum_middle_pages(updates):
    """
    Sum the middle element from a series of lists (given as a 2D array)
    Parameters
    ----------
    updates : 2D list
        a 2D list of (hopefully now) valid updates (the pages of each update are given as a list)
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

invalid_updates = determine_incorrect_rules(Updates)
# print("INVALID UPDATES : ", invalid_updates)

fixed_updates = reorder_invalid_updates(invalid_updates, Updates.rules)
# print("FIXED UPDATES : ", fixed_updates)

sum = sum_middle_pages(fixed_updates)
print("SUM : ", sum)