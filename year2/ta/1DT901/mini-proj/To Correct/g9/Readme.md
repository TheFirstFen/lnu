
# Robotic Lawnmower Project Report 
Members: Faiyaz Muhtadee och Rodan Chahin

Program: Civilingenjör i mjukvaruteknik CIDMV

Course: 1DT901  
Date of submission: 2023-11-04

### Introduction  
Uppgiften som vi blev tilldelade var att simulera en gräsklippare. Man ska rita upp en trace med hjälp av matploblib som ska visa gräsklipparens väg igenom trädgården. I samband med detta ska man också beräkna den totala arean av gräsmattan som gräsklipparen har klippt och detta ska man även visa upp som en coverage map. 

### 1. Present Ground Maps

![Preview of smallmap](../Maps/Smallplot.png)
small.csv är en 27 x 30 m karta vilket motsvarar en total area av 810 m2. Arean av gräsmattan är 603 m2 och detta motsvarar 74% av den totala ytan. 

![Alt text](../Maps/Mymapplot.png)
mymap.csv är en 30 x 20 m karta vilket motsvarar en total area av 600 m2. Av detta är 492 m2 gräs och detta motsvarar 82% av den totala arean. 

Som inspiration till vår mymap.csv använde vi en förenklad version av Rodans hus. Den svarta rektangeln längst ner på kartan ska föreställa själva huset. De två objekten över huset ska föreställa två stycken träd. Vi tänkte att vi skulle hålla det enkelt till en början och inte överkomplicera kartan. Vi valde att sätta start positionen till nedre vänstra hörnet på kartan utav enkelhetens skull.

### 2. Coordinate Map

Till en början består vår ground map av flera listor i en stor lista. Innehållet i listorna är 0, 1 eller 2 beroende på om det ursprungligen var object, lawn eller start position. Vi insåg rätt tidigt att denna varianten inte kunde användas som en koordinat karta. Anledningen till detta var att den var omvänt. För att fixa detta problem skapade vi en funktion.

```python
def coordinates(x, y, map):
    coordinates = map[::-1]
    return coordinates[x][y]
```

I funktionen skickar vi in kartan, x och y koordinater och inuti funktionen reverse:ar den kartan och ger oss de rätta koordinaterna. Detta löste inte hela problemet för oss dock. Det som fortfarande återstod var att x och y axeln hade bytt plats. Och detta löste vi genom att skicka in koordinaterna omvänt. Kodstycket nedan visar detta:

``` python
if coordinates(y, x, map) == 0:
        return True
```
För att bestämma om en viss koordinat räknas som utanför eller inte använde vi oss av denna funktionen:

``` python
def is_outside(x, y, map):
    x = math.floor(x)
    y = math.floor(y)
    if x < 0 or x >= len(map[0]):
        return True
    if y < 0 or y >= len(map):
        return True
    if coordinates(y, x, map) == 0:
        return True
    return False
```
Det första funktionen gör är att den tar bort decimalerna från x och y koordinaterna. Om inte man gjorde såhär kunde koordinaterna inte skickas in i funktionen "coordinates". Därefter tas det reda på om koordinaterna är inom gränserna för kartan. Av detta skäl behöver man också skicka in kartan i "is_outside" funktionen. Bredden mäts av len(map[0]) och höjden mäts av len(map). Då det finns en "noll:te" ruta tex (0,0),(0,1) behöver man ha x < 0 istället för x <= 0: Den måste också räkna med att noll:te rutan är innanför. Å andra sidan ska den inte räkna med den sista positionen då det redan finns en noll:te ruta. Tex om kartan är på bredden 35 rutor lång ska x koordinaten 35 räknas som utanför då det blir den 36:te rutan. Ytterligare en if sats används för att undersöka om koordinaten är ett objekt. Lägg märke till att vi skickar in x och y omvänt av skälet jag nämnde i föregående stycke. 




### 3. Trace (Grade E requirement)

Vi använder en funktion som vi kallar movement för att skapa rörelsen och detta ritar vi därefter upp som en plot. Vi har gjort trace och coverage samtidigt. Med detta menar jag att vi i huvudsak tar trace på pixel mappen (NxN mappen). För att kompensera för en större karta gör vi hastigheten lika mycket större.

