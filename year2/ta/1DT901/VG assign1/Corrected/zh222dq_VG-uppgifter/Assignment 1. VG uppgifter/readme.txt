sumofthree.py:
För att lista ut och lösa problemen används modulus(%) och heltalsdivision(//).
Användaren skriver tre nummer.
Siffran till höger isoleras m.h.a modulus(%10). 
Siffran i mitten isoleras m.h.a heltalsdivision(//10) och sedan multiplicerad med modulus(%10). 
Siffran till vänster isoleras m.h.a heltalsdivision (//100)


 change.py:
För att lista ut och lösa problemen används modulus(%) och heltalsdivision(//).
Price och payment ges av användaren. Change (summan man får tillbaka) tas fram genom att 
subtrahera payment med price.
(a, b ,c, ..., j) beskriver svenska kronor som är allt mellan 1000kr till 1kr. 
Första alfabetet beskriver den största sedeln och sista alfabetet beskriver den minsta sedeln.
För att få fram hur många sedlar change motsvarar används heltalsdivision mellan change och sedlar.
Modulus används för att ta redan på hur mycket change som är kvar inför nästkommande steg.


 tax.py:
För att lista ut och lösa problemen används if satser.
Månadsinkomsten ges av användaren. För att lista ut hur många procent skatt som ska dras av inkomsten
används if satser. Om skatten är lägre än 30%, då multipliceras månadsinkomsten med 0.30.
Om skatten är mellan 50000 och 38000 då subtraheras månadsinkomsten med 38000. Sedan 
multipliceras summan av det med 0.35. Resten tas fram genom att multiplicera 38000 med 0.30.
Resten och skatten adderas för att ta reda på den slutliga skatten.
Samma metod appliceras på vidare steg.

 squarecolor.py:
 För att lista ut och lösa problemen används if satser, modulus och string indexing.
Chess square identifier ges av användaren. String indexing används för att isolera 
alfabetet samt siffran. Modulus används för att lista ut om siffran är udda eller jämnt.
Om alfabetet är a, c, e eller g och är udda då är spelaren på en svart ruta.
Annars om alfabetet är a, c, e eller g och är jämnt då är spelaren på en vit ruta.
Samma metod har tillämpats på b, d, f och h.

