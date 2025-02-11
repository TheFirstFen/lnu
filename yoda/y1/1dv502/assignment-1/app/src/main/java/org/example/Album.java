package org.example;

/**
 * Album class representing a musical album.
 */
public class Album {
  private String name;
  private int releaseYear;
  private String artist;
  private String genre;

  /**
   * Constructor to initialize the album with name, release year, artist, and genre.
   *
   * @param name the name of the album
   * @param releaseYear the release year of the album
   * @param artist the artist of the album
   * @param genre the genre of the album
   */
  public Album(String name, int releaseYear, String artist, String genre) {
    setName(name);
    setYear(releaseYear);
    setArtist(artist);
    setGenre(genre);
  }

  /**
   * Constructor to initialize the album with name, release year, and artist.
   *
   * @param name the name of the album
   * @param releaseYear the release year of the album
   * @param artist the artist of the album
   */
  public Album(String name, int releaseYear, String artist) {
    setName(name);
    setYear(releaseYear);
    setArtist(artist);
  }

  /**
   * Gets the name of the album.
   *
   * @return the name of the album
   */
  public String getName() {
    return name;
  }

  /**
   * Gets the artist of the album.
   *
   * @return the artist of the album
   */
  public String getArtist() {
    return artist;
  }

  /**
   * Gets the release year of the album.
   *
   * @return the release year of the album
   */
  public int getYear() {
    return releaseYear;
  }

  /**
   * Gets the genre of the album.
   *
   * @return the genre of the album
   */
  public String getGenre() {
    return genre;
  }

  /**
   * Sets the name of the album.
   *
   * @param name the name of the album
   */
  public final void setName(String name) {
    this.name = validName(name);
  }

  /**
   * Sets the release year of the album.
   *
   * @param year the release year of the album
   */
  public final void setYear(int year) {
    releaseYear = validYear(year);
  }

  /**
   * Sets the artist of the album.
   *
   * @param artist the artist of the album
   */
  public final void setArtist(String artist) {
    this.artist = validArtist(artist);
  }

  /**
   * Sets the genre of the album.
   *
   * @param genre the genre of the album
   */
  public final void setGenre(String genre) {
    this.genre = validGenre(genre);
  }

  /**
   * Checks if the genre is valid.
   *
   * @param genre the genre to validate
   * @return the validated genre
   */
  public String validGenre(String genre) {
    String result = validName(name);
    if (result.equals("No name")) {
      return "No genre";
    }
    return genre;
  }

  /**
   * Gets the title of the album.
   *
   * @return the title of the album
   */
  public String getTitle() {
    return getName();
  }

  /**
   * Checks if the album name is valid.
   *
   * @param name the name to validate
   * @return the validated name
   */
  private String validName(String name) {
    if (name == null || name.length() < 4) {
      return "No name";
    }
    return name;
  }

  /**
   * Checks if the release year is valid.
   *
   * @param year the year to validate
   * @return the validated year
   */
  private int validYear(int year) {
    if (year <= 1800 || year > 2029) {
      return -1;
    }
    return year;
  }

  /**
   * Checks if the artist name is valid.
   *
   * @param artist the artist name to validate
   * @return the validated artist name
   */
  private String validArtist(String artist) {
    String result = validName(artist);
    if (result.equals("No name")) {
      return "No artist";
    }
    return artist;
  }
}
