countdigits.py:
För att lista ut och lösa problemen används def, if-satser och while loop.
En stor mängd av siffrorna ges av användaren. Funktionen digits(d) används för att lista ut 
hur många nollor, jämna tal och udda tal som finns med i mängden där användaren gav. 
while-loopen i funktionen digits(d) beskriver en loop som isolerar nollor, jämna tal och udda tal 
av användarens mängd. För varje nolla/udda tal/jämnt tal som finns med i användarens mängd 
adderas zero, odd och even med 1 i loopen. Funktionen slutar med en returnering av 
hur många zero, odd och even som fanns med i mängden som gavs av användaren.


abcd.py:
För att lista ut och lösa problemen används def och for loop.
Funktionen get_number(a, b, c, d) är en funktion för att skapa heltalsvärde baserat på 
serie multiplikation och addition av de fyra olika värden. I funktionen beskrivs 1000*a som första
siffran i positionen, 100*b andra siffran i positionen, 10*c tredje siffran, d fjärde positionen när vi sedan
adderar de. Funktionen returnerar sedan p som är ett fyrsiffrigt heltal.
I quadruple nested loopen är a siffror mellan 1-10, b är siffror mellan 0-10, c är 0-10 och
d är 1-10. If satsen används för att visa om talet DCBA är lika med fyra gånger talet ABCD, då ska 
get_number(a, b, c, d) skrivas ut.


pi_approx.py:
För att lista ut och lösa problemen används def och for loop.
Funktionen in_circle(x, y) beräknar om en punkt är i enhetscirkeln genom att använda formeln för enhetscirkeln
och if satsen säger om en punkt är i enhetscirkeln då måste den vara mindre eller lika med 1 och där 
returnerar den True, annars False. For-loopen beräknar antalet punkter av N som är med i circle där x och y
är random siffror mellan (-1, 1). Loopen skickar dessa värden till funktionen och för varje gång
punkterna är i enhetscirkeln adderas count med 1. Count används senare för att beräkna pi m.h.a formeln
(4 * count)/N.



salary_revision.py:
För att lista ut och lösa problemen används listor.
Ett antal månadslöner ges av användaren. Först används list för att kunna läsa de separerade 
talen som skrivs av användaren. Sedan beräknas medianen beroende på om det är udda eller jämnt. 
Är det jämt då tar vi medelvärdet av de två siffrorna i mitten, annars tar vi siffran i mitten.
Average räknas fram genom att ta summan av ints och sedan dividera det med len(ints) som är
antalet heltal. Gap tas fram genom att subtrahera den största och minsta värden i ints.

