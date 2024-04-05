# Robotic Lawnmower Project Report 
Members: ALaa Daeef och Sofia Emma Ashley Svensson
Program: Master of Science in Engineering: Software Engineering,
Course: 1DT901  
Date of submission: 2023-11-03

### Introduction  
Detta programmeringsprojekt fokuserar på att simulera rörelsen hos en robotgräsklippare och att uppskatta området för gräsklippning efter en viss tid. Simuleringen är baserad på en markkarta representerad av en CSV-fil, där olika symboler indikerar gräsytor, hinder och robotens startpunkt. Robotens rörelse simuleras genom att generera slumpmässiga hastigheter och ta steg tills den träffar ett hinder eller når kartgränsen. När ett hinder påträffas ändrar roboten riktning genom att generera en ny slumpmässig hastighet. Simuleringen producerar ett spår av robotens rörelser, och varje körning av simuleringen resulterar i ett annat spår på grund av hastighetsvalets slumpmässiga natur. Målet är att analysera och visualisera spåren för att uppskatta mängden gräs som klippts av gräsklipparen över tid.

### 1. Present Ground Maps
Båda katorna representerar ett rutnätsliknande område med olika symboler som indikerar olika element. Här är en förklaring för symbolerna som används på kartan:
"L" representerar gräset.
"O" representerar ett hinder. 
"S" representerar startpositionen. 

Small.csv: 
Kartarea = 30 * 30 = 900 m^2
Gräsarean = Antal "L" = 694, (694/900) * 100 = 77,11%

My_map.csv:
Kartarea = 40 * 40 = 1600 m^2
Gräsarean = Antal "L" = 1353, (1353/1600) * 100 = 84,56%


### 2. Coordinate Map
convert_ground_map är en funktion som tar in en lista som representerar en markkarta med symboler. Den omvandlar varje symbol i kartan till ett motsvarande heltal och returnerar en ny lista med dessa heltal som representerar markkartan.

is_outside är en funktion som tar in koordinaterna x och y, samt en markkarta ground_map. Den avrundar koordinaterna till heltal och kontrollerar sedan om de är utanför markkartans gränser eller om marktypen vid den avrundade positionen är hinder (2). Funktionen returnerar True om koordinaterna är utanför gräsmattan eller om marktypen är ett hinder, annars returnerar den False.

### 3. Trace (Grade E requirement)
Koden simulerar rörelsen av ett objekt i en tvådimensionell miljö. Här är en detaljerad förklaring steg för steg:

1. Funktionen `one_step(x, y)` genererar en slumpmässig vinkel `a` och beräknar hastigheten i x- och y-riktning (`Vx` och `Vy`) baserat på den slumpmässiga vinkeln.

2. Listorna `ls_x` och `ls_y` skapas för att lagra koordinaterna för objektets position under simuleringen.

3. Funktionen `movement(x, y, ground_map)` tar in startpositionen för objektet (`x` och `y`) och kartan över terrängen. Sedan utförs följande steg i en loop med 90000 iterationer:
    En ny position (`Xn`, `Yn`) beräknas genom att addera den tidigare positionen med hastigheten i x- och y-riktning (`Xf` och `Yf`).

    Om objektet inte är utanför kartan (`is_outside(Xn, Yn, ground_map) is False`), läggs den nya positionen till i listorna `ls_x` och `ls_y`.

    Om objektet är utanför kartan (`is_outside(Xn, Yn, ground_map) is True`), justeras positionen tillbaka till en giltig position genom att använda den föregående positionen (`Xb` och `Yb`) och en ny slumpmässig rörelse genererad av `one_step`-funktionen.

4. Efter loopen returneras listorna `ls_x` och `ls_y`, vilket representerar objektets simulerade rörelse över tiden. 


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
1. Det svåraste som vi hade problem med var att göra trace att funka på ett sätt så att det skulle gå överallt i kartan och att inte gå över hindrarna. Den som tog mest tid var att skapa kartan för att vi förstodde inte riktigt från början att det fanns ett annat sätt än att skriva allting för hand.

2. Vi har lärt oss att bara testa fram hela tiden och att det tar mycket tid för att komma fram till resultatet som man vill. Den som vi skulle ha gjort annorlunda är att planera mer så man blir inte stressad på sista veckan när man ska ha presentationen.

3. Om vi hade mer tid vi skulle ha gjort coverage och vi hade tänkt oss innan en ide för att förbättre trace så att det skulle går rakt istället för en vinkel hela tiden och om vi har gjort det, coverage blir säkert 100% beroende av tiden såklart.

### Project issues

1. Vi tyckte att vi jobbade bra tillsammans, vi forstod varandra och det fanns absulot inga problem förutom med koden ibland och vi träffades nästan varje dag för att diskutera hur vi kan skriva koden och förbättra det på ett enklare sätt.

2. - Vi jobbade tillsammans och diskuterade hur man gör kartan och båda testade fram för trace. Vi var alltid tillsammans när vi jobbade med projekten så vi spenderade samma tid på det och vi skulle säga nästan 12h per vecka.

3. Vi tycker att diskutera är verkligen det bästa sättet att lösa projektet och om vi skulle ha haft en liknande projekt, vi skulle säga att lägga mer tid på det.
