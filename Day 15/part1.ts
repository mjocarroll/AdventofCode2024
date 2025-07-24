// 23/07/2025
// mjocarroll
// Day 15 of AoC 2024

// given the layout of a warehouse and the movements of a box-pushing robot inside,
// determine the final layout of the warehouse.
// then calculate the sum of all boxes' GPS coord (distance from top * 100 + distance from left)
// We've done similar problems on prior days in python, so let's try solving this one is typescript.

import * as fs from "fs";
const filename: string = "input.txt";

// for dictionary use in moveRobots()
interface Dictionary<T> {
    [key: string]: T;
}


fs.readFile(filename, "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  
  // read in and parse file
  let fileParts: string[] = data.trim().split("\n\r\n");
  let map: string[][]  = fileParts[0].split("\n")
                                     .map((lines) => lines.trim().split(""));
  let path: string[] = fileParts[1].trim().replace(/(\n|\r)/gm, "").split("");

  // move the robot along its path
  for (var i: number = 0; i < path.length; i++) {
    // find where the robot is
    // line below courtesy of https://lage.us/Javascript-Item-in-2d-Array-Using-indexOf.html
    let index: number = ([].concat.apply([], ([].concat.apply([], map))).indexOf("@"));
    let robotPos: Dictionary<number> = { x : Math.floor(index / map[0].length), y : index % map[0].length };
    moveRobot(map, path[i], robotPos);
  }

  console.log(formatMap(map));
  calcGPS(map);

});



/**
 * A recursive function to step through the robot's path and move it (and any applicable boxes) if feasible.
 * If it's not possible, just skip that step of the path.
 * @param map       : the 2D array of characters to store the warehouse map in.
 * @param direction : the direction the robot is moving in.
 * @param pos       : the position we're starting from
 * @returns whether the robot could successfully move.
 */
function moveRobot(map: string[][], direction: string, pos: Dictionary<number>) {
  // dictionary of directions
  // because of how the map is built, we check (y,x) and not (x,y)
  // the dictionary below swaps up/left and down/right to compensate
  // (awful, I know, but simpler)
  const Directions: Dictionary<Dictionary<number>> = {
    "^" : { x : -1, y : 0  },
    ">" : { x : 0,  y : 1  },
    "v" : { x : 1,  y : 0  },
    "<" : { x : 0,  y : -1 },
  }

  // move the robot
  let dir: Dictionary<number> = Directions[direction];
  let newPos: Dictionary<number> = { x : pos.x + dir.x, y : pos.y + dir.y };

  // shouldn't have to worry about out of range errors, because the map is lined with walls
  // case: facing a wall
  if (map[newPos.x][newPos.y] === "#") {
    // can't move
    return false;
  }
  // case: facing an empty space
  else if (map[newPos.x][newPos.y] === ".") {
    // move into it
    [map[pos.x][pos.y], map[newPos.x][newPos.y]] = [map[newPos.x][newPos.y], map[pos.x][pos.y]];
    return true;
  }
  // case: facing a box
  else if (map[newPos.x][newPos.y] === "O") {
    // recurse (looking for any empty space in this direction)
    if (moveRobot(map, direction, newPos)) {
      // if we can move the box, do so
      [map[pos.x][pos.y], map[newPos.x][newPos.y]] = [map[newPos.x][newPos.y], map[pos.x][pos.y]];
      return true;
    }
  }

  return false;
}



/**
 * Calculate the GPS score of the warehouse and print it
 * @param map : the 2D array of characters to store the warehouse map in.
 */
function calcGPS(map: string[][]) {
  let gps: number = 0;
  for (var i: number = 0; i < map.length; i++) {
    for (var j: number = 0; j < map[0].length; j++) {
      if (map[i][j] === "O") {
        gps += i * 100 + j;
      }
    }
  }

  console.log("GPS: " + gps);
}



/**
 * helper function to format the map for printing
 * @param map : the 2D array of characters to store the warehouse map in.
 * @returns the formatted map
 */
function formatMap(map: string[][]) {
  return map.map((lines) => lines.join(""));
}
