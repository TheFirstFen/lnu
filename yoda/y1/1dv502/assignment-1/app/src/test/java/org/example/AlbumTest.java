package org.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;



/**
 * Test class for Album.
 */
public class AlbumTest {
  
  @Test
  public void testAlbum() {
    // Tests that the constructor and getters works correctly.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    assertEquals("The Dark Side of the Moon", album.getName());
    assertEquals("Pink Floyd", album.getArtist());
    assertEquals(1973, album.getYear());
  }

  @Test
  public void testSetName() {
    // Tests that the name is set correctly.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setName("Wish You Were Here");
    assertEquals("Wish You Were Here", album.getName());
  }

  @Test
  public void testSetNameToShort() {
    // Tests that the name is set to "No name" if the name is too short.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setName("No");
    assertEquals("No name", album.getName());
  }

  @Test
  void testSetNameNull() {
    // Tests that the name is set to "No name" if the name is null.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setName(null);
    assertEquals("No name", album.getName());
  }

  @Test
  public void testSetYear() {
    // Tests that the year is set correctly.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setYear(1975);
    assertEquals(1975, album.getYear());
  }

  @Test
  public void testSetYearTooLow() {
    // Tests that the year is set to -1 if the year is too low.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setYear(1800);
    assertEquals(-1, album.getYear());
  }

  @Test
  void testSetYearTooHigh() {
    // Tests that the year is set to -1 if the year is too high.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setYear(2030);
    assertEquals(-1, album.getYear());
  }

  @Test
  public void testSetArtist() {
    // Tests that the artist is set correctly.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setArtist("The Beatles");
    assertEquals("The Beatles", album.getArtist());
  }

  @Test
  public void testSetArtistToShort() {
    // Tests that the artist is set to "No artist" if the artist is too short.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setArtist("No");
    assertEquals("No artist", album.getArtist());
  }

  @Test
  void testSetArtistNull() {
    // Tests that the artist is set to "No artist" if the artist is null.
    Album album = new Album("The Dark Side of the Moon", 1973, "Pink Floyd");
    album.setArtist(null);
    assertEquals("No artist", album.getArtist());
  }

}
