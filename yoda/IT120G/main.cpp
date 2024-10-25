#include <iostream>
#include <string>

using namespace std;


int main() {
    int temps[2] = {20, 30};

    struct Person
    {
        int age;
        string name;
    };
    
    Person person1 = Person();
    person1.age = 1;
    person1.name = "Bea";

    Person person2 = Person();
    person1.age = 2;
    person1.name = "Bob";

    return 0;
}
