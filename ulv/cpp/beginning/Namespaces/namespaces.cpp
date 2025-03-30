#include <iostream>

namespace zero {
    int x = 0;   
}


namespace first {
    int x = 1;
}

namespace second {
    int x = 2;
}

int main() {
    // entities can have the same name in different namespaces
    // to access them, use the namespace name followed by the scope resolution operator ::
    using namespace std;

    std::cout << "x: " << zero::x << "\n";
    std::cout << "x" << first::x << "\n";
    std::cout << "x" << second::x << "\n";

    string name = "John";

    cout << "Hello " << name << "\n"; 

    return 0;
}