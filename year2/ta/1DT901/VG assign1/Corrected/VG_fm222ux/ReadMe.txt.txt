Sum of three:
Tanken var att jag ska separera de 3 talen för att sedan lägga ihop dem. Sista talet kan 
separeras med modulo 10. Andra siffran tar jag reda på genom att utföra heltals division 
med 10 och sedan ta mod 10. För att få första siffran tar man heltals division med 100. 

Change:
För att ta reda på vilka sedlar som ska användas använde jag heltals div tex(Antal 1000 kr sedlar = Change//1000).
På detta sätt får man reda på hur många 1000 kr sedlar får plats i variabeln change. Därefter räknade jag ut
resten som fanns kvar efter att 1000 kr får plats med hjälp av mod och repeterade denna process för varje typ av sedel. 

Taxes:
Tanken var att separera de 3 inkomst kategorierna med en if sats. Inkomst under 38 000 multiplicerades enbart med 0.3.
För inkomst över 38000 tilllämpades en extra skatt. Man behövde allstå räkna med vanliga skatten och utöver den 
lägga till en extra avgift på summan mellan 50000 och 38000 (50000 - 38000). Jag gjorde samma med det sista alternativet (inkomst över 50000). 

Squarecolor:
Tanken var att separera de olika utfallen med if satser. Jag insåg från början att man skulle behöva ha ytterligare en if sats inuti en if sats. 
Jag såg snabbt ett mönster i schackbrädan där kolumn a, c, e och g hade jämna tal på vita squares. Motsatsen gällde för b,d,f,h
där de jämna talen var svarta squares. Med indexing läste jag av position 0 och fick reda på vilken bokstav det var och därefter om siffran i position 
1 går att dela på 2 eller inte. På så sätt kunde jag urskilja om det var svart eller vitt. 



