import com.sb224sc.people.*;

public class TestMain {
    public static void main(String[] args) {
        Person person = new Person();
        person.setFirstName("Clark");
        person.setLastName("Kent");
        person.setBirthYear(2000);

        Superman superman = new Superman();
        superman.setFirstName("Kal El");
        superman.setLastName("Kent");
        superman.setBirthYear(1985);

        Superwoman superwoman = new Superwoman();
        superwoman.setFirstName("Lois");
        superwoman.setLastName("Kent");
        superwoman.setBirthYear(1990);

        Superchild superchild = new Superchild();
        superchild.setFirstName("Jon");
        superchild.setLastName("Kent");
        superchild.setBirthYear(2015);

        System.out.println(person);
        System.out.println(superman);
        System.out.println(superwoman);
        System.out.println(superchild);
    }
}
