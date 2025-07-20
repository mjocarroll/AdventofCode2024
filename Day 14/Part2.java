// 20/07/2025
// mjocarroll
// Day 14 of AoC 2024

// I don't like this question's wording. What exact shape is a christmas tree in this context?
// Guidance for my part 2 solution taken from https://youtu.be/ySUUTxVv31U?si=BHrf1u0K8vto__-p
// In essence, given our quadrant delineation from part 1, we can guess that we can spot a christmas tree via an 
// ... unprecedented amount of robots in one quadrant

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Part2 {
    public static final int WIDTH  = 101;
    public static final int HEIGHT = 103;
    public ArrayList<Robot> robots;

    public Part2() {
        this.robots = new ArrayList<Robot>(); // maximum number of possible robots
    }

    public static void main(String[] args) {        
        if (args.length != 1) {
            System.out.println("Usage: java Part2 <filename>");
            return;
        }

        Part2 sim = new Part2();
        sim.readRobots(sim, args[0]);
        sim.findTree(sim);

    }



    /**
     * Read the robots in from the given file and store them as an array in Part1's robots field
     * @param foo      : the Part2 object representing this simulation.
     * @param filename : the name of the file to read from.
     */
    public void readRobots(Part2 foo, String filename) {
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
     * Determine the number of robots in each quadrant, then multiply those numbers together.
     * @param foo : the Part2 object representing this simulation. 
     */
    public int calcSafetyFactor(Part2 foo) {
        int q1, q2, q3, q4;
        q1 = q2 = q3 = q4 = 0;
        int xBound = (WIDTH-1)/2;
        int yBound = (HEIGHT-1)/2;

        for (int i = 0; i < foo.robots.size(); i++) {
            int x = foo.robots.get(i).getPX();
            int y = foo.robots.get(i).getPY();

            // quad 1
            if (x < xBound && y < yBound) {
                q1++;
            }
            // quad 2
            else if (x > xBound && y < yBound) {
                q2++;
            } 
            // quad 3
            else if (x < xBound && y > yBound) {
                q3++;
            }
            // quad 4
            else if (x > xBound && y > yBound) {
                q4++;
            }
        }

        return q1 * q2 * q3 * q4;
    }
    


    /**
     * PART 2
     * Iterate a second for the longest amount of time it would take a robot to return to its starting position
     * And print whatever second had the lowest safety factor
     * Therefore, its robots are the least likely to be evenly dispersed, therefore they're likely to be clustering
     * And that cluster may be a tree!
     * @param foo : the Part2 object representing this simulation.
     */
    public void findTree(Part2 foo) {
        int minSF = Integer.MAX_VALUE;
        int minIter = -1;
        System.out.println("Checking the safety factor for " + WIDTH * HEIGHT + " seconds...");
        for (int sec = 0; sec < WIDTH * HEIGHT; sec++) {
            // wait one second, then calculate the safety factor
            for (int i = 0; i < foo.robots.size(); i++) {
                foo.robots.get(i).move(HEIGHT, WIDTH, 1);
            }
            int sf = calcSafetyFactor(foo);
            if (sf < minSF) {
                minSF = sf;
                minIter = sec + 1;
            }
        }
        System.out.println("MIN SAFETY FACTOR: " + minSF + ", ITERATION: " + minIter);
    }
}
