package Algorithmer;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Sum3 {
    private int[] triplets;
    private int[] id;
    private Random random;

    public void init(int size) {
        random = new Random();
        id = new int[size];
        for(int i = 0; i < size; i++) {
            int a = random.nextInt(size*10);
            int b = a - (size*5); 
            id[i] = b;
        }
    }

    public void find3sum() {
        int s = 0;
        int n = id.length;
        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                for(int k = j+1; k < n; k++) {
                    if(id[i] + id[j] + id[k] == 0) {
                        s += id[i] + id[j] + id[k]; 
                    }
                }
            }
        }
    }   
}
