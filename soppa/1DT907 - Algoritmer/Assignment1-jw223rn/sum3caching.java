import java.util.List;
import java.util.ArrayList;
import java.util.Random;
import java.util.HashMap;
import java.util.Map;


public class sum3caching {
    private List<Integer> mylist;

    public sum3caching(Integer size) {
        mylist = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            int randomInt = random.nextInt(2 * size + 1) - size;
            mylist.add(randomInt);
        }
    }

    public List<List<Integer>> calc3sum() {
        Map<Integer, Integer> cache = new HashMap<>();
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < mylist.size() - 2; i++) {
            int goal = -mylist.get(i);
            Map<Integer, Integer> nextcache = new HashMap<>();

            for (int j = i + 1; j < mylist.size(); j++) {
                int needednum = goal - mylist.get(j);
                if (nextcache.containsKey(needednum)) {
                    List<Integer> templist = new ArrayList<>();
                    templist.add(mylist.get(i));
                    templist.add(needednum);
                    templist.add(mylist.get(j));
                    res.add(templist);
                }   
                nextcache.put(mylist.get(j), j);      
            }
            cache.put(mylist.get(i), i);      
        }
        return res;
    }

    public static void main(String[] args) {
        sum3caching s = new sum3caching(800);
        Runnable code = () -> s.calc3sum();
        Timeit.timeCode(code, 1, true);
    }
}
