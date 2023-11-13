package algorithms;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

// * Problem 5
public class BruteForce3Sum {
    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        int len = nums.length;
        for (int i = 0; i < len - 2; i++) {
            for (int j = i + 1; j < len - 1; j++) {
                for (int k = j + 1; k < len; k++) {
                    if (nums[i] == nums[j] || nums[i] == nums[k] || nums[j] == nums[k])
                        continue;
                    if (nums[i] + nums[j] + nums[k] == 0)
                        result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                }
            }
        }

        return result;
    }
}
