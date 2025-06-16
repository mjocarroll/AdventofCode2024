// 16/06/2025
// mjocarroll
// Day 2 of AoC 2024

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;

import java.lang.Integer;
import java.lang.NumberFormatException;

import java.util.Arrays;

// adapting Part 1 to consider the problem dampener
// now check full record, even on a fail, to see if it can be fixed

// loop over each line, step through each number
// if ever unsafe, terminate before finishing report and go to the next

public class Part2 {
    public int safeReports = 0;
    public int totalReports = 0;   // I'm just curious

    public static void main(String[] args) {
        // 1 argument: file name
        if (args.length != 1) {
            System.out.println("Usage: java Part1 <input filename>");
            return;
        }

        Part2 Foo = new Part2();

        try {
            // read file, line by line (each line is one report)
            BufferedReader br = new BufferedReader(new FileReader(args[0]));
            String line;

            while ((line = br.readLine()) != null) {
                Foo.totalReports++;
                String[] report = line.split(" ");

                if (Foo.isReportSafe(report, true)) {
                    System.out.print("S!, ");
                    Foo.safeReports++;
                } else {
                    System.out.print("ns, ");
                }
                
            }  
            
            System.out.println("\nTOTAL REPORTS: " + Foo.totalReports + "\nSAFE REPORTS: " + Foo.safeReports);

            br.close();

        } catch (FileNotFoundException e) {
            System.err.println("File not found exception: " + e.getMessage());
        }  catch (IOException e) {
            System.err.println("IO exception: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Number format exception: " + e.getMessage());
        }

    }


    /*
     * params:
     * report   :   the items in the report as a str array
     * allow_rm :   allow a level of recursion. prevents going down to the base case     * 
     */
    public boolean isReportSafe(String[] report, boolean allow_rm) throws NumberFormatException {
        // determine whether report is safe
        // if so, incremement total counter
        int lastLevel = Integer.parseInt(report[0]);
        int currLevel;
        // need to flag whether a report is increasing or decreasing
        int incrFlag = 0;
        int decrFlag = 0;
        boolean safe = true;

        for (int i = 1; i < report.length; i++) {
            currLevel = Integer.parseInt(report[i]);

            int step = currLevel - lastLevel;
            // log if we're currently increasing or decreasing (for future checks)
            if (step < 0) { decrFlag++; }
            if (step > 0) { incrFlag++; }

            // first, check step distance is safe
            // secondly, check if this is increasing or decreasing
            if (step == 0 || Math.abs(step) > 3 || (step > 0 && decrFlag > 0) || (step < 0 && incrFlag > 0)) {
                safe = false;
                // PART 2: can't break. instead, try again to see if it passes if this element is removed
                if (allow_rm) {
                    String[] fudgedReport = new String[report.length-1];
                    // wish I could do array splicing in java
                    int k = 0;
                    for (int j = 0; j < report.length; j++) {
                        if (j != i) {
                            fudgedReport[k] = report[j];
                            k++;
                        }
                    }
                    System.out.println(Arrays.toString(report));
                    // System.out.println(Arrays.toString(fudgedReport));
                    if (isReportSafe(fudgedReport, false)) {
                        // then the record is safe without this item!
                        // just return true now
                        return true;
                    }
                }
            }

            // set lastLevel for next loop
            lastLevel = currLevel;
        }

        return safe;
    }
}