/*
Konstruera ett program som adderar två tal. Programmet skall först "fråga" efter talen, dvs
"Mata in tal ett: " och "Mata in tal två: ". Efter resp. fråga skall talen läsas in till varsin
heltalsvariabel. De två heltalsvariablerna skall därefter adderas och resultatet placeras i
ytterligare en heltalsvariabel för att skrivas ut på skärmen med texten: "Summan av X + Y
ar Z". Där X, Y och Z står för det första inmatade talet, det andra inmatade talet resp.
summan av de två inmatade talen.
*/

/*
Konstruera ett program som liknar det i Övning 4, men programmet skall istället utföra en
division av två reella tal. Som resultat skall följande sträng skrivas ut på skärmen: "Om du
dividerar X med Y så blir kvoten Z". Där X, Y och Z står för det första inmatade talet, det
andra inmatade talet resp. kvoten av de två inmatade talen.
*/

#include <iostream> 

int main()
{
    double X;
    std::cout << "Mata in tal ett: ";
    std::cin >> X;

    double Y;
    std::cout << "\nMata in tal 2: ";
    std::cin >> Y;

    double Z = X / Y;

    std::cout << "\nKvoten av " << X << " / " << Y << " är " << Z << std::endl;
}