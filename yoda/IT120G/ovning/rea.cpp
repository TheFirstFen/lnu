/*
Konstruera ett program som beräknar priset på en rabatterad vara. Till programmet skall
först varans pris före rabatten anges och därefter varans rabatt i procent. Välj själv
lämpliga inledande texter för inmatning av de två värdena. Programmet skall som resultat
ge följande utskrift på skärmen:

Pris före rabatt : 102.50 Kr
Rabatt i procent : 17
Pris efter rabatt: 85.07 Kr
*/

#include <iostream>

int main()
{
    float beforeSale = 102.50;
    float percentage = 17/100;
    float priceAfterSale = beforeSale * percentage;

    std::cout << "Price after sale " << priceAfterSale;
}
