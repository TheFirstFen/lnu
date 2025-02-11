package org.example;

import java.util.ArrayList;

/**
 * Band class representing a musical band with albums.
 */
public class Band {
  private String bandName;
  private int startYear;
  private final ArrayList<Album> albums = new ArrayList<>();

  /**
   * Constructor to initialize the band with a name and start year.
   *
   * @param band the name of the band
   * @param startYear the year the band started
   */
  public Band(String band, int startYear) {
    setBandName(band);
    setStartYear(startYear);
  }

  /**
   * Sets the name of the band.
   *
   * @param name the name of the band
   */
  public final void setBandName(String name) {
    bandName = name;
  }

  /**
   * Sets the start year of the band.
   *
   * @param year the start year of the band
   */
  public final void setStartYear(int year) {
    startYear = year;
  }

  /**
   * Adds an album to the band's discography.
   *
   * @param albumName the name of the album
   * @param year the release year of the album
   * @param genre the genre of the album
   */
  public void addAlbum(String albumName, int year, String genre) {
    Album album = new Album(albumName, year, bandName, genre);
    albums.add(album);
  }

  /**
   * Adds an album to the band's discography without specifying the genre.
   *
   * @param albumName the name of the album
   * @param year the release year of the album
   */
  public void addAlbum(String albumName, int year) {
    addAlbum(albumName, year, "");
  }

  /**
   * Gets all albums of the band.
   *
   * @return an array of all albums
   */
  public Album[] getAlbums() {
    Album[] albumArray = new Album[albums.size()];
    for (int i = 0; i < albums.size(); i++) {
      albumArray[i] = albums.get(i);
    }
    return albumArray;
  }

  /**
   * Gets all albums of the band of a specific genre.
   *
   * @param genre the genre of the albums to retrieve
   * @return an array of albums of the specified genre
   */
  public Album[] getAlbums(String genre) {
    Album[] genreAlbums = new Album[albums.size()];
    int elements = 0;
    for (int i = 0; i < albums.size(); i++) {
      if (albums.get(i).getGenre().equals(genre)) {
        // adds the album and resizes the genreAlbums
        genreAlbums[i] = albums.get(i);
        elements++;
      }
    }
    Album[] output = new Album[elements];
    for (int i = 0; i < elements; i++) {
      output[i] = genreAlbums[i];
    }
    return output;
  }

  /**
   * Gets the start year of the band.
   *
   * @return the start year of the band
   */
  public int getYear() {
    return startYear;
  }

  /**
   * Gets the name of the band.
   *
   * @return the name of the band
   */
  public String getName() {
    return bandName;
  }

  /**
   * Gets the oldest album of the band.
   *
   * @return the oldest album
   */
  public Album getOldestAlbum() {
    Album oldest = albums.getFirst();

    for (int i = 1; i < albums.size(); i++) {
      if (oldest.getYear() > albums.get(i).getYear()) {
        oldest = albums.get(i);
      }
    }

    return oldest;
  }
}
