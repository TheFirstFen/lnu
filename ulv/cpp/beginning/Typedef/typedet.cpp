#include <iostream>
#include <vector>

// typedef std::vector<std::pair<std::string, int>> pairlist_t;
// typedef std::string text_t;
// typedef int number_t;
using text_t = std::string;
using number_t = int;

int main() {
    /* typedef = reserved keyword used to create an additional name
                 (alias) for another data type.
                  New identifier for an existing type
                  Helps with readability and reduces typos
                  Use when there is a clear benefit
                  Replaced with 'using' (work better w/ templates)
    */

    // std::vector<std::pair<std::string, int>> parilist1;
    // pairlist_t parilist2;

    // std::string firstname = "John";
    text_t firstname = "Doe";

    number_t x = 5;

    std::cout << "firstname: " << firstname << "\n";
    std::cout << "x: " << x << "\n";
    return 0;
}