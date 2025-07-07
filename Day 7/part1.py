# 06/07/25
# mjocarroll
# Day 7 of AoC 2024

# given a file with some equations (minus their operators), see what operations can be added to make the equation true
# parse file, solve recursively



# recursively find all operator options for the equation
# if any meet the target, break and return true
def recursiveSolve(target, operands, total, index):
    """
    A function to try all operator combinations for an equation. Returns true if a combination is found that satisfies the target.
    Parameters
    ----------
    target : num
        the target the operands should sum/multiply to.
    operands : num[]
        the numbers that must be added/multiplied to reach the target.
    total : num
        the running total of this current branch of the computation
    index : num
        the next operand to attempt to add
    """

    # base case: len(operands) = index
    # if total = target, return true, else false
    if len(operands) <= index:
        if total == target:
            return True
        else:
            return False
    
    # case: len(operands) < index
    # branch: add or multiply operands[index] to total, increment index, and recurse
    addTotal = total + operands[index]
    if (recursiveSolve(target, operands, addTotal, index+1)):
        return True

    mulTotal = total * operands[index]
    if (recursiveSolve(target, operands, mulTotal, index+1)):
        return True

    return False



# parse line into target + operands
def parseLine(line):
    """
    A function to parse an equation into its target and operands, returned as an array
    Parameters
    ----------
    line : str
        the equation to parse, given as a string.
    """

    eq = []
    eq.append(int(line.split(":")[0]))
    eq.append(list(map(int, line.split(":")[1].split())))
    print(eq)

    return eq



# step through file line by line
def parseFile(filename):
    """
    A function that steps through a file line by line and determines how many equations given in the file are solvable.
    Parameters
    ----------
    filename : str
        the name of the file with the equations to parse
    """

    total = 0
    with open(filename, "r") as file:
        for line in file:
            equation = parseLine(line)
            target   = equation[0]
            operands = equation[1]
            if (recursiveSolve(target, operands, 0, 0)):
                total += target
    
    print("TOTAL: ", total)


# MAIN
parseFile("input.txt")