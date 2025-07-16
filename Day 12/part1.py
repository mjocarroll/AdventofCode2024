# 16/07/25
# mjocarroll
# Day 12 of AoC 2024

# determine area + perimeter of all plots in a garden
# then calculate the total price of fencing the garden

# print map (helper function)
def print_map(map):
    """A function for printing a 2D list with each internal list on its own line."""
    for i in range(len(map)):
        print(map[i])



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



# recursively branch out to find the boundaries of a given plot
def handle_plot(garden, plot, plant, x, y):
    """
    A function to recursively find the edges of a plot, updating info on the area and perimeter as it goes
    Parameters
    ----------
    garden : 2D list
        a 2D list representation of the garden containing the plots
    plot : list
        a list holding the area and perimeter of the plot
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
    # if so, handle_plot() on that plant
    # else, perimeter +1

    # up
    if y > 0:
        if garden[x][y-1] == plant:
            handle_plot(garden, plot, plant, x, y-1)
        elif garden[x][y-1] != plant.lower():
            plot[1] = plot[1] + 1
    # still need to count map borders as a perimeter
    else:
        plot[1] = plot[1] + 1
    
    # right
    if x < len(garden)-1:
        if garden[x+1][y] == plant:
            handle_plot(garden, plot, plant, x+1, y)
        elif garden[x+1][y] != plant.lower():
            plot[1] = plot[1] + 1
    else:
        plot[1] = plot[1] + 1

    # down
    if y < len(garden[0])-1:
        if garden[x][y+1] == plant:
            handle_plot(garden, plot, plant, x, y+1)
        elif garden[x][y+1] != plant.lower():
            plot[1] = plot[1] + 1
    else:
        plot[1] = plot[1] + 1

    # left
    if x > 0:
        if garden[x-1][y] == plant:
            handle_plot(garden, plot, plant, x-1, y)
        elif garden[x-1][y] != plant.lower():
            plot[1] = plot[1] + 1
    else:
        plot[1] = plot[1] + 1



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
                # print_map(garden)
                # print("current price =", price, " ( area :", plot[0], ", perimeter :", plot[0], ")\n")

    print("TOTAL PRICE OF FENCING: ", price)



# MAIN
garden = read_garden_from_file("input.txt")
determine_pricing(garden)