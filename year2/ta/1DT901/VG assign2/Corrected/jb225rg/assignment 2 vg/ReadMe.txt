
Counting digits - Jag gjorde en for-loop som gick igenom alla enskilda siffror i talet och sedan kollade
                  om det var udda, jämnt eller noll. Därefter adderade den en till en 'counter' som höll 
                  på antalet av olika sortes talen.

Birthday Candles - Jag skapade variabler för ljus, boxar, ålder, ålder nu och en som räknar antalet boxar.
                   Jag använde mig av en for loop för som gick igenom varje år. Om vi redan hade 
                   tillräckligt med ljus från ett tidigare år så användes bara dem ljusen. Men om det inte
                   fanns tillreckligt så fick man köpa boxar. Då gjorde jag en while-loop som itererade 
                   tills det fanns tillräckligt med ljus för den nuvarande åldern. Där fanns också en 
                   variavel som räknade antalet köpta boxar. Efter varje år så subtraherade jag antalet
                   ljus som var lika med ålders från hur många ljus jag hade.


ABCD - Jag använde mig av nestlade for-loopar för att hitta dem olika numrena. For-looparna för A och D
       var mellan numrena 1-9 då dem inte fick vara 0, medans C och D var emellan 0-9. Sedan i sista
       for-loopen använde jag mig av en if-sats som var san om 4*ABCD == DCBA, och då skrev ut dem talen
       gjorde det sant.

Calculating Pi - Vi ska räkna fram en aproximation på pi för n = 100, 10000 och 1000000. Jag valde att
            skapa en for-loop som gick mellan numrena 1-4 och sen sätta n=100**(numret i for-loopen) för
            på det sätte få n att vara 100**1, 100**2 och 100**3. Efter det hade jag ytterligare en 
            for-loop som tog fram en punkt i form av ett x- och ett y-värde och senare räknade ut deras 
            avstånd fråt origo (0, 0) genom att ta sqrt(x**2 + y**2). Om det är längre än 1 så ligger 
            punkten utanför våran cirkel. De antalet punkter vars avstånd < 1 räknas och antalet lagras.
            Efter det så räknade jag ut hur många av punkterna som hamnade innuti cirkeln delat med det
            totala antal punkter. Produkten av det multiplicerat med 4 blir våras pi-aproximtion. 
            Tillslut så tar jag faktiska pi minus aproximationen och tar absolutbeloppet av det flr att 
            se hur långt ifrån faktiska pi som aproximationen va.

Salary - Jag lagrade de avlästa talen och använde .slpit() för att sedan lägga in talen som ints i en ny
         lista. Jag gjorde funktioner som räknade ut de olika värdena vi ville ha. En för 'average' som
         tar summan av talen delat på antal tal, 'gap' som tar största minus minsta och sist medianen som 
         först sorterar listan i storleksordning för att den plocka it talen i mitten. Om det var ett 
         jämns antal tal så tog den medelvärdet av dem två i mitten.

Drunken Sailor - Jag använde mig av en lista med två värden för att hålla koll på x och y värdena. En 
                 lista för storleken av 'the grid' och sedan en ny som hökk koll på sjömannens position.
                 Jag hade en for-loop för alla sjömän som också återställde positionen i 'the grid'
                 till (0, 0) för varje ny sjömn. sen innuti denna for-looprn hade jag en annan for-loop 
                 som itererade för varje steg sjömännen skulle ta. För att slumpa fram stegen så valde 
                 jag att göra en lista med talen 1-4 och sedan låta datorn slumpa ett av dessa talen med
                 random.choice() och sen beroende på vilket tal som valdes betydde detta ett steg i x-
                 eller y-led, positivt eller negativt. Efter varje steg en sjöman tagis så kollar jag om
                 den nya positionen ärutanför gränserna. Om den är inne börjar en ny iterering för nästa
                 steg, men om den är utanför d.v.s att x eller y är större än storleken på 'the grid', så
                 avbryts iterationerna för stegen och börjar med nästa sjöman. Varje gång en sjöman faller
                 av 'the grid' lagrar datorn det i en variabel för att sen skriva ut totalen i slutet. 
                 Dessutom räknas antalet sjömän som faller av ut i procent av totalen. Det görs i en 
                 funktion som gör det genom att ta de sjömän som fallit delat på totalen och sedan 
                 produkten multiplicerat med 100 för stt få det i procent.
