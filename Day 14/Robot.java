// 20/07/2025
// mjocarroll
// Day 14 of AoC 2024

// All the methods and info we need to represent one robot

public class Robot {
    // unique id per robot
    private int id;
    // its current position - updated with each step
    private int px;
    private int py;
    // its velocity
    private int vx;
    private int vy;

    public Robot(int id, int px, int py, int vx, int vy) {
        this.id = id;
        this.px = px;
        this.py = py;
        this.vx = vx;
        this.vy = vy;
    }

    public int getPX() {
        return this.px;
    }

    public int getPY() {
        return this.py;
    }

    public int getVX() {
        return this.vx;
    }

    public int getVY() {
        return this.vy;
    }

    public void setPX(int x) {
        this.px = x;
    }

    public void setPY(int y) {
        this.py = y;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", pos: (" + px + "," + py + "), velocity: " + vx + "," + vy;
    }

    /**
     * Simulate a second of robot movement. Change px and py, wrapping around the space if needed.
     * @param height : height of the space
     * @param width  : width of the space
     * @param secs   : how many seconds of movement are happening
     */
    void move(int height, int width, int secs) {
        // System.out.println("# "+ this.id + " CURRENT PX, PY: " + this.px + ", " + this.py);

        int xShift = this.px + (this.vx * secs);
        this.px = xShift % width;
        if (this.px < 0) {
            this.px = width + this.px;
        }

        int yShift = this.py + (this.vy * secs);
        this.py = yShift % height;
        if (this.py < 0) {
            this.py = height + this.py;
        }

        // System.out.println("# "+ this.id + " XSHIFT = " + xShift + " YSHIFT = " + yShift);
        // System.out.println("# "+ this.id + " PX, PY AFTER " + secs + " SECS: " + this.px + ", " + this.py);
    }
}
