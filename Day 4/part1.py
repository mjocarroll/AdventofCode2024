## 17/06/2025
## mjocarroll
# Day 4 of AoC 2024

# solve word search for every occurrence of the word "XMAS in any orientation
# read word search in as a 2D array
# search every X for an M in an adjacent/diagonal cell, then an A in the same direction, then an S


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



# search the word search for the given word (XMAS)
# print how many times it occurs
def search_for_word(grid, word):
    """
    A function that searches a 2D list of characters for a given word (assumed to be 2 chars or longer) across adjacent cells (horizontally, vertically, or diagonally)
    Parameters
    ----------
    grid : list
        the 2D list to search
    word : str
        the word to search for in the 2D list
    """

    count = 0
    # rows
    for i in range(len(grid)):
        # columns
        for j in range(len(grid[i])):
            if grid[i][j] == word[0]:
                # check 8 adjacent cells for the second letter
                # if it's found, follow that direction to see if it has the whole word

                # up
                if i > 0 and grid[i-1][j] == word[1]:
                    if follow_word(grid, (i-1), j, word, 2, "up"):
                        count = count + 1
                # up + right
                # no elifs, because one word[0] can be the anchor of several words
                if i > 0 and j < (len(grid[i])-1) and grid[i-1][j+1] == word[1]:
                    if follow_word(grid, (i-1), (j+1), word, 2, "ur"):
                        count = count + 1
                # right
                if j < (len(grid[i])-1) and grid[i][j+1] == word[1]:
                    if follow_word(grid, i, (j+1), word, 2, "ri"):
                        count = count + 1
                # down + right
                if i < (len(grid)-1) and j < (len(grid[i])-1) and grid[i+1][j+1] == word[1]:
                    if follow_word(grid, (i+1), (j+1), word, 2, "dr"):
                        count = count + 1
                # down
                if i < (len(grid)-1) and grid[i+1][j] == word[1]:
                    if follow_word(grid, (i+1), j, word, 2, "do"):
                        count = count + 1
                # down + left
                if i < (len(grid)-1) and j > 0 and grid[i+1][j-1] == word[1]:
                    if follow_word(grid, (i+1), (j-1), word, 2, "dl"):
                        count = count + 1
                # left
                if j > 0 and grid[i][j-1] == word[1]:
                    if follow_word(grid, i, (j-1), word, 2, "le"):
                        count = count + 1
                # up + left
                if i > 0 and j > 0 and grid[i-1][j-1] == word[1]:
                    if follow_word(grid, (i-1), (j-1), word, 2, "ul"):
                        count = count + 1
                        



    
    print(word, "s COUNTED: ", count)



# follow each letter in the same direction
def follow_word(grid, i, j, word, char_index, direction):
    """
    A function that searches a 2D list for a word written in a given direction
    Parameters
    ----------
    grid : list
        the 2D list to search
    i, j : num
        current coordinates the char_index should be within the grid
    word : str
        the word to search for in the 2D list
    char_index : str
        the character in the word we're currently looking for
    direction : str
        the direction the next character should be found in on the grid
    """

    # base case
    if char_index == len(word):
        # then the word exists on the grid!
        print("base case hit.")
        return True

    # else, recurse until we either finish the word or don't find the right letter
    print("Recursing to find letter ", word[char_index])
    match direction:
        case "up":
            if i > 0 and grid[i-1][j] == word[char_index]:
                if follow_word(grid, (i-1), j, word, (char_index+1), "up"):
                    return True
        case "ur":
            if i > 0 and j < (len(grid[i])-1) and grid[i-1][j+1] == word[char_index]:
                if follow_word(grid, (i-1), (j+1), word, (char_index+1), "ur"):
                    return True
        case "ri":
            if j < (len(grid[i])-1) and grid[i][j+1] == word[char_index]:
                if follow_word(grid, i, (j+1), word, (char_index+1), "ri"):
                    return True
        case "dr":
            if i < (len(grid)-1) and j < (len(grid[i])-1) and grid[i+1][j+1] == word[char_index]:
                if follow_word(grid, (i+1), (j+1), word, (char_index+1), "dr"):
                    return True
        case "do":
            if i < (len(grid)-1) and grid[i+1][j] == word[char_index]:
                if follow_word(grid, (i+1), j, word, (char_index+1), "do"):
                    return True
        case "dl":
            if i < (len(grid)-1) and j > 0 and grid[i+1][j-1] == word[char_index]:
                if follow_word(grid, (i+1), (j-1), word, (char_index+1), "dl"):
                    return True
        case "le":
            if j > 0 and grid[i][j-1] == word[char_index]:
                if follow_word(grid, i, (j-1), word, (char_index+1), "le"):
                    return True
        case "ul":
            if i > 0 and j > 0 and grid[i-1][j-1] == word[char_index]:
                if follow_word(grid, (i-1), (j-1), word, (char_index+1), "ul"):
                    return True
        case _:
            print("Not a direction.")
            return False
        
    return False



# MAIN
word_search = read_text_as_2D_list("input.txt")
search_for_word(word_search, "XMAS")