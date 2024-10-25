#include "headers/gameManager.h"
#include "headers/helpers.h"

int main() {
    // generates a new random seed
    srand(time(0));
    bool restart = true;

    // starts and restarts the game
    while(restart){
        printRules();
        std::cout << "\n\n\n";
        restart = game();
        // clears the terminal
        clear();
    }
    std::cout << "Thank you for playing, come again soon :)" << std::endl;

    return 0;
}
