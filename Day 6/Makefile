# 27/06/2025
# mjocarroll
# Day 6 of AoC 2024

# Makefile for parts 1 and 2

all: part1 part2


part1: part1.o 
	clang -Wall -Wextra -g part1.o -o part1

part2: part2.o 
	clang -Wall -Wextra -g part2.o -o part2

part1.o: part1.c part1.h
	clang -Wall -Wextra -g -c part1.c -o part1.o

part2.o: part2.c part2.h
	clang -Wall -Wextra -g -c part2.c -o part2.o

clean:
	rm *.o part1 part2