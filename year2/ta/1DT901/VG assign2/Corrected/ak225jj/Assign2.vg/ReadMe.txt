    countdigits.py
Jag börjar med att läsa in av inputen som en sting, för att sedan 
kunna läsa av alla siffror var för sig i for loopen.
Precis innan loopen har jag en count för alla nollor, udda- och jämna tal. 
I loopen gör jag om varje tecken var för sig till en integer. När varje 
tecken är en integer, går de igenom if, elif och else satserna och fastnar
de i en av de adderas det på ett på respektive count.

    birthday_candles.py
Börjar med att göra en count för totala antalet boxar med ljus som kommer 
att behövas, samt antalet ljus. Efter det jör jag en for loop för intervallet
1 till 101 (eftersom den då slutar räkna vid 100) samt en count för antalet
öppnade boxar. Innuti for loopen lägger jag till en while loop där 
jag använder mig utav candles och open_box counten. Så länge antalet ljus är
färre än antalet fyllda år, lägg till 24 ljus på ljus counten.
Utanför while men innanför for beräknar jag antalet ljus som finns kvar samt
totala antalet boxar. Sedan printar jag det som ska beräknas från noll till
100 i for loopen och beräkningen utav totalet antalet boxar som använts
samt antalet ljus som finns kvar.

    abcd.py
Skapar först en funktion med variablerna: a, b, c, d som givet i uppgiften
som returnerar a värdet multiplicerat med 1000 adderat med b värdet 
multiplicerat med 100 addeat med c multiplicerat med 10 och sist adderat med
d. Efter det skapar jag en variabel max_value som jag tilldelar värdet 9. 
Sedan skapar jag fyra for loopar innuti varandra för värdena a till d, 
som vardera har ett givet intervall. Där efter skapar jag en variabel  som
ger ett nummer med alla möjliga sifferkombinationer i ordningen: a, b, c, d
samt en variabel j med alla möjliga sifferkombinationer i ordningen: 
d, c, b, a. Sist skapar jag en if sats som printar värdet i multiplicerat
med 4 som är lika med just det värdet j.

    pi_approx.py
Börjar med att importera funktionerna: math och random. 
Eftersom 100, 10 000 och 1 000 000 alla går att skriva som 100 upphöjt till
ett tal "to_the_power" (1 till 3), sätter jag första variabeln n=100 i en for
loop. Innuti den sätter jag en ny for loop som kommer slumpa n antal punkter
på linjerna x och y som har det givna intervallet (-1, 1). I loopen gör jag
en variabel p som avstånded från origo till alla punkter. Därefter använder
jag en if sats för att: för alla punkter "p" som befinner sig i intervallet 
(-1, 1), som är radien av cirkeln, ska addera 1 på en count tot_points. 
För att sedan beräkna det ungefärliga värdet på pi: multiplicerar jag arean
av kvadraten med tot_points och dividerar det med n (antalet punkter). 
Eftersom diffen mellan det ungefärliga pi värdet och det riktiga pi värdet 
går att räkna ut genom att subtraherat pi med det ungefärliga pi värdet,
tar jag absolutbeloppet av diffen (ifall diffen skulle bli negativ). 
Där efter printar jag resultatet.

    salary_revision.py
Börjar med att läsa av inputen som en sting för att sedan splitta strängen,
göra om den till flera integers och sedan sortera den från lägsta 
till högsta värde. För att berkäkna medianen använder jag mig utav integer 
division i en if sats. Där ifall antalet löner är udda blir medianen längden 
på listan med löner heltalsdividerat med två. Annars i else satsen blir 
medianen (ifall antalet löner är jämn) blir medianen värdet av: längden på
listan heltalsdividerat med två, adderar med längden på listan 
heltalsdividerat med två subtraherat med 1 och sedan dividerat med två.
För att beräkna medellönen summerar jag lönerna och dividerar summan med 
antalet löner. Efter det beräknar jag gappet mellan lönerna och det gör jag
genom att subtrahera max lönen med min lönen. Sist printar jag resultatet. 

    drunken_sailor.py
Först importerar jag random. Eftersom man kan skildra riktingarna på steg 
en drunken sailor kan ta med ett kordinatsystem skapar utgår jag från att 
en  drunken sailor antingen kan ta steg i x-led eller y-led. Därför skapar
jag en funktion man_over_board som returnerar värder på x och y om de 
befinner sig i intervallet size (givet från inputen). 
Efter det tilldelas variablerna: size, steps och sailiors från en input. 
Med de givna variablerna använder jag mig utav en for loop med antalet 
"sailiors". I den loopen har jag ytterligare en for loop för antalet steg.
Stegriktningarna slumpas med ranint i intervallet (o, 3) där olika 
variabler för steg adderas med 1 beroende på vilket slumpässigt värde 
variabeln steg får. Sedan skapar jag en if sats utanför den andra for loopen
som säger att ifall inte funktionen gäller ska en count "water" adderas 
med 1, eftersom det betyder att drunken sailior då har ramlat ner i vattnet. 
Där efter beräknar jag procentantalet av drunken sailiors som trillat ner i 
vattnet och sist printar jag resultatet. 
