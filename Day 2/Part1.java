// 16/06/2025
// mjocarroll
// Day 2 of AoC 2024

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;

import java.lang.Integer;
import java.lang.NumberFormatException;

// determine how many reports are safe from input.txt

// loop over each line, step through each number
// if ever unsafe, terminate before finishing report and go to the next

public class Part1 {
    public static void main(String[] args) {
        // 1 argument: file name
        if (args.length != 1) {
            System.out.println("Usage: java Part1 <input filename>");
            return;
        }

        try {
            // read file, line by line (each line is one report)
            BufferedReader br = new BufferedReader(new FileReader(args[0]));
            String line;
            int safeReports = 0;
            int totalReports = 0;   // I'm just curious

            while ((line = br.readLine()) != null) {
                totalReports++;

                // determine whether report is safe
                // if so, incremement total counter
                String[] report = line.split(" ");
                int lastLevel = Integer.parseInt(report[0]);
                int currLevel;
                // need to flag whether a report is increasing or decreasing
                int incrFlag = 0;
                int decrFlag = 0;
                boolean safe = true;

                for (int i = 1; i < report.length; i++) {
                    currLevel = Integer.parseInt(report[i]);

                    // first, check step distance is safe
                    int step = currLevel - lastLevel;
                    if (step == 0 || Math.abs(step) > 3) {
                        System.out.print("Not safe, ");
                        safe = false;
                        break;
                    }

                    // log if we're currently increasing or decreasing (for future checks)
                    if (step < 0) { decrFlag++; }
                    if (step > 0) { incrFlag++; }

                    // secondly, check if this is increasing or decreasing
                    // if we've done the opposite before, this isn't safe
                    // (step is negative if we're decreasing, positive if increasing)
                    if ((step > 0 && decrFlag > 0) || (step < 0 && incrFlag > 0)) {
                        System.out.print("Not safe, ");
                        safe = false;
                        break;
                    }

                    // set lastLevel for next loop
                    lastLevel = currLevel;
                }

                if (safe) {
                    System.out.print("Safe!, ");
                    safeReports++;
                }
            }  
            
            System.out.println("\nTOTAL REPORTS: " + totalReports + "\nSAFE REPORTS: " + safeReports);

        } catch (FileNotFoundException e) {
            System.err.println("File not found exception: " + e.getMessage());
        }  catch (IOException e) {
            System.err.println("IO exception: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Number format exception: " + e.getMessage());
        }

    }
}