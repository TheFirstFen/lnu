4. Pretty recursive print (VG)
Problemet i denna uppgift är att printa filerna med olika mellanrum beroende på "djupet" av filerna (hur många parent-folders de har).
Min lösning var att skicka den rekursiva funktion med en variabel depth, som ökar med ett när funktionen kallas rekursivt. Det gör att mellanrummet går tillbaka när funktionen går tillbaka till nästa mapp.

9. Lines of Python (VG)
I denna uppgift skulle varje rad man skrivit räknas. 
Min lösning var att leta igenom varje fil under min programmerings-mapp och där endast räkna raden ifall det fanns en giltig bokstav på raden.

12. Letter Count (VG)
Problemet i denna uppgift var att hålla koll på mängden gånger en bokstav skrivs. 
Min lösning var att använda ett dictionary med varje bokstav inlagd.
Därefter ökades dess värde varje gång bokstaven hittades i filen. Till slut omvandlades detta till ett histogram där
en stjärna representerade 100 tillfällen bokstaven hittats i filen.