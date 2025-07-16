# 16/07/25
# mjocarroll
# Day 12 of AoC 2024

# for part 2, we use the area * num of sides to calculate fence pricing, not area * perimeter

# print map (helper function)
def print_map(map):
    """A function for printing a 2D list with each internal list on its own line."""
    for i in range(len(map)):
        print(map[i])



# read input
def read_garden_from_file(filename):
    """
    A function to read a file and store its contents as a 2D list of characters (the garden).
    Parameters
    ----------
    filename : str
        the file to read from.
    """

    garden = []
    with open(filename, "r") as file:
        for line in file:
            garden.append(list(line.strip()))

    return garden



# helper function for handle_plot(): is an element on the corner of its plot
def is_corner(garden, plant, a=None, b=None, c=None):
    """A helper function for handle_plot() for determining whether a given plant is on the corner of its plot in the garden."""

    # return 1 if a corner; 0 if not
    # if outer corner, a != plant and c != plant
    # if inner corner, a == plant and c == plant but b != plant

    # for brevity, make sure everything is uppercase
    p = plant.upper()
    a = a.upper() if a != None else a
    b = b.upper() if b != None else b
    c = c.upper() if c != None else c

    if a != p and c != p:
        return 1
    elif a == p and b != p and c == p:
        return 1
    
    return 0



# recursively branch out to find the boundaries of a given plot
def handle_plot(garden, plot, plant, x, y):
    """
    A function to recursively find the edges of a plot, updating info on the area and num of sides as it goes
    Parameters
    ----------
    garden : 2D list
        a 2D list representation of the garden containing the plots
    plot : list
        a list holding the area and num of sides of the plot
    plant : char
        the type of plant in the plot we're currently surveying
    x, y : nums
        coords of the plant's position in the garden
    """

    # check whether we are the plant we need
    # if so, area +1
    if garden[x][y] != plant:
        # clearly not in the plot; abort
        return
    
    # need to track what we've already counted in this plot
    # do this by setting to lowercase
    garden[x][y] = garden[x][y].lower()
    plot[0] = plot[0] + 1

    # check whether up/down/left/right are plants like us
    # if so, handle_plot() on that plant to count area

    # up
    if y > 0:
        if garden[x][y-1] == plant:
            handle_plot(garden, plot, plant, x, y-1)
    # right
    if x < len(garden)-1:
        if garden[x+1][y] == plant:
            handle_plot(garden, plot, plant, x+1, y)
    # down
    if y < len(garden[0])-1:
        if garden[x][y+1] == plant:
            handle_plot(garden, plot, plant, x, y+1)
    # left
    if x > 0:
        if garden[x-1][y] == plant:
            handle_plot(garden, plot, plant, x-1, y)


    # PART 2: counting sides
    # side length is going to screw us over here, so instead, let's count the number of CORNERS
    # if our current spot is on a corner, plot[1] +1
    # (note that one spot can be on more than one corner)

    # all the coords we need for determining corners
    up    = None if y == 0                  else garden[x][y-1]
    right = None if x == len(garden)-1      else garden[x+1][y]
    down  = None if y == len(garden[0])-1   else garden[x][y+1]
    left  = None if x == 0                  else garden[x-1][y]

    up_right   = None if x == len(garden)-1 or y == 0                else garden[x+1][y-1]
    down_right = None if x == len(garden)-1 or y == len(garden[0])-1 else garden[x+1][y+1]
    down_left  = None if x == 0 or y == len(garden[0])-1             else garden[x-1][y+1]
    up_left    = None if x == 0 or y == 0                            else garden[x-1][y-1]

    # Now our variables have been established: check each direction for corners
    plot[1] = plot[1] + is_corner(garden, plant, up, up_left, left)         # top left
    plot[1] = plot[1] + is_corner(garden, plant, up, up_right, right)       # top right
    plot[1] = plot[1] + is_corner(garden, plant, down, down_right, right)   # bottom right
    plot[1] = plot[1] + is_corner(garden, plant, down, down_left, left)     # bottom left



# determine the boundaries of each plot
def determine_pricing(garden):
    """
    A function to step through a garden and work out the price of fencing for each plot
    Parameters
    ----------
    garden : 2D list
        the garden to determine the plot boundaries of
    """

    price = 0
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            # we are assuming plots are always delineated with capital letters
            # (handle_plot() sets counted plots to lowercase)
            if garden[i][j].isupper():
                plant = garden[i][j]
                plot = [0, 0]
                handle_plot(garden, plot, garden[i][j], i, j)
                price = price + (plot[0] * plot[1])
                print(plot[0], "area,", plot[1], "corners")
                # print_map(garden)
                # print("current price =", price, " ( area :", plot[0], ", perimeter :", plot[0], ")\n")

    print("TOTAL PRICE OF FENCING: ", price)



# MAIN
garden = read_garden_from_file("input.txt")
determine_pricing(garden)