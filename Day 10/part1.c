// 14/07/2025
// mjocarroll
// Day 10 of AoC 2024

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "part1.h"

// read in a "topological map" (a map of nums 0-9) and find how many paths each 0 has to a 9
// where a path cannot move diagonally and only goes up in steps of exactly 1
// output the sum of the trailheads' (the 0s) score (how many 9s each can reach)

int main(int argc, char* argv[]) {
    // one command line argument: the file to read
    if (argc != 2) {
        printf("Usage: ./part1 <map filename>\n");
        return 1;
    }

    // read said file into a 2D array
    FILE *mapfile = fopen(argv[1], "r");
    if (!mapfile) {
        fprintf(stderr, "error: unable to open map file: %s\n", strerror(errno));
        return 1;
    }

    // map will only contain numbers, but read in as char
    // width+1 accommodates for the null character
    char inputMap[MAP_HEIGHT][MAP_WIDTH+1] = {0};
    int lines = MAP_HEIGHT;
    while (lines-- > 0) {
        // sizeof(map) + 1 for \n, +1 for null char
        fgets(inputMap[MAP_HEIGHT-lines-1], sizeof(*inputMap)+2, mapfile);
    }

    // convert to int array for use
    int map[MAP_HEIGHT][MAP_WIDTH] = {0};
    charArrayToIntArray(inputMap, map);
    printMap(map);


    // proper purpose: find all viable trails
    // for every 0 in the array, find its paths to a 9 and return the number
    // sum these paths
    int score = 0;
    for (int i = 0; i < MAP_WIDTH; i++) {
        for (int j = 0; j < MAP_HEIGHT; j++) {
            if (map[i][j] == 0) {
                score += findTrails(map, i, j);
                printf("After new trailhead, score = %d\n", score);
            }
        }
    }

    printf("SCORE: %d\n", score);

}



// helper function: convert a 2D char array to a 2D int array
void charArrayToIntArray(char input[MAP_HEIGHT][MAP_WIDTH+1], int map[MAP_HEIGHT][MAP_WIDTH]) {
    for (int i = 0; i < MAP_WIDTH; i++) {
        for (int j = 0; j < MAP_HEIGHT; j++) {
            map[i][j] = input[i][j] - '0';
        }
    }
}



// helper function: print the map
void printMap(int map[MAP_HEIGHT][MAP_WIDTH]) {
    for (int i = 0; i < MAP_HEIGHT; i++) {
        for (int j = 0; j < MAP_WIDTH; j++) {
            printf("%d", map[i][j]);
        }
        printf("\n");
    }
}



/* Find all possible reachable 9s from a given trailhead.
 * map : the map to search for trails
 * x   : x coord of the given trailhead
 * y   : y coord of the given trailhead
 * return : the number of trails possible from this trailhead
 */
int findTrails(int map[MAP_HEIGHT][MAP_WIDTH], int y, int x) {
    if (map[y][x] != 0) {
        // not a trailhead
        return 0;
    }

    // step() will be recursively called from the current position 
    // and returns how many trails were found
    // use an array to ensure no 9 is counted twice
    int peaks_found[MAP_HEIGHT][MAP_WIDTH] = {0};
    return step(map, peaks_found, y, x);
}



/* Recursively try the next step of every possible path from our current step
 * map          : the map to search for trails
 * peaks_found  : a global record of whether a 9 has been reached from this trailhead
 * x            : x coord of the current step
 * y            : y coord of the current step
 * return : the number of trails possible from this trailhead
 */
int step(int map[MAP_HEIGHT][MAP_WIDTH], int peaks_found[MAP_HEIGHT][MAP_WIDTH], int y, int x) {
    int current_step = map[y][x];

    // base case: current_step == 9
    // then we found a trail and can return 1
    if (current_step == 9) {
        if (peaks_found[y][x] == 1) {
            // we've already counted this one
            return 0;
        }
        // else, mark we've reached it for the first time
        peaks_found[y][x] = 1;
        return 1;
    }

    int total = 0;
    // else, look at all 4 adjacent cells for current_step + 1
    // up
    if (y < MAP_HEIGHT-1 && map[y+1][x] == current_step+1) {
        total += step(map, peaks_found, y+1, x);
    }
    // right
    if (x < MAP_WIDTH-1 && map[y][x+1] == current_step+1) {
        total += step(map, peaks_found, y, x+1);
    }
    // down
    if (y > 0 && map[y-1][x] == current_step+1) {
        total += step(map, peaks_found, y-1, x);
    }
    // left
    if (x > 0 && map[y][x-1] == current_step+1) {
        total += step(map, peaks_found, y, x-1);
    }

    // return the sum of paths found from the four directions
    return total;
}