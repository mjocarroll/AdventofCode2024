// 20/07/2025
// mjocarroll
// Day 14 of AoC 2024

import java.util.ArrayList;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;

import java.lang.Integer;
import java.lang.NumberFormatException;

import java.util.regex.Matcher;
import java.util.regex.Pattern;



// given a list of robot starting positions and their velocities (how far/where they move in one second), predict where they will be in 100 secs.
// puzzle output is the "safety factor" after 100 secs: num of robots in each quadrant multiplied together


public class Part1 {
    public static final int WIDTH  = 101;
    public static final int HEIGHT = 103;
    public ArrayList<Robot> robots;

    public Part1() {
        this.robots = new ArrayList<Robot>(); // maximum number of possible robots
    }

    public static void main(String[] args) {
        /*
         * we need to:
         * - read the input file and store each robot's position and velocity
         * - be able to perform a "step" operation to change a robot's position with each second
         * - do the above for every robot for 100 seconds
         * - determine their final positions wrt each quadrant of the map
         * - calculate safety factor.
         */

        if (args.length != 1) {
            System.out.println("Usage: java Part1 <filename>");
            return;
        }

        Part1 sim = new Part1();
        sim.readRobots(sim, args[0]);
        sim.wait(sim);
        int safetyVector = sim.calcSafetyVector(sim);
        System.out.println("SAFETY VECTOR: " + safetyVector);
    }


    /**
     * Read the robots in from the given file and store them as an array in Part1's robots field
     * @param foo      : the Part1 object representing this simulation.
     * @param filename : the name of the file to read from.
     */
    public void readRobots(Part1 foo, String filename) {
        // step through and parse each line
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            String line;
            int id = 0;
            while ((line = br.readLine()) != null) {
                // match any digit with an optional hyphen before it
                Pattern pattern = Pattern.compile("-?\\d+");
                Matcher matcher = pattern.matcher(line);
                // matcher.find() should find the matches in order:
                // knowing our puzzle input, that should go px -> py -> vx -> vy
                matcher.find(); int px = Integer.parseInt(matcher.group());
                matcher.find(); int py = Integer.parseInt(matcher.group());
                matcher.find(); int vx = Integer.parseInt(matcher.group());
                matcher.find(); int vy = Integer.parseInt(matcher.group());

                foo.robots.add(new Robot(id, px, py, vx, vy));

                // System.out.println(foo.robots.get(id));
                id++;

            }
            br.close();

        } catch (FileNotFoundException e) {
            System.err.println("File not found exception: " + e.getMessage());
        }  catch (IOException e) {
            System.err.println("IO exception: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Number format exception: " + e.getMessage());
        }
    }



    /**
     * Wait 100s and update robot positions accordingly via the Robot.move() function.
     * @param foo : the Part1 object representing this simulation. 
     */
    public void wait(Part1 foo) {
        // step through each robot and have them move for 100s
        for (int i = 0; i < foo.robots.size(); i++) {
            foo.robots.get(i).move(HEIGHT, WIDTH, 100);
        }
    }



    /**
     * Determine the number of robots in each quadrant, then multiply those numbers together.
     * @param foo : the Part1 object representing this simulation. 
     */
    public int calcSafetyVector(Part1 foo) {
        // step through each robot, keeping a running total of how many crop up per quad
        int q1, q2, q3, q4;
        q1 = q2 = q3 = q4 = 0;
        // coord are 0 to n-1, not 1 to n, so boundaries are functionally -1
        int xBound = (WIDTH-1)/2;
        int yBound = (HEIGHT-1)/2;

        for (int i = 0; i < foo.robots.size(); i++) {
            int x = foo.robots.get(i).getPX();
            int y = foo.robots.get(i).getPY();
            // in a world where we didn't know the room size ahead of time, we may want to add an extra validation step here
            // ... to work out the exact boundaries depending on whether HEIGHT and WEIGHT are even or odd
            // but we know it'll always be odd

            // q1 | q2
            // -- + --
            // q3 | q4

            // quad 1
            if (x < xBound && y < yBound) {
                q1++;
                System.out.println("Robot " + i + " (" + foo.robots.get(i) + ") is in quad 1");
            }
            // quad 2
            else if (x > xBound && y < yBound) {
                q2++;
                System.out.println("Robot " + i + " (" + foo.robots.get(i) + ") is in quad 2");
            } 
            // quad 3
            else if (x < xBound && y > yBound) {
                q3++;
                System.out.println("Robot " + i + " (" + foo.robots.get(i) + ") is in quad 3");
            }
            // quad 4
            else if (x > xBound && y > yBound) {
                q4++;
                System.out.println("Robot " + i + " (" + foo.robots.get(i) + ") is in quad 4");
            }
            else {
                System.out.println("Robot " + i + " (" + foo.robots.get(i) + ") is not in a quad!");
            }
        }

        System.out.println("Q1: " + q1 + ", Q2: " + q2 + ", Q3: " + q3 + ", Q4: " + q4);
        return q1 * q2 * q3 * q4;
    }

}