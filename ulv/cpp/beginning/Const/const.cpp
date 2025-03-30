#include <iostream>

int main() {
    // Constants are read only variables
    // They are declared using the 'const' keyword
    const double PI = 3.14159;
    double radius = 10;
    double circumference = 2 * PI * radius;

    const int LIGHT_SPEED = 299792458;
    const int WIDTH = 1920;
    const int HEIGHT = 1080;

    std::cout << "Circumference: " << circumference << "\n";

    return 0;
}