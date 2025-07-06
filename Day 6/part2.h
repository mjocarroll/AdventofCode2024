// 05/07/25
// mjocarroll
// Day 6 of AoC 2024

// Header file for part 2

// for ease, I'm using macros rather than counting the rows/cols in the file
#define ROWS 130
#define COLS 130

// directions
#define U 0
#define R 1
#define D 2
#define L 3

int findPath(char map[ROWS][COLS], int obs_map[ROWS][COLS], int g_row, int g_col, int dir);
void printMap(char map[ROWS][COLS]);

int determineLoops(char map[ROWS][COLS], int g_row, int g_col, int dir);