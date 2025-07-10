# 10/07/25
# mjocarroll
# Day 9 of AoC 2024

# given a string of numbers signifying blocks of files and free space, shift the files to minimise free space
# then produce a checksum for the new filespace
# PART 2: no fragmentation. Only move to where there's space for the whole file

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
# if it returns -1, there is no free space of the given size
def find_next_free_space(curr_block, size, filespace):
    """A function to find the index of the leftmost block of free space of a given size in the filespace  (given as a list) (ending at our current block exclusive)"""

    block_size = 0
    for i in range(curr_block):
        if filespace[i] == '.':
            block_size = block_size + 1
            if block_size == size:
                # return the index of the start of this string of free blocks
                return (i-(block_size-1))
        # if we come across a file block, reset free block size
        elif block_size > 0:
            block_size = 0
    
    return -1



# helper function for compact_filespace()
def find_file_length(file_index, filespace):
    """A function to find the size of a given file in the filespace (given as a list)"""

    block_size = 0
    id = filespace[file_index]
    for i in range(file_index, len(filespace)):
        if filespace[i] == id:
            block_size = block_size + 1
        # if we come across a block without that id, then we know we've seen the end of the file
        elif block_size > 0:
            return block_size
    
    return block_size



# fragment + compact filespace
def compact_filespace(filespace):
    """A function to rearrange the filespace (given as a list) to minimise free space."""

    # PART 2: move blocks grouped by their file
    # find the highest id we need to consider; we work decrementing from there
    curr_id = -1
    for i in range(len(filespace)):
        if filespace[i] != '.' and curr_id < filespace[i]:
            curr_id = filespace[i]
    
    while curr_id > 0:
        # find location and size of the file with the curr_id
        file_len = 0
        file_loc = 0
        for i in range(len(filespace)):
            if filespace[i] == curr_id:
                file_len = find_file_length(i, filespace)
                file_loc = i
                break
        
        # find leftmost free space of its size
        # if it exists, move it
        # else, skip
        free_index = find_next_free_space(i, file_len, filespace)
        if free_index >= 0:
            for j in range(file_len):
                filespace[free_index] = filespace[file_loc]
                filespace[file_loc] = '.'

                free_index = free_index + 1
                file_loc = file_loc + 1
        
        curr_id = curr_id - 1


# puzzle output: determine the checksum of the new filespace
# sun(position * file ID)
def calc_checksum(filespace):
    """A function with takes the view of the filespace (as a list) and calculates + prints the checksum of its arrangement (position * file ID for all blocks)"""

    checksum = 0
    for i in range(len(filespace)):
        if filespace[i] != '.':
            checksum = checksum + (i * filespace[i])

    print("CHECKSUM: ", checksum)



# MAIN
dm = read_disk_map("input.txt")
print("Translating to disk map...")
fs = translate_disk_map(dm)
print("Compacting filespace...")
compact_filespace(fs)
calc_checksum(fs)