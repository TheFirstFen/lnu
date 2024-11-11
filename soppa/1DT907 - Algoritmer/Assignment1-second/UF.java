package Assignment1;

import java.util.ArrayList;
import java.util.List;

public class UF {
    private List<Integer> mylist;

    public UF(Integer size) {
        mylist = new ArrayList<>();
        for (Integer i = 0; i < size; i++) {
            mylist.add(i);
        }

    }
    public Boolean connected(Integer a, Integer b) {
        return a == b;
    }
    public void union(Integer a, Integer b) {
        Integer a_id = mylist.get(a);
        Integer b_id = mylist.get(b);

        Integer i = 0;
        for (Integer n : mylist) {
            if (n == a_id) {
                mylist.set(i, b_id);
            }
            i ++;
        }
    }

    public static void main(String[] args) {
        UF u = new UF(8);
        System.out.println(u.mylist);
        u.union(0, 1);
        u.union(6, 7);
        System.out.println(u.mylist);
        u.union(1, 2);
        System.out.println(u.mylist);
    }

}