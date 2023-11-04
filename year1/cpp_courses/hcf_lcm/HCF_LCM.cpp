// hcf_lcm.cpp
//
// Author: Samuel Berg
// Date: 10-Sep-2019

#include <iostream>
#include <string>
using namespace std;

int main(){
    int a, b, c;
    cout << "Enter first no. : \n";
    cin >> a;
    cout << "Enter second no. : \n";
    cin >> b;

    cout << "Numbers: " << a << " and " << b << endl;
    c = a * b;
    while (a != b) {
        if(a > b)
            a = a - b;
        else
            b = b - a;
    }

    cout << "HCF = " << a << endl;
    cout << "LCM = " << c / a << endl;

    return 0;
}
