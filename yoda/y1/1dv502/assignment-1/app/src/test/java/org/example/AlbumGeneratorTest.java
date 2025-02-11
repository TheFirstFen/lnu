package org.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.Test;

/**
 * Test class for AlbumGenerator.
 */
public class AlbumGeneratorTest {
@Test
  public void testAlbumGenerator() {
    // Tests that the constructor and getters works correctly.
    AlbumGenerator albumGenerator = new AlbumGenerator();
    Album[] greatestAlbums = albumGenerator.generateAlbums();
    assertEquals(4, greatestAlbums.length);

    for (Album a : greatestAlbums) {
      assertNotNull(a);
      assertNotEquals("No name", a.getName());
      assertNotEquals("No artist", a.getArtist());
      assertNotEquals(-1, a.getYear());
    }
  }
}