``` python
def movement(time, N, map):
    global time_count
    x, y = find_start(map)
    x_list = []
    y_list = []
    vx = 0
    vy = 0.3
    while time_count < time:
        xnew, ynew = newcoordinates(x, y, vx, vy)
        while is_outside(xnew, ynew, map):
            vinkel = random.uniform(0, 2 * math.pi)
            vx = 0.3 * N * math.cos(vinkel)
            vy = 0.3 * N * math.sin(vinkel)
            xnew, ynew = newcoordinates(x, y, vx, vy)
        x_list.append(xnew)
        y_list.append(ynew)
        x = xnew
        y = ynew
    time_count = 0
    return x_list, y_list
```
Funktionen tar de 3 parametrar, time, N och map. Den använder den globala variabeln time_count för att räkna tid. Det börjar med att den hittar start punkten genom att skanna kartan efter en 2:a (2 representerar start rutan). Vi har gjort så att gräsklipparen rör sig framåt till en början innan den träffar ett hinder. Om time_count är mindre än tiden som man anger genereras nya koordinater med hjälp av vx och vy. 

``` python
def newcoordinates(x, y, vx, vy):
    global time_count
    newx = x + vx * delta_t
    newy = y + vy * delta_t
    time_count += delta_t
    return newx, newy
```
Ett nytt x och y värde genereras med hjälp av vx och delta_ t som visat ovan. Delta_t är skillnanden i tid mellan varje rörelse. Efter att det genereras nya koordinater undersöks det ifall dessa koordinater är inom gränserna med hjälp av is_outside funktionen. Om den är ute genereras det en ny slumpmässig vinkel och därmed ny vx och vy. Sen genereras en ny punkt med den nya riktningen och så undersöks det igen om denna punkten är ute. När vi har hittat en lämplig punkt lägger vi till den i en lista och sätter x och y = de punkterna så att while loopen kan fortsätta. Slutligen sätter vi time_count till 0. Detta behövs ifall man gör flera omgångar. 

Då vi har gjort trace och coverage direkt från movement måste vi dela alla värden på N för att de ska få plats i trace plotten. Annars blir trace kartan för small.csv tex 125 x 150 med N = 5 istället för 25 x 30. Detta gör vi som nedan:

```python
smallx = [x/N for x in x_list]

smally = [y/N for y in y_list]
```

#### Trace small.csv after 2 hours
![Trace small.csv](../Maps/Tracesmall.png)

#### Trace mymap.csv after 2 hours
![Trace mymap.csv](../Maps/Tracemymap.png)

### 4. Coverage (Grade C requirement)

Coverage efter 2 timmar med en 5x5 rutnät för small.csv är ca 50% 
![Coverage small.csv](../Maps/Coveragesmall.png)

Coverage efter 2 timmar med en 5x5 rutnät för mymap.csv är ca 55% 
![Coverage mymap.csv](../Maps/Coveragemymap.png)

Om man hade ökat ∆t kommer coverage att minska. ∆t är hur ofta gräsklipparen uppdaterar sin position och om den ökas kommer sannolikheten att gräsklipparen hoppar öven en position att öka. Dvs även om den går igenom en ruta kan det vara så att rutan inte räknas med som täckt. Om man däremot minskar ∆t kommer coverage att öka för att den kommer uppdatera sin position oftare och sannolikheten att den missar en ruta som den har gått över minskar. Om man ökar N kommer coverage att också minska. Detta kan ses som att gräsklipparen blir mindre på storleken och täcker därmed mindre yta för varje steg.

Det mest realistiska hade varit N = 2 om man antar att varje ruta är 1 kvadrat meter. Jag gör antagandet att en gräsklippare har en bredd på en halv meter när jag tar denna slutsats. Om den hade varit mindre än detta hade det inte varit lika effektivt. Den hade varit mindre och haft mindre batteri också. 

Det hade varit bra om gräsklipparen hade kunnat arbeta omkring 3 timmar per dag. Gräset är ca 95% klippt efter 9 timmar och om vi antar att gräset växer tillbaka helt efter en veckas tid så borde 3 timmars arbets dag vara perfekt för gräsklipparen. Helst vill man att den ska arbeta så få dagar som möjligt då det kan ske mycket oförväntat. Tex kan det börja regna under 3 av dagarna och under dessa dagar är det inte optimalt för den att klippa. Men man måste ta hänsyn till att dens batteri inte håller så länge och då blir 3 timmar om dagen i 3 dagar perfekt för den. 

### 5. Multiple Simulations (Grade B requirement)

Detta är vår funktion för att simulera fler omgångar:

