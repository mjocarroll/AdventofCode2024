// 27/06/2025 - 05/07/25
// mjocarroll
// Day 6 of AoC 2024
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "part1.h"



// given a map, predict the path of a guard
// guard moves forward, turns 90 degrees when they hit an object
// answer is how many distinct positions the guard covers on a map


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

    // pass 2D array to findpath(), which will mark the path accordingly
    findPath(map, g_row, g_col, g_dir);

    // print number of marks
    int marks = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (map[i][j] == 'X') {
                marks++;
            }
        }
    }

    printf("\n");
    printMap(map);
    printf("MARKS: %d\n", marks);
    
}



void findPath(char map[ROWS][COLS], int g_row, int g_col, int dir) {
    // findPath tackles map one step at a time, recursively

    // base case: guard is facing map edge
    // walk off map + return
    if ((g_row == 0 && dir == U)            // upper edge
        || (g_col == COLS && dir == R)      // right
        || (g_row == ROWS && dir == D)      // lower
        || (g_col == 0 && dir == L)         // left
    ) {
        map[g_row][g_col] = 'X';
        return;    
    }

    // case: guard is facing an obstacle
    else if ((dir == U && map[g_row-1][g_col] == '#')
        || (dir == R && map[g_row][g_col+1] == '#')
        || (dir == D && map[g_row+1][g_col] == '#')
        || (dir == L && map[g_row][g_col-1] == '#')
    ) {
        // turn right
        if (dir == U) dir = R;
        else if (dir == R) dir = D;
        else if (dir == D) dir = L;
        else if (dir == L) dir = U;

        findPath(map, g_row, g_col, dir);
    }

    // case: nothing is facing guard
    else {
        // walk forward
        map[g_row][g_col] = 'X';
        if (dir == U) g_row--;
        else if (dir == R) g_col++;
        else if (dir == D) g_row++;
        else if (dir == L) g_col--;

        findPath(map, g_row, g_col, dir);
    }
    
    return;
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