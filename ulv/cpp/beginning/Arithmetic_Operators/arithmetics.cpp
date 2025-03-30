#include <iostream>

int main() {
    // arithmetic operatiors = return the result of a specific
    // arithmetic operation (+ - * /)

    // addition
    int student = 20;
    // student = student + 1;
    student += 1;
    // student++;

    //subtraction
    //student = student - 1;
    student -= 2;
    // student--;

    // multiplication
    // student = student * 2;
    student *= 2;

    // division
    // student = student / 2;
    student /= 3;

    int remainder = student % 2;

    

    std::cout << "student: " << student << "\n";
    std::cout << "remainder: " << remainder << "\n";

    return 0;
}