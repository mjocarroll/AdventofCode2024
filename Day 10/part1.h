// 14/07/2025
// mjocarroll
// Day 10 of AoC 2024

// Header file for part 1
// For ease, we're going to assume we know the size of the map

#define MAP_WIDTH  50
#define MAP_HEIGHT 50

void charArrayToIntArray(char input[MAP_HEIGHT][MAP_WIDTH+1], int map[MAP_HEIGHT][MAP_WIDTH]);
void printMap(int map[MAP_HEIGHT][MAP_WIDTH]);
int findTrails(int map[MAP_HEIGHT][MAP_WIDTH], int y, int x);
int step(int map[MAP_HEIGHT][MAP_WIDTH], int peaks_found[MAP_HEIGHT][MAP_WIDTH], int y, int x);