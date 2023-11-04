// math.cpp
//
// Author: Samuel Berg
// Date: 10-Sep-2019

#include <iostream>
using namespace std;

int main(){

    int dividend = 14; //cin <<;
    int divisor = 3; //cin <<;

    int quotient;
    int remainder;

    quotient = dividend / divisor;
    remainder = dividend % divisor;

    cout << "Quotient = " << quotient << endl;
    cout << "Remainder = " << remainder;

    return 0;
}
