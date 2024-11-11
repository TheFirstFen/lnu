import java.util.List;
import java.util.ArrayList;

public class QUF {
    private List<Integer> mylist;

    public QUF(Integer size) {
        mylist = new ArrayList<>();
        for (Integer i = 0; i < size; i++) {
            mylist.add(i);
        }

    }
    public Boolean connected(Integer a, Integer b) {
        return root(a) == root(b);
    }
    public void union(Integer a, Integer b) {
        Integer ra = root(a);
        Integer rb = root(b);
        mylist.set(ra, rb);
    }
    public Integer root(Integer n) {
        while (n != mylist.get(n)) {
            n = mylist.get(n);
        }
        return n;
    }

    public static void main(String[] args) {
        QUF u = new QUF(8);
        System.out.println(u.mylist);
        u.union(0, 1);
        u.union(1, 2);
        System.out.println(u.mylist);
        u.union(3, 4);
        System.out.println(u.mylist);
    }
}
