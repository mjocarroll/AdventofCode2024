// 23/07/2025
// mjocarroll
// Day 15 of AoC 2024

// given the layout of a warehouse and the movements of a box-pushing robot inside,
// determine the final layout of the warehouse.
// then calculate the sum of all boxes' GPS coord (distance from top * 100 + distance from left)

// PART 2: everything except the robot are now twice as wide!
// have to compensate for moving boxes as a unit and for being able to push boxes in a tree

import * as fs from "fs";
const filename: string = "input2.txt";

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
  const Directions: Dictionary<Dictionary<number>> = {
    "^" : { x : -1, y : 0  },
    ">" : { x : 0,  y : 1  },
    "v" : { x : 1,  y : 0  },
    "<" : { x : 0,  y : -1 },
  }
  let dir: Dictionary<number> = Directions[direction];
  let newPos: Dictionary<number> = { x : pos.x + dir.x, y : pos.y + dir.y };

  if (map[newPos.x][newPos.y] === "#") return false;

  else if (map[newPos.x][newPos.y] === ".") {
    [map[pos.x][pos.y], map[newPos.x][newPos.y]] = [map[newPos.x][newPos.y], map[pos.x][pos.y]];
    return true;
  }

  // PART 2: have to consider which direction we're approaching from
  if (map[newPos.x][newPos.y] === "[" || map[newPos.x][newPos.y] === "]") {
    // whichever way we're moving, we need to check the space behind each space containing a box to move
    // (this is width == 1 when horizontal, but may be larger when moving vertically)
    if (direction === "<" || direction === ">") {
        // skip an extra spot and recurse
        if (moveRobot(map, direction, { x : newPos.x + dir.x, y : newPos.y + dir.y })) {
            [map[newPos.x][newPos.y], map[newPos.x + dir.x][newPos.y + dir.y]] = [map[newPos.x + dir.x][newPos.y + dir.y], map[newPos.x][newPos.y]];
            [map[pos.x][pos.y], map[newPos.x][newPos.y]] = [map[newPos.x][newPos.y], map[pos.x][pos.y]];
            return true;
        }
    }
    else if (direction === "^" || direction === "v") {
        // the dictionary for finding the position for another half of a box
        const BoxPair: Dictionary<Dictionary<number>> = {
            "[" : { x : 0,  y : 1  },
            "]" : { x : 0,  y : -1 },
        }
        let pair: string = map[newPos.x][newPos.y];
        let b1: Dictionary<number> = { x : newPos.x, y : newPos.y };
        let b2: Dictionary<number> = { x : newPos.x + BoxPair[pair].x, y : newPos.y + BoxPair[pair].y};
        // check the values directly forward in the next row
        if (checkValidMove(map, direction, b1, b2)) {
            moveRobot(map, direction, b1);
            moveRobot(map, direction, b2);
            [map[pos.x][pos.y], map[newPos.x][newPos.y]] = [map[newPos.x][newPos.y], map[pos.x][pos.y]];
            return true;
        }
    }
  }

  return false;
}



/**
 * A sister to moveRobot() that only checks a move's viability and doesn't move anything on the map
 * Specifically for checking if two sides of a box are both valid to move when moving vertically
 * @param map       : the 2D array of characters to store the warehouse map in.
 * @param direction : the direction the robot is moving in.
 * @param b1pos     : the position of one half of the box we're hoping to move.
 * @param b2pos     : the position of the other half of the box we're hoping to move.
 * @returns whether the given box could successfully move.
 */
function checkValidMove(map: string[][], direction: string, b1Pos: Dictionary<number>, b2Pos: Dictionary<number>) {
  // given the position of the two box halves and the row they're in, check what is directly forward of them
  // make this recursive to follow each branch, but bear in mind the map will never move
  const Directions: Dictionary<Dictionary<number>> = {
    "^" : { x : -1, y : 0  },
    ">" : { x : 0,  y : 1  },
    "v" : { x : 1,  y : 0  },
    "<" : { x : 0,  y : -1 },
  }
  let dir: Dictionary<number> = Directions[direction];
  let pushedB1: Dictionary<number> = { x : b1Pos.x + dir.x, y : b1Pos.y + dir.y };
  let pushedB2: Dictionary<number> = { x : b2Pos.x + dir.x, y : b2Pos.y + dir.y };

  // base case: either we find at least one wall (cannot move) or two free spaces (can move)
  if (map[pushedB1.x][pushedB1.y] === "#" || map[pushedB2.x][pushedB2.y] === "#") return false;
  if (map[pushedB1.x][pushedB1.y] === "." && map[pushedB2.x][pushedB2.y] === ".") return true;

  // therefore: one of the spaces to push into must contain a box
  // main concern: if any space we want to push into currently contains a box, find its pair and recurse
  // (determine whether we're pushing a full box or half a box)
  const BoxPair: Dictionary<Dictionary<number>> = {
      "[" : { x : 0,  y : 1  },
      "]" : { x : 0,  y : -1 },
  }
  // c -> contains
  let c1: string = map[pushedB1.x][pushedB1.y];
  let c2: string = map[pushedB2.x][pushedB2.y];
  if (BoxPair[c1] !== undefined && BoxPair[c2] !== undefined) {
    // work out if it's one box or two
    // pbp -> pushed box pair
    let pbp1: Dictionary<number> = { x : pushedB1.x + BoxPair[c1].x, y : pushedB1.y + BoxPair[c1].y };
    let pbp2: Dictionary<number> = { x : pushedB2.x + BoxPair[c2].x, y : pushedB2.y + BoxPair[c2].y };
    if (pbp1.x === pushedB2.x && pbp1.y === pushedB2.y && pbp2.x === pushedB1.x && pbp2.y === pushedB1.y) {
      // just one box, directly ahead
      return checkValidMove(map, direction, pushedB1, pushedB2);
    } else {
      // two boxes [][]
      return checkValidMove(map, direction, pushedB1, pbp1) && checkValidMove(map, direction, pushedB2, pbp2);
    }
  }
  // else, there's only half a box here
  if (BoxPair[c1] !== undefined) {
    let pbp1: Dictionary<number> = { x : pushedB1.x + BoxPair[c1].x, y : pushedB1.y + BoxPair[c1].y };
    return checkValidMove(map, direction, pushedB1, pbp1);
  } else if (BoxPair[c2] !== undefined) {
    let pbp2: Dictionary<number> = { x : pushedB2.x + BoxPair[c2].x, y : pushedB2.y + BoxPair[c2].y };
    return checkValidMove(map, direction, pushedB2, pbp2);
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
      // PART 2: only need to worry about left hand side of a box
      if (map[i][j] === "[") {
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
