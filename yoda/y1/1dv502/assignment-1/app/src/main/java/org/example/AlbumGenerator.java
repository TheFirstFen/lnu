package org.example;

/**
 * AlbumGenerator class for generating a list of albums.
 */
public class AlbumGenerator {

  /**
   * Generates an array of albums.
   *
   * @return an array of albums
   */
  public Album[] generateAlbums() {
    Album[] albums = new Album[4];
    String[] names = {"A New Hope", "The Empire Strikes Back", 
                      "Return of the Jedi", "The Phantom Menace"};
    String[] artistNames = {"John Williams", "John Williams", "John Williams", 
                            "John Williams"};
    int[] releaseYears = {1977, 1980, 1983, 1999};

    for (int i = 0; i < albums.length; i++) {
      Album a = new Album(names[i], releaseYears[i], artistNames[i]);
      albums[i] = a;
    }

    return albums;
  } 
}
