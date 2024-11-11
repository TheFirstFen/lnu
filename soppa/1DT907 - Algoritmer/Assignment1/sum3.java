package Assignment1;

import java.util.List;
import java.util.ArrayList;
import java.util.Random;
public class sum3 {
    List<Integer> mylist;

    public sum3(Integer size) {
        mylist = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            int randomInt = random.nextInt(2 * size + 1) - size;
            mylist.add(randomInt);
        }
    }

    public List<List<Integer>> calc3sum() {
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < mylist.size() - 2; i++) {
            for (int j = i + 1; j < mylist.size() - 1; j++) {
                for (int v = j + 1; v < mylist.size(); v++) {
                    int num1 = mylist.get(i);
                    int num2 = mylist.get(j);
                    int num3 = mylist.get(v);

                    if (num1 + num2 + num3 == 0) {
                        List<Integer> nums = List.of(num1, num2, num3);
                        res.add(nums);
                    }
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {


        sum3 s = new sum3(800);
        Runnable code = () -> s.calc3sum();
        Timeit.timeCode(code, 1, true);
    }
}
