Counting Digits: 
Tanken var att jag ska input siffran som en sträng och att jag därefter ska med hjälp av string indexing identifiera nollor, udda och jämna
tal i strängen. Jag delade in vardera del i 3 olika funktioner. Det var kanske lite onödigt att ha seperata funktioner för udda och jämna
men jag ville separera upp koden i tydliga delar. För att särskilja mellan udda och jämna tal testar jag om talet mod 2 blir 0.


Birthday Candles: 
I denna uppgift insåg jag att jag behövde hålla reda på antal candles jag hade och detta gjorde jag med en variabel som jag kallade för candle. 
Jag insåg att jag kunde använda en for-loop för att loopa genom åldrarna (for-loop pga att jag vet hur många gånger den ska loopa) och en 
while loop för att fylla på candles när de inte räcker. Genom att använda en while loop på detta sätt behövde jag inte spara antal 
resterande candles efter varje födelsedag som en seperat variabel (som i change uppgiften på assisgment 1). 


ABCD:
Svårigheten för mig i denna uppgift var att kombinera talen a, b, c och d till ett enda tal abcd. Detta löste jag med två olika funktioner,
en för abcd och en för dcba. Tex i funktionen get_abcd tänkte jag att första platsen A är en tusen tal och att andra
platsen B är en hundra tal osv. Efter att jag hade listat ut detta behövde jag använda en quadruple nested loop för att testa alla kombinationer 
av a, b, c, d för att se för vilken av kombinationen if satsen abcd * 4 == dcba stämde.


Approx pi:
Tanken var att jag ska slumpmässigt generera x och y punkter mellan 1 och -1. Dessa punkter skickar jag in i en funktion
som avgör om punkterna finns i enhetscirklen. Sättet funktionen avgör detta är att den jämför y koordinaten för punkten som jag har
genererat med den riktiga y koordinaten i enhets cirkeln för samma x värde. Tex om y koordinaten som jag har genererat är 
positiv testar jag att se om min y koordinat är mindre än den verkliga y koordinaten för samma x värde och om den är det 
är den i gränsen för enhets cirkeln. 
  

Salary Revision:
Det första jag behövde göra var att skapa en lista utav input. Detta gjorde jag med split metoden och därefter sorterade och listan och 
konverterade den till en integer lista. Jag räknade ut gap med min och max funktionen och detta fungerade då listans element var integers.
Jag delade upp median beräkningen in i 2 delar beroende på om listans längd var udda eller jämn. Jag gjorde en seperat variable för
längden/2 som jag kallade för a (a = int(len(salaries_int)//2)). Detta var för att jag märkte att jag använde detta uttryck ofta 
och koden blev därmed otroligt långt om jag inte förkortade den på något sätt. 


Drunken Sailor:
För att lösa uppgiften visualiserade jag ett xy plan. Jag började med att skapa en funktion som avgör som sailorn
hamnar i vattnet eller inte. Efter att jag hade insett att sailorn börjar i origo kunde jag därefter generera en slumpmässig
riktning som sailorn skulle gå åt och utefter riktningen som valdes uppdaterade jag positionen för sailorn. Tex start positionen
var (0,0) och om han ska gå åt vänster blir den uppdaterade positionen (-1,0). Denna process repeterade jag för totala antal steg. 
Om x eller y värdet för sailorns position någonsin blev större än gränsen k hamnar han i vattnet och funktionen returnerar ett True värde
som jag höll räkningen på. Jag repeterade sedan detta för den totala antalet sailors. 


