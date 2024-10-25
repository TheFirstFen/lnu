/*
Konstruera ett program som läser in ett tal till en heltalsvariabel och sedan skriver ut talet
på skärmen, med den inledande texten: "Talet du matade in var X". Där X motsvarar det
inmatade talet. Prova att ge ett realtal som 12.345 till programmet. Vad händer?

Justera nu programmet i föregående övning, så att en teckensträng "Mata in ett tal: "
skrivs ut innan talet läses in! Observera att inläsningen av talet skall ske på samma rad
som teckensträngen "Mata in ett tal: ".

*/

#include <iostream>

int main()
{
    int x;
    std::cout << ">> ";
    std::cin >> x;

    std::cout << "Talet du matade in var " << x << std::endl;
    // tar bara in 12 då det är heltalet och datatypen för x är int
}

