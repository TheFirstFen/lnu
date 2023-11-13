Robotic Lawnmower Project Report


Projektmedlemmar: Astrid Grettve Karnehed och Gustav Pettersson
Program: Civilingenjör mjukvaruteknik
Kurs: 1DT901
Datum för inlämning av projekt: 04/11 - 2023


INTRODUKTION
Projektet handlar i stora drag om att simulera en gräsklippares rörelser under en bestämd tid. En karta över ett landområde läses in och med hjälp av en trace kan rörelserna från en gräsklipparkörning kartläggas. Projektet ingår som ett moment i kursen 1DT901.


PRESENTATION AV GROUNDMAPS

Groundmap för 'small.csv':
<img src="https://i.gyazo.com/895d84693518d948d64b95a895d8cbbd.png" width="400"/>
'small.csv' är en 30x27 groundmap (810m^2), där ungefär 74% av kartan är gräs (602m^2).

Groundmap för 'test_groundmap.csv'
<img src="https://i.gyazo.com/d9a4eb92f6f0c3385ee4139dca2ebdcc.png" width="400"/>
'test_groundmap.csv' är en helt påhittat karta som användes i början. Kartan är 4x8 (32m^2) där ungefär 72% av kartan är gräs (25m^2). En idé i början var att göra en karta av Gustavs trädgård, men detta bedömdes vara för tidskrävande.


KOORDINATKARTOR 
För att överföra kartorna från en .csv fil till en 2D lista med korrekta koordinater börjar funktionen 'coordinate_list' med att läsa in alla element i .csv filen.
<img src="https://i.gyazo.com/eea7491a478da92b295c88989a69fa47.png" width="400"/>
Alla element läggs in i en lista, och därefter används .strip och .replace för att ta bort andra symbolen som kan ha hamnat i listan. En tanke nu efteråt är att det hade antagligen varit lättare att endast lägga till 'L', 'O', 'S' ur .csv filen istället för att lägga till allt och sedan ta bort det som inte behövs.
Denna delen av koden räknar också ut antalet rader och kolumner som .csv filen har, genom att räkna antalet radbrytningar (rader) och sedan räknar ut antalet kolumner (totala antalet element/ rader). Funktionen använder detta för att sedan göra det till en 2D lista, som ännu inte har rätt koordinater. 2D listan använder sedan .replace för att byta symbolerna till siffror, för att eventuellt kunna visa kartan med färger genom matplotlib. Listan som finns vid detta tillfälle sparas som 'visualmap'.
För att få rätt koordinater i 2D listan byter den plats på första och sista, andra och näst sista, osv. Därefter byter den X värden till Y värden (ex. (1, 5) blir till (5, 1)). Listan vid detta tillfälle har rätt koordinater i listan som den har i en graf.


TRACE
Tracen tar in 2 olika listor, en med x-koordinater och en med y-koordinater. Dessa två listor kommer från 2 'for' loopar där den första har 'one_step' funktionen. 'one_step' tar in startpunktens koordinater och en velocity, vilket gör att den börjar gå diagonalt. För varje gång 'one_step' körs, skickar den ut nya koordinater som sparas i en lista. 'one_step' börjar med att testa ett nytt steg, och om detta steget är på gräs, skickas den ut. Om steget är utanför eller på ett hinder, slumpas en ny riktning, och därefter testas ett nytt steg i den riktningen. Om det steget ändå är utanför kommer en ny riktning att hittas, tills nästa steg är på gräs, då den koordinaten skickas ut.

Trace för 'test_groundmap.csv' efter 15 minuter (eftersom att kartan är mindre):
<img src="https://i.gyazo.com/5e1a72764532411f87afeda2d8b02ba5.png" width="400"/>

Trace för 'small.csv' efter 2 timmar:
<img src="https://i.gyazo.com/84cf1dc95a8220b195e6509cc97e7a99.png" width="400"/>


SLUTSATSER AV PROJEKTET/SVÅRIGHETER
Det finns ett flertal slutsatser och lärdomar som kan tas från detta projekt. Framförallt kunde en diskussion kring uppstådda problem i koden vara väldigt givande. Många gånger kunde våra kunskaper inom programmering komplementera varandra, vilket ledde till att det blev enklare att föra arbetet framåt. Ytterligare hade genomförandet av projektet kunnat underlättas om en genomtänkt planering hade tagits fram i ett tidigt stadie av projektet. Detta för att få en överskådlig bild om vilka delar av projektet som skulle kunna vara mer tidskrävande, samt att det blir enklare att fördela arbetsuppgifterna. Slutligen hade projektets hänvisade instruktioner varit bra att följa mer noggrant. Vilket främst kommer sig av att ordningen för när projektets olika delar kodas kan spela en betydande roll. Exempelvis kan det vara svårt att säkerställa att funktionen is_outside fungerar som avsett när inläsningen av en groundmap inte fungerar korrekt.


TEKNISKA SVÅRIGHETER
Gitlab är något som tagit mycket tid från projektet redan från start. Merge problem har uppstått frekvent under arbetets gång. Mot slutet av projektet användes därför seperata filer att koda i. Ytterligare en svårighet på vägen var att alltid komma ihåg att använda git pull och git push för att kunna arbeta med den senast uppdaterade koden. Många gånger kunde även koden som kodats vara onödigt komplicerad och svårförstådd, vilket kan leda till att det är svårare att gå tillbaka i koden och förstå kodens funktion. Det som kan underlätta för att undvika att detta händer är att rensa upp i koden oftare, ta bort onödiga prints och korta ner koden. Även fler funktioner och bättre variabelnamn hade gjort koden mer lättförståelig.


SAMARBETE
Dem enda delarna som vi specifikt delade upp var att Gustav började och kodade funktionen 'coordinate_list', och senare kodade Astrid 'is_outside'. Utanför detta diskuterades projektet under flera tillfällen där samarbete var fokuset istället för att dela upp specifika delar till varandra. Detta ledde till att vi alltid var på samma sida i hur koden byggdes upp och skulle användas till senare steg. Kommunikation skedde antingen på campus, både under och utanför laborationstillfällen, eller via datorn. Någon form av kommunikation om projektet skedde i princip varje dag.

Gustavs delar:
- Började projektet med att koda 'coordinate_list'
- Fixade visualisering av groundmap och trace med matplotlib
- Började one_step (Vi gjorde den tillsammans)
- Genomsnittlig tid spenderat under hela projektet är ungefär 1.5-2 timmar per dag
Astrids delar:
- Kodade delar av one_step 
- Hade hand om is_outside
- Genomsnittlig tid spenderad på projektet är omkring 1.5 timmar om dagen






