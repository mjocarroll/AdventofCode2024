# 10/07/25
# mjocarroll
# Day 9 of AoC 2024

# given a string of numbers signifying blocks of files and free space, fragment the files to minimise free space
# then produce a checksum for the new filespace

# read disk map
def read_disk_map(filename):
    """A function to read a disk map (the puzzle input) into a list from a given file name."""

    with open(filename, "r") as file:
        contents = file.read()

    return list(map(int, list(contents)))



# translate disk map to actual space
# assign file IDs here
def translate_disk_map(disk_map):
    """A function that takes a disk map (as a list) and translates it into a picture of the filespace we can use (as a list) for fragmentation."""

    # alternates between number of file blocks and number of free blocks
    # file flag tells us whether we're looking at 
    file_index = 0
    file = True
    fs = []
    for i in range(len(disk_map)):
        if file:
            for j in range(disk_map[i]):
                fs.append(file_index)
            file_index = file_index + 1
            file = False
        else:
            for j in range(disk_map[i]):
                fs.append('.')
            file = True

    return fs



# helper function for compact_filespace()
# if it returns -1, there is no free space
def find_next_free_space(curr_block, filespace):
    """A function to find the index of the next block of free space (given as a list) in the filespace (starting at our current block inclusive)"""

    for i in range(curr_block, len(filespace)):
        if filespace[i] == '.':
            return i
    
    return -1



# fragment + compact filespace
def compact_filespace(filespace):
    """A function to fragment + compact the filespace (given as a list) into a contiguous block with no free space."""

    free_index = find_next_free_space(0, filespace)
    block_index = len(filespace) - 1

    while free_index > 0:
        # if the block index is currently pointing to a file block, shift it to the next free space
        # else, if block index is pointing at free space, just pop the free space
        # decrement block index and find next free space
        if filespace[block_index] != '.':
            filespace[free_index] = filespace[block_index]

        filespace.pop(block_index)

        free_index = find_next_free_space(free_index, filespace)
        block_index = block_index - 1



# puzzle output: determine the checksum of the new filespace
# sun(position * file ID)
def calc_checksum(filespace):
    """A function with takes the view of the filespace (as a list) and calculates + prints the checksum of its arrangement (position * file ID for all blocks)"""

    checksum = 0
    for i in range(len(filespace)):
        checksum = checksum + (i * filespace[i])

    print("CHECKSUM: ", checksum)



# MAIN
dm = read_disk_map("input.txt")
fs = translate_disk_map(dm)
compact_filespace(fs)
calc_checksum(fs)