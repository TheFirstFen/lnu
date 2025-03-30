#include <iostream>

int main() {
    // integer
    int x; //declaration
    x = 5; //assignment
    int y = 6;
    int sum = x + y;

    // double
    double pi = 3.14;
    double radius = 2.0;

    // character
    char grade = 'A';
    char initial = 'B';

    // boolean
    bool student = false;
    bool power = true;

    // string
    std::string name = "John";
    std::string day = "Friday";

    std::cout << "x: " << x << "\n";
    std::cout << "y: " << y << "\n";
    std::cout << "sum (x+y): " << sum << "\n";
    std::cout << "pi: " << pi << "\n";
    std::cout << "radius: " << radius << "\n";
    std::cout << "grade: " << grade << "\n";
    std::cout << "initial: " << initial << "\n";
    std::cout << "student: " << student << "\n";
    std::cout << "power: " << power << "\n";
    std::cout << "name: " << name << "\n";
    std::cout << "day: " << day << "\n";

    return 0;
}