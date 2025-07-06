// 05/07/25
// mjocarroll
// Day 6 of AoC 2024
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "part2.h"



// given a map, predict the path of a guard
// now figure out all the locations an obstacle can be placed to cause the guard to loop


int main(int argc, char* argv[]) {
    // one command line argument: the file to read
    if (argc != 2) {
        printf("Usage: ./part1 <map filename>\n");
        return 1;
    }

    // read said file into a 2D array (array of arrays)
    FILE *mapfile = fopen(argv[1], "r");
    if (!mapfile) {
        fprintf(stderr, "error: unable to open map file: %s\n", strerror(errno));
        return 1;
    }

    char map[ROWS][COLS] = {0};
    // variables we need for tracking a guard's position
    int g_row, g_col, g_dir, guard_found = 0;

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (fscanf(mapfile, " %c", &map[i][j]) != 1) {
                exit(1);
            } 
            if (!(map[i][j] == '.') && !(map[i][j] == '#')) {
                if (!guard_found) {
                    printf("guard found!\n");
                    g_row = i;
                    g_col = j;
                    guard_found = 1;
                    if (map[i][j] == '^') g_dir = U;
                    else if (map[i][j] == '>') g_dir = R;
                    else if (map[i][j] == 'v') g_dir = D;
                    else if (map[i][j] == '<') g_dir = L;
                } else {
                    printf("\ntoo many guards\n");
                    exit(1);
                }
            }              
        }   
    }
    if (!guard_found) {
        printf("\nno guard!\n");
        exit(1);
    }
    fclose(mapfile);
    printMap(map);

    // PART 2: we want to place down obstacles and see what happens
    // findPath now returns whether or not the guard ever exited
    // run on every location we could put a new obstacle
    int obstacles = determineLoops(map, g_row, g_col, g_dir);

    printf("\n");
    printMap(map);
    printf("OBSTACLES: %d\n", obstacles);
    
}



// PART 2 METHOD
// returns the number of obstacle locations that create loops
int determineLoops(char map[ROWS][COLS], int g_row, int g_col, int dir) {
    // add a single new obstacle
    int loops = 0;
    int obs_tried = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (map[i][j] == '.') {
                map[i][j] = '#';
                // run findpath on every new variation of the map
                // if a guard loops, findPath returns 0
                int obs_map[ROWS][COLS] = {0};
                if (!findPath(map, obs_map, g_row, g_col, dir)) {
                    loops++;
                }
                obs_tried++;
                map[i][j] = '.';
            }
        }
        printf("Obstacles tried: %d, successful loops: %d\n", obs_tried, loops);
    }
    
    return loops;

}




int findPath(char map[ROWS][COLS], int obs_map[ROWS][COLS], int g_row, int g_col, int dir) {
    // findPath tackles map one step at a time, recursively
    // PART 2: need to track how many times an obstacle has been hit
    // use obs_map: every time an obstacle is hit, mark its position on obs_map. 
    // if an obstacle is hit twice, a loop exists.

    // base case: guard is facing map edge
    // walk off map + return
    if ((g_row == 0 && dir == U)            // upper edge
        || (g_col == COLS && dir == R)      // right
        || (g_row == ROWS && dir == D)      // lower
        || (g_col == 0 && dir == L)         // left
    ) {
        return 1;    
    }

    // case: guard is facing an obstacle
    int o_row = g_row;
    int o_col = g_col;
    if (dir == U) o_row = g_row-1;
    else if (dir == R) o_col = g_col+1;
    else if (dir == D) o_row = g_row+1;
    else if (dir == L) o_col = g_col-1;

    if (map[o_row][o_col] == '#') {
        // if we've seen this obstacle twice before, we must be looping
        if (obs_map[o_row][o_col] == 3) {
            // printMap(obs_map);
            return 0;
        }

        // else, mark it and turn right
        obs_map[o_row][o_col]++;
        if (dir == U) dir = R;
        else if (dir == R) dir = D;
        else if (dir == D) dir = L;
        else if (dir == L) dir = U;

        return findPath(map, obs_map, g_row, g_col, dir);
    }

    // case: nothing is facing guard
    else {
        // walk forward
        if (dir == U) g_row--;
        else if (dir == R) g_col++;
        else if (dir == D) g_row++;
        else if (dir == L) g_col--;

        return findPath(map, obs_map, g_row, g_col, dir);
    }
    
    return 1;
}



void printMap(char map[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        printf("line %d: ", i+1);
        for (int j = 0; j < COLS; j++) {
            printf("%c", map[i][j]);        
        } 
        printf("\n"); 
    }
}