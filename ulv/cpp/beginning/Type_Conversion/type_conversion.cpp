#include <iostream>

int main() {
    // Type conversion = conversion a value of one data type to another
    // Implicit conversion = automatic conversion by the compiler
    // Explicit = Precede value with new data type (int, double, char, etc.) x

    // double x = (int) 3.14;
    //char x = 100;
    //std::cout << "x: " << x << "\n";
    //std::cout << (char) 100; 

    int correct = 8;
    int question = 10;
    double score = correct / (double) question * 100;

    std::cout << score << "%";

    return 0; 
}