``` python
def many_runs(map, num, N, time):
    per_list = []
    for i in range(num):
        xlist, ylist = movement(time, N, map)
        cov = coverage(map, xlist, ylist)
        per = get_percentage(map, cov)
        per_list.append(per)
    average = np.mean(per_list)
    standard_deviation = np.std(per_list)
    print(round(average, 1), "±", round(standard_deviation, 1))
    print(per_list)
```
På small.csv får vi efter 10 omgångar med N = 5 och 2 timmars tid resultatet = 48.1 ± 0.9. 

48.1 är genomsnittet i procent och standard avvikelsen ligger på 1%. 

På mymap.csv får vi efter 10 omgångar med N = 5 och 2 timmars tid resultatet = 55.4 ± 0.7

55.4 är genomsnittet i procent och standard avvikelsen ligger på 0.7%. 

För att beräkna hur mycket tid som behövs för 90% coverage justerade jag funktionen ovan till att beräkna tid istället. Den ser ut såhär:

```python
def time_for_90(map, num, N):
    per_list = []
    
    for time in range(7200, 100000, 3600):
        for i in range(num):
            xlist, ylist = movement(time, N, map)
            cov = coverage(map, xlist, ylist)
            per = get_percentage(map, cov)
            per_list.append(per)
            average = np.mean(per_list)
            per_list = []
        if average >= 90:
            return time
```
På small.csv returnerade den tiden 8 timmar och på mymap.csv returnerade den 6 timmar.

## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming?
- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
- How could the results be improved if you were given a bit more time to complete the task.

Vårt största tekniska problem var att beräkna coverage. Det tog lång tid för oss att lista ut hur man skulle dela in kartan in i mindre bitar. Efter att vi hade listat ut det där fastnade vi igen ett tag då vi inte insåg vad nästa steg var. Vi klurade ut det tillslut efter mycket diskussion. En annan problem vi hade var att vi till en början inte använda oss utav delta_t och detta ledde till att gräsklipparen hoppade över flera rutor. 

Vi lärde oss mycket om samarbete och speciellt hur man använder gitlab på ett bra sätt för att sammarbeta. Vi förbättrade också vår problemlösning strategi då vi under ett flertal gånger fastnade och behövde klura ut hur man skulle göra näst. För oss var penna och papper det som hjälpte oss lösa majoriteten av våra tekniska problem. Om vi bemöter ett liknande problem nu kommer vi till en början att försöka diskutera ihop det tillsammans och tänka ut en lösning innan vi börjar koda. Såklart kan man testa lite men man borde tänka innan man börjar koda. 

Om vi hade lite mer tid hade vi nog satsat på A nivån och försökt förbättra gräsklipparens bounce mekanism. Vi hade behövt testa flera olika bounce mekanismer för att hitta en som hade kunnat ge bättre coverage. Vi hade också försökt simulera att gräset växer.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.
 	* Estimate hours spend each week (on average)
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.

Vi gjorde majoriteten av arbetet tillsammans. Ibland hände det att vi inte kunde ses men då använde vi oss utav slack/discord för att ändå arbeta tillsammans. Vi pratade ofta om projektet och våra planer kring den. 

Faiyaz:
Jag gjorde majoriteten av det matematiska tex beräkningar kring movement och coverage. Det var också jag som gjorde mycket av det praktiska kodningen. Det hände ofta att jag fastnade på en viss del och då inventerade Rodan en kreativ lösning som jag kodade. Jag tror att jag totalt lade omkring 30 timmar. 


Rodan: 
Jag gjorde majoriteten av det visuella arbetet. Tex fixade jag arbetet kring matplotlib och hur vi använde den för att visuelisera olika delar. Det var oftast jag som listade ut de kreativa lösningarna när vi stötte på ett problem på vägen. Jag lade omkring 30 timmar också på projektet. 

Det största vi lärde oss är att man inte ska kasta sig in i ett problem. Man ska istället fundera lite innan och diskutera ihop det med varandra. Till en början gjorde vi inte detta men mot slutet insåg vi bägge två hur viktigt det är att sitta och klura med penna och papper innan man skriver ner koden. Till nästa projekt kommer vi också vara lite försiktigare efter att vi har gjort klart en del. Ibland hände det att vi gick vidare till nästa del utan att till 100% kontrollera att föregånde del fungerade. I slutändan blev konsekvenserna av detta att man fick lägga mer tid än förväntat på att troubleshoota. 
