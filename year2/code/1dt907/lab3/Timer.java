import java.lang.System;

// * Problem 3
public class Timer {
    private long startTime;
    private long endTime;

    public void start() {
        startTime = System.nanoTime();
    }

    public void stop() {
        endTime = System.nanoTime();
    }

    public void reset() {
        startTime = 0;
        endTime = 0;
    }

    public double getTimeInNanoSeconds() {
        if (startTime == 0 | endTime == 0) {
            throw new IllegalStateException("Timer hasn't been used.");
        }
        return endTime - startTime;
    }

    private double convertMicroSeconds(double time) {
        return time / 1_000.0;
    }

    private double convertMilliSeconds(double time) {
        return time / 1_000_000.0;
    }

    private double convertSeconds(double time) {
        return time / 1_000_000_000.0;
    }

    private double convertMinutes(double time) {
        return convertSeconds(time) / 60.0;
    }

    private double convertHours(double time) {
        return convertMinutes(time) / 60.0;
    }

    // * Send in time in ns.
    public String chooseTimePrefix(double time) {
        if (time > 60_000_000_000_000.0)
            return formatString(convertHours(time)) + " h";
        if (time > 60_000_000_000.0)
            return formatString(convertMinutes(time)) + " min";

        if (time > 1_000_000_000)
            return formatString(convertSeconds(time)) + " s";

        if (time > 1_000_000)
            return formatString(convertMilliSeconds(time)) + " ms";

        if (time > 1_000)
            return formatString(convertMicroSeconds(time)) + '\u00B5' + "s";

        return formatString(time) + " ns";
    }

    private String formatString(double time) {
        return String.format("%.4f", time);
    }
}
