package org.example;

/**
 * Time class for converting time units.
 */
public class Time {

  /**
   * Converts hours, minutes, and seconds to total seconds.
   *
   * @param hours the number of hours
   * @param minutes the number of minutes
   * @param seconds the number of seconds
   * @return the total number of seconds
   */
  public int toSeconds(int hours, int minutes, int seconds) {
    seconds += (hours * 60 * 60);
    seconds += (minutes * 60);
    return seconds;
  }
}
