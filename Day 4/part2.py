## 17/06/2025
## mjocarroll
# Day 4 of AoC 2024

# X-MAS instead of XMAS

# read in a file as a 2D list of characters
def read_text_as_2D_list(filename):
    """
    A function that reads a given file and stores its characters in a 2D list
    Parameters
    ----------
    filename : str
        the filename of the file to read.
    """

    contents = []
    with open(filename, "r") as file:
        for line in file:
            contents.append(list(line))

    return contents



# more tailored: pinpoint every A
def find_As(grid):
    """A function to pinpoint ever A in the grid"""

    count = 0
    # rows
    for i in range(len(grid)):
        # columns
        for j in range(len(grid[i])):
            if grid[i][j] == 'A':
                if find_XMAS(grid, i, j):
                    count = count + 1
    

    print("XMASs COUNTED: ", count)



# from an A coordinate, determine if an X-MAS exists
def find_XMAS(grid, i, j):
    """A function to find if an X-MAS exists, given a coordinate of an A on the grid."""

    # we need to check what's at each diagonal
    if i <= 0 or i >= (len(grid)-1) or j <= 0 or j >= (len(grid[i])-1):
        # this A is on an edge, thus cannot be the centre of a cross
        return False

    ul = grid[i-1][j-1]
    ur = grid[i-1][j+1]
    dl = grid[i+1][j-1]
    dr = grid[i+1][j+1]
    corners = [ul, ur, dl, dr]

    # check each corner is an S or an M (only two of each, and they must be cis, not trans, across the A)
    if corners.count("S") == 2 and corners.count("M") == 2:
        if ul != dr and ur != dl:
            return True

    return False



# MAIN
grid = read_text_as_2D_list("input.txt")
find_As(grid)