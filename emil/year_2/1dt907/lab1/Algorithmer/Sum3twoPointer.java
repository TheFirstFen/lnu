package Algorithmer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Sum3twoPointer {
    private int[] triplets;
    private int[] id;
    private Random random;
    private int size;


    public void init(int size) {
        random = new Random();
        id = new int[size];
        for (int i = 0; i < size; i++) {
            int a = random.nextInt(size * 10);
            int b = a - (size*5);
            id[i] = b;
        }
    }

    public void find3sum2pointer() {
        int s = 0;
        Arrays.sort(id);

        int n = id.length;

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && id[i] == id[i - 1]) {
                continue;
            }
        
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int total = id[i] + id[left] + id[right];

                if (total == 0) {
                    s += id[i] + id[left] + id[right];

                    while (left < right && id[left] == id[left + 1]) {
                        left++;
                    }

                    while (left < right && id[right] == id[right - 1]) {
                        right--;
                    }

                    left++;
                    right--;
                }
                else if (total < 0) {
                    left++;
                }
                else {
                    right--;
                }
            }
        }
    }
}
