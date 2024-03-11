### 1
Skriv ett program i Go som skapar en goroutine som skriver ut en text på skärmen

```go 
package main

import (
    "fmt"
    "sync"
    )

func main() {
    wg := sync.WaitGroup{}
    wg.Add(1)
    go func() {
        defer wg.Done()
        fmt.Println("Hello there")
    }()
    wg.Wait()

}
```

### 2
Skriv ett program i Go som läser ett värde från en kanal och skriver ut det på skärmen

```go
package main

import (
    "fmt"
    "sync"
)

func main() {
    strChan := make(chan string, 1)

    strChan <- "Hello there" // WRITES
    x := <- strChan // READS

    close(strChan)
    fmt.Println(x)
}


```
### 3
Var är GIL i Python och hur påverkar det trådade program i Python?

### 4
Skriv ett program i Go som kan ge upphov till ett data race

```go
package main

import (
    "sync"
    "fmt"
)

func main() {
    wg := sync.WaitGroup{}

    num := 0
    expected := 100

    for i := 0; i < expected; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            num++
        }()
    }

    wg.Wait()

    fmt.Println("Does 'num' equal 'expected'?", num == expected)
}
```

I detta program skapar vi 100 goroutines som inkrementerar 'num' med 1. Förväntningen är att 'num == expected' inte alltid kommer vara sann eftersom vi har flera goroutines som läser och skriver till 'num' samtidigt. Detta riskerar att exempelvis två goroutines läser värdet 5 för att sedan skriva 6 till minnesadressen medan det egentliga värdet bör vara 7. Detta är ett typexempel på ett race condition. 

### 5
Implementera Peterson’s algorithm i Go-liknande kod.

runtime gosched? 

### 6
Implementera en producent i Go-liknande kod som använder mutex för ömesidig uteslutning

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
    var lock sync.Mutex
    var wg sync.WaitGroup
    var lst []int

    for i := 0; i < 2; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            producer(0, 10, &lock, &lst)
        }()
    }
    wg.Wait()
    fmt.Println(lst)
}



func producer(start int, end int, lock *sync.Mutex, lst *[]int) {
    for i := start; i <= end; i++ {
        lock.Lock()
        *lst = append(*lst, i)
        lock.Unlock()
    }
}
```



### 7
Implementera en producent i Go-liknande kod som använder kanaler för ömesidig uteslutning
```go
package main

import (
    "sync"
    "fmt"
)

func main() {
    var lock sync.Mutex
    var lst []int
    gate := make(chan any, 1)

    for i := 0; i < 2; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            producer(0, 10, gate, &lst)
        }()
    }
    wg.Wait()
    fmt.Println(lst)
    close(gate)
}

func producer(start int, end int, gate chan any, lst *[]int) {
    for i := start; i <= end; i++ {
        gate <- nil
        *lst = append(*lst, i)
        <- gate
    }
}
```



### 8
Ge ett exempel i Go där två goroutines delar en variabel och använder en mutex för att (korrekt) skydda tillgången

```go
package main

import (
    "sync"
    "fmt"
)

func main() {
    var wg sync.WaitGroup
    var lock sync.Mutex

    x := 0

    for i := 0; i < 2; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            incrementor(&x, &lock)
        }()
    }
    wg.Wait()

    fmt.Println("Does x equal 100?", x == 100)
}

func incrementor(x *int, lock *sync.Mutex) {
    for {
        lock.Lock()
        if *x >= 100 {
            lock.Unlock()
            return
        } 
        *x++
        lock.Unlock()
    }
}
```
I detta program har vi två goroutines som kontinuerligt inkrementerar 'x' tills 'x == 100' är sant. Rutinerna använder mutex lås för att skydda oss från race conditions.

### 9
Ge ett exempel på ett program i Go med kanaler som kan leda till deadlock

```go
package main

import (
	"fmt"
	"math/rand"
	"sync"
)

func main() {
    var wg sync.WaitGroup
    c := make(chan int, 5)

    random := rand.Intn(11)

    for i := 0; i < random; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            writeToChan(c)
        }()
    }
    
    wg.Wait()
    fmt.Println("We made it")
    close(c)
    
}

func writeToChan(c chan<- int) {
    c <- 1
}
```

### 10
Ge ett exempel på ett program i Go utan kanaler som kan leda till deadlock

```go
package main

import (
    "sync"
)

func main() {
    var l1 sync.Mutex
    var l2 sync.Mutex
    var wg sync.WaitGroup

    wg.Add(1)
    go func() { // GO ROUTINE 1 (G1)
        defer wg.Done()
        l1.Lock()
        l2.Lock()

        l1.Unlock()
        l2.Unlock()
    }()

    wg.Add(1)
    go func() { // GO ROUTINE 2 (G2)
        defer wg.Done()
        l2.Lock()
        l1.Lock()

        l1.Unlock()
        l2.Unlock()
    }()
    wg.Wait()
}
```

I detta programmet har vi två gorutiner där G1 först låser l1, sedan l2. G2 låser först l2, sedan l1. I detta program finns en risk att G1 låser l1 och G2 låser l2 samtidigt. Det betyder att G1 kommer vänta på att l2 ska låsas upp, och G2 på l1, vilket betyder att båda kommer vänta i all evighet vilket skapar ett deadlock.

### 11
Implementera en parallel prefix sum med goroutines i Go

### 12
Implementera en parallel prefix scan med goroutines i Go

### 13
Implementera en parallel odd-even transposition sort med goroutines i Go

### 14
Visa hur en for-loop kan paralleliseras i Go med goroutines

```go
package main

import (
    "sync"
    "time"
    "fmt"
)

func main() {
    var wg sync.WaitGroup

    for i := 0; i < 10; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            printer(i)
        }(i)
    }
    wg.Wait()
}

func printer(i int) {
    time.Sleep(time.Second)
    fmt.Println(i)
}
```

### 15
Hur kan en barrier impementeras med mutex? Visa i Go-liknande kod

### 16
Hur kan en barrier impementeras med kanaler? Visa i Go-liknande kod

### 17
Ge en concurrent/parallel algoritm för att hitta det minsta värdet i en lista i Go-liknande kod

```go
package main

import (
	"fmt"
	"math"
	"sync"
)


func main() {
    var wg sync.WaitGroup
    reportChan := make(chan int)
    indexChan := make(chan [2]int, 10)
    doneChan := make(chan any)

    lst := []int{-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, -2, -10, 13, 14}

    intervall := 3
    valuesOnReportChan := len(lst) / intervall
    if len(lst) % intervall != 0 {
        valuesOnReportChan++
    }
    goroutines := 4

    wg.Add(1)
    go func() {
        defer wg.Done()
        sendIndexes(intervall, len(lst), indexChan)
    }()

    for i := 0; i < goroutines; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            worker(&lst, indexChan, reportChan, doneChan)
        }()
    }

    min := math.MaxInt
    for i := 0; i < valuesOnReportChan; i++ {
        x :=  <- reportChan
        if x < min {
            min = x
        }
    }
    close(doneChan)
    wg.Wait()
    fmt.Println("Smallest value: ", min)

}

func sendIndexes(intervall int, lstLen int, indexChan chan<- [2]int) {
    if intervall > lstLen {
        panic("intervalls may not exceed the lenght of the list")
    }
    start := 0
    end := intervall
    for end <= lstLen {
        l := [2]int{start, end}
        indexChan <- l
        start = end
        end += intervall
    }
    if end > lstLen {
        l := [2]int{start, lstLen}
        indexChan <- l
    }
}

func worker(lst *[]int, indexChan <-chan [2]int, reportChan chan<- int, doneChan chan any) {
    for {
        select {
        case _, ok := <- doneChan:
            if !ok {
                return
            }
        case l := <- indexChan:
            start, end := l[0], l[1]
            min := math.MaxInt
            for i := start; i < end; i++ {
                if (*lst)[i] < min {
                    min = (*lst)[i]
                }
            }
            reportChan <- min
        }
    }
    
}
```

### 18
Vad innebär en atomär variabel i Go
Det är en variabel som du kan utföra operationer på på en atomär nivå. Atomär nivå syftar på ett villkor för variabeln som garanterar att tiden det tar att göra en operation är så pass kort att inga race conditions sker om du skulle utföra flera operationer på variabeln från olika trådar samtidigt. 

### 19
Visa hur en variabels värde kan jämföras och bytas atomärt i Go

```go
package main

import (
	"fmt"
	"sync/atomic"
)

func main() {
	var x atomic.Int64
	x.Store(3)
    x.CompareAndSwap(3, 5) // LOOK HERE
    
    fmt.Println(x.Load() == 5)
}
```

### 20
Förklara vad happens before i en minnesmodell
Vad menar han?

### 21
Vilka antaganden kan göras om två trådar modiferar en delad variabel (enligt Javas minnes-modell).

### 22
Förklara begreppet multicore cpu

En 'multicore cpu' syftar på en flerkärnig processorenhet. Kärnorna på processorn är en slags processor i sig och möjliggör parallell exekvering. 

### 23
Vad är skillnanden mellan concurrency och parallelism?

Parallelism syftar på parallella exekveringar av olika processer och/eller trådar i ett program. Exempelvis kan två trådar exekveras och köras parallelt där tråd 1 beräknar 1 + 1 och tråd 2 1 + 2. Concurrency, eller samtidighet på svenska, syftar på själva strukturen och logiken i koden som möjliggör att parallella processer kan köras. Ett exempel på 'concurrent programming' är utformningen av den logik som gör att parallella processer kan läsa och skriva till samma minne på ett korrekt och säkert vis.

Inte helt hundra...

### 24
Vad betyder det att ett problem är embarrassingly parallel?

Det betyder att problemet är väldigt lätt att parallellisera. Detta kännetecknas genom att problemet kan delas upp i mindre delar som är oberoende från varandra vilket gör det lätt att integrera parallellism. Detta är ett slags idealtillstånd när man använders sig av parallelism. 

### 25
Ge exempel på ett problem som är embarrassingly parallel

Med hjälp av en monte carlo simulering kan man approximera pi genom att slumpmässigt ansätta punkter i en kvadrat med sidan 2 längdenehter som har en innersluten cirkel med radien 1 längdenhet. Kvoten mellan det totala antalet punkter och de punkter som hamnar i cirkeln kommer ge en approximation av pi. Detta problem kan lätt parallelliseras genom att låta ett set processer generera dessa slumpmässiga punkter.


### 26
Förklara begreppet operativsystem

Begreppet 'operativsystem' är ett mjukvaruprogram som finns i mer eller mindre alla dagens datorer. Programmets syfte är att ge ett användarvänligt gränssnitt med funktioner som gör datorn användarbar för en vanlig person. Programmet hanterar uppgifter som programexekvering, resursallokering, kommunikation med I/O, datahantering, etc.

### 27
Vad betyder det att ett operativsystem kan ses som ett interface mot datorn?

### 28
Vad betyder det att ett operativsystem kan ses som ett kontrollsystem för datorn?

Det betyder att operativsystemet kontrollerar vad som får hända på en dator. Operativsystemet ger en användare möjligheter att ändra många saker på en dator i form av exempelvis vad som sparas, samtidigt som den begränsar användaren i flera avseenden. Exempelvis kanske det inte är lämpligt för en "vanlig" användare att ha direkt tillgång till minnet där hen kan skriva till minnesadresser och ändra i minnesstrukturen då personen förmodligen inte vet vad den gör, vilket kan få oönskade konsekvenser. Därmed är det bättre att låta ett 'kontrollsystem' som ett operativsystem att göra det jobbet med mycket annat som gör att datorn funkar som den ska.

### 29
Vad är skillnaden på system mode och user mode?

### 30
Ange fem tillstånd en process kan befinna sig i och förklara vad de innebär

- new - Processen är i ett tillstånd av att ha precis skapats.
- ready - Processen är redo att köras
- run - Processen kör
- wait - Processen väntar in något för att få köra igen
- terminate - Processen avslutas

### 31
Förklara begreppen stack, heap, data och text i relation till processer

Stack - ?
Heap - Syftar på det dynamiska minne som används av processen
Data - Syftar på de initialiserade och ej initialiserade globala och statiska variabler
Text - Syftar på koden som ska köras av processen

### 32
Vad lagras i ett processkontrollblock (PCB)?

Det är en datastruktur som sparar information om en process. Exempel på sådan information är processens nummer, dess tillstånd, minnesbegränsningar mm.

### 33
Vad är en context switch?

En context switch är processen att pausa en process och spara dess tillstånd för att sedan ladda upp och och köra en annan process. Denna procedur sker kontinuerligt i ett operativsystem som möjliggör, endast till synes, en parallell exekvering av exempelvis två olika program.

### 34
Förklara vad som händer under en context switch

För ett set av processer/trådar som körs av en processor så förflyttar processorn sin uppmärksamhet mellan processerna/trådarna kontinuerligt och ofta för att ge intrycket att processerna/trådarna körs parallellt. Under en context switch så kör processorn en godtycklig process/tråd en viss tid. Efter det pausar den processen/tråden för att sedan spara dess nuvarande tillstånd till minnet. Den går sedan vidare till nästa process/tråd för att ladda upp dess tillstånd och köra den en viss tid och så vidare. 

### 35
Vad innebär schemaläggning av en process?

### 36
När tas beslut om schemaläggning?

### 37
Vad gör dispatcher?

### 38
Ange tre kriterier som kan användas för att bestämma vilken schemaläggningsalgoritm som skall användas

### 39
Vad betyder det att en process är I/O bound?

Det betyder att en process är begränsad av input/output som disk, användarinput från mus och tangentbord, nätverk etc

### 40
Vad betyder det att en process är CPU bound?

Det betyder att en process är begränsad av processorns interna resurser som antalet kärnor, processorns hastighet, cache etc.

### 41
Förklara hur schemaläggning sker om First Come, First Served används

### 42
Förklara hur schemaläggning sker om Round Robin används

### 43
Förklara preemptive schemaläggning

### 44
Förklara non-preemptive schemaläggning

### 45
Vad är ett quantum?

### 46
Hur påverkar ett quantum schemaläggningen?

### 47
Vad är viktigt att tänka på när man bestämmer quantum?

### 48
Förklara begreppen isolation och encapsulation i relation till processer

### 49
Vad är skillnaden på en process och en tråd?


En process är en sjävständig enhet som innehåller en egen uppsättning resurser som den kan arbeta med och används för att köra ett program eller applikation. Processer är isolerade till varandra och kan därmed inte kommunicera. Trådar är en del av en process och kan köras parallellt för att utföra uppgifter där trådarna kan kommunicera med varandra och nyttja resurserna som finns i processen. 

### 50
Vad används stacken till i en tråd?

### 51
Var är skillnaden på user-level- och kernel-level-trådar?

### 52
Förklara begreppet blockerande anrop

### 53
Vad händer om en user-level tråd gör ett blockerande anrop?

### 54
Vad händer om en kernel-level tråd gör ett blockerande anrop?

### 55
Varför vill man dela minne mellan trådar?

Ibland finns det ett intresse i att trådar kommunicerar med varandra. Det kräver någon form av gemensamt minne för trådarna att skriva och läsa från för att kommunikationen ska kunna ta plats.

### 56
Vad är skillnaden mellan att dela minne mellan trådar och processer?

Skillnaden är att trådar delar samma minne inom en process medan processer har separata minnesutrymmen som inte delas. Det innebär att trådar kan dela gemensam data direkt genom exempelvis variabler. Processer kommunicerar genom andra metoder som delade minnessegment eller genom Inter Process Communication IPC.

### 57
Förklara begreppet sequentially consistent i relation till minne

Det är en minnesmodell som beskriver hur minnet måste ordnas i ett parallellt system för att minnesoperationer ska ske i någon sekventiell ordning. När man programmerar seriellt sker alltid minnesoperationer i en sekventiell ordning eftersom du endast kan göra en minnesoperation i taget. Inom concurrent programming finns det möjlighet att utföra flera minnesoperationer samtidigt med trådar vilket kan orsaka race conditions. Därmed är det viktigt att de minnesoperationer som görs av parallellt exekverade trådar sker en i taget i någon ordning så att minnet beter sig som vi förväntar oss. 

### 58
Vad innebär ett data race/race condition?

Ett så kallat race condition är ett fenomen som förekommer inom exempelvis 'concurrent programming' där parallella processer riskerar att skapa inkonsekventa beteenden i ett program på grund av den timing som processerna sker. Exempelvis om två processer ska inkrementera värdet på en variabel x = 0 med 1 förväntar vi oss att x = 2 när processerna är färdiga. Dock om processerna sker samtidigt i den mån att båda hinner läsa värdet 0 för att sedan skriva värdet 1 till x kommer x ha det slutgiltiga värdet 1. Detta blir ett inkonsekvent beteende som inte är önskat.

### 59
Vad är en kritisk sektion?

En kritisk sektion är en sektion i koden där den delade datan för de parallella processerna/trådarna som körs behandlas och/eller hämtas. Dessa sektioner kräver ofta exklusivitet vilket betyder att sektionerna endast får köras av en tråd/process i taget. 

### 60
Ge exempel på ett data race

Säg att två parallellt exekverade processer vill inkrementera variabeln x = 0 med 1. Vår förväntning är att när processerna är klara kommer x ha tilldelats värdet 2. Det finns dock en risk att båda processerna hinner läsa värdet 0 från variabeln x vilket betyder att båda kommer skriva värdet 1 till x. Detta betyder att det slutgiltiga värdet för x är 1 vilket är inkosekvent med det förväntade resultatet. Detta problem är ett typexempel på ett data race.

### 61
Vad innebär ömsesidig uteslutning?

Det innebär att ett visst segment i koden endast får köras av en process i taget. Det vill säga: alla andra processer som körs parallellt är uteslutna från segmentet tills den process som är i segmentet är färdig. Exempelvis om flera processer ska skriva till variabeln x, förutsätter detta ömsesidig uteslutning eftersom race conditions annars kan skapas.

### 62
Hur kan ömesidig uteslutning lösas? ge exempel.

Man kan använda låsvariabler som kommunicerar ifall en process får gå in i kodsegmentet som kräver ömsesidig uteslutning. Detta förutsätter att själva låsningsprocessen är atomär. Om inte så kommer race conditions skapas där fler än en process riskerar att komma in i segmentet.

En annan metod är att använda sig av strikta växlingar (strict alternations) där man har en variabel 'turn' som kommunicerar ifall en process får köra ett kodsegment. Detta funkar dock bara för två processer. Processen som kör kodsegmentet som kräver ömsesidig uteslutning kan ändra variabeln 'turn' så att den andra processen får köra och vise versa.

### 63
Förklara hur strict alteration försöker lösa ömesidig uteslutning

Metoden 'strict alteration' använder sig av en variabel 'turn' som kommunicerar för två processer vem som  får köra ett kodsegment som kräver ömsesidig uteslutning. Säg att process A får köra när 'turn' är lika med 0 och process B när 'turn' är lika med 1. Om 'turn' till en början är 0, kommer process A få köra kodsegmentet. När process A är klar skriver den 1 till 'turn' och process B får köra osv.

### 64
Förklara Peterson’s algoritm för ömsesidig uteslutning

### 65
Vad innebär progression i relation till ömesidig uteslutning?



### 66
Vad innebär begränsad väntan i relation till ömesidig uteslutning?

### 67
Vad är en semafor?

En semafor är en variabel som agerar som ett lås för att styra hur många processer/trådar som får tillgång till exempelvis en kritisk sektion.

### 68
Vad är ett mutex lock?

Ett 'mutex lock' är en binär semafor som tillåter en låsning och en upplåsning i taget, därmed 'binär'. Den kan användas i sammanhang när ett moment i ett program kräver exklusivitet. Exempelvis att ändra värdet på en variabel kräver eklusivitet eftersom parallella processer riskerar annars att skriva över varandras ändringar.

### 69
Vad är skillnaden mellan en binär och en räknande semafor?

En binär semafor tillåter en låsning och en upplåsning i taget. En räknande semafor kan tillåta fler än en låsning och lika många upplåsningar. Exempelvis kan det finnas utrymme för flera processer att vara i en kritisk sektion, vilket betyder att en räknande semafor bör användas i stället för en binär.

### 70
Visa hur en räknande semafor kan implementeras med hjälp av binära semaforer

```go
package semaphore

import (
    "sync"
)

type SemaPhore struct {
    writeLock sync.Mutex
    waitLock sync.Mutex
    N int
    counter int
}

func (s *SemaPhore) Lock() {
    s.waitLock.Lock()
    for s.counter == s.N {
        // wait...
    }
    s.writeLock.Lock()
    s.counter++
    s.writeLock.Unlock()
    s.waitLock.Unlock()
}

func (s *SemaPhore) Unlock() {
    s.writeLock.Lock()
    if s.counter <= 0 {
        panic("unlock of unlocket lock")
    }
    s.counter--
    s.writeLock.Unlock()
}
```
### 71
Vilka risker finns det med låsning?

Det finns olika risker med att låsa. Här är några risker. 

- Programmet kan hamna i deadlock om ett set trådar lyckas få en låsningssekvens som gör att de måste vänta på varandra om varje tråd håller ett lås som någon annan behöver, samtidigt som varje tråd efterfrågar ett lås som någon annan tråd håller.
- Att låsa större datastrukturer för exklusiv tillgång för en tråd kan orsaka ett mer sekventiellt beteende hos ett program eftersom endast en tråd kan göra en operation på datastrukturen. Det besegrar själva syftet med att programmera parallellt. 
- Att göra låsningar kräver resurser som minne och uppmärksamhet av processorn vilket blir en overhead.

### 72
Vad är ett deadlock?

Ett deadlock är ett tillstånd som exempelvis en tråd kan vara i när tråden inte kommer vidare i sitt arbete eftersom den väntar på någon slags obligatorisk resurs som den aldrig tilldelas, alternativt kommer åt. Exempelvis ser vi i koden nedan hur en gorutin inte kommer vidare i sin anonyma funktion eftersom det finns inget i programmet som kommer släppa låsresursen 'lock' som gör att gorutinen kan låsa, göra sitt arbete, sedan låsa upp och avsluta.

```go
package main

import (
    "sync"
)

func main() {
    var lock sync.Mutex
    var wg sync.WaitGroup

    lock.Lock()

    wg.Add(1)
    go func() {
        defer wg.Done()
        lock.Lock()
        // DO WORK
        lock.Unlock()
    }()

    wg.Wait()
}
```

### 73
Vad innebär det att en process är deadlocked?
En process är 'deadlocked' när den inväntar en händelse som bara en annan process kan orsaka men som aldrig orsakas. Processen kommer aldrig vidare på grund av detta och ligger därmed bara och väntar.

### 74
Vilka fyra villkor krävs för deadlock?

- Mutual exclusion
- hold and wait
- No preemption
- Circular wait

### 75
Förklara hold and wait
Det är ett tillstånd när en process håller i minst en resurs samtidigt som de efterfrågar andra resurser. För att en deadlock ska skapas för denna process förutsätter det att andra processer som håller i någon av de efterfrågade resurserna aldrig släpper den.

### 76
Förklara no preemption
I ett sammanhang med deadlocks innebär det att man inte kan ta ifrån en resurs från en process innan processen är färdig.

Anteckningar:
Begreppet 'no preemption' innebär att man inte kan avbryta en exekverande process för att sedan låta den återuppta där den avbröts vid ett senare tillfälle.

### 77
Förklara circular wait

Det är när varje process i ett set av minst två processer inväntar någon händelse från någon/några annan/andra process/er som gör att de får gå vidare i sin exekvering men som aldrig händer. Det blir en cirkulär väntan eftersom varje process väntar på någon annan i ett visst led.

### 78
Förklara hur deadlock kan förhindras
En deadlock kan förhindras genom att förhindra ett av följande eller fler:
- Mutual exclusion
- hold and wait
- No preemption
- Circular wait

### 79
Hur kan mutual exclusion förhindras för att undvika deadlock?

'Mutual exclusion' håller om det finns minst en resurs som endast en process får hantera i taget. Så om alla resurser får hanteras av fler än en process så har vi förhindrat 'mutual exclusion'. I regel är det inte möjligt att förhindra 'mutual exclusion' dock.

### 80
Hur kan hold and wait förhindras för att undvika deadlock?

Genom att exempelvis sätta en timeout för när den måste sluta efterfråga en resurs och släppa de resurser som den håller i.  

### 81
Hur kan no preemption förhindras för att undvika deadlock?

Om en tråd håller i en resurs och efterfrågar en annan som den måste vänta på så kan man ta ifrån (preempt) resursen som den redan håller i för att låta någon annan process ta den. Alternativt, om en tråd efterfrågar en upptagen resurs kan den kolla ifall resursen kan bli ifråntagen av processen som håller den.

### 82
Hur kan circular wait förhindras för att undvika deadlock?

Cirkulär väntan kan förhindras genom att ansätta en ordning för hur resurser ska tas av processerna. Säg att  vi har resurserna A, B och C som används av ett set processer. Om resurserna erhålls av alla processer i samma ordning som de nämndes vid namn innebär detta att en slags kö kommer bildas som har sitt slut vid C. Det viktiga här är att vi bildar inga cykler i vår resource allocation graph.

### 83
Ge exempel på hur en semafor kan användas så att hold and wait inte gäller

### 84
Varför kan det vara problematiskt att förhindra no preemption

Det kan vara problematiskt eftersom när du tvingar bort en resurs från en tråd som arbetar med någon form av minneshantering så kan du behöva intetgöra det arbete som tråden redan har gjort på minnet. Detta intetgörandet vara svårt att genomföra.

### 85
Varför kan det vara problematiskt att förhindra hold and wait

### 86
Förklara starvation

'Starvation' är ett tillstånd som en process kan vara i där processen kontinuerligt aldrig blir tilldelad en resurs som gör att den inte kan komma vidare i sin exekvering.

### 87
Vad är en resource allocation graph och hur används den i samband med deadlock?

En 'resource allocation graph' är en graf bestående av två olika sorters noder: Trådar och resurser. I grafen använder man riktade bågar som innebär två olika saker i två olika sammanhang: 

- En utgående båge från en tråd till en resurs innebär att tråden efterfrågar resursen
- En utgående båge från en resurs till en tråd innebär att resursen tilldelas till tråden

Grafen kan användas för att hitta deadlocks. Exempelvis kan en cykel i grafen indikera på att det finns ett deadlock. Se exempel nedan:

!["Deadlock graph"](/img/deadlockgraph.png)

Notera att lås ett och två är binära semaforer.

Om den första tråden tilldelas det första låset samtidigt som den andra tråden tilldelas det andra låset kommer ett deadlock skapas eftersom tråd ett och två kommer i nästa tur efterfråga en resurs som hålls av den andra.

### 88
Hur kan man avgöra om ett system är i deadlock med hjälp av en resource allocation graph?

Man kan titta efter cykler i grafen. Om det finns cykler kan detta indikera att det finns deadlocks. Dock behöver det undersökas närmre.

Här är ett exempel:
!["Deadlock graph"](/img/deadlockgraph.png)


Notera att lås ett och två är binära semaforer.

Om den första tråden tilldelas det första låset samtidigt som den andra tråden tilldelas det andra låset kommer ett deadlock skapas eftersom tråd ett och två kommer i nästa tur efterfråga en resurs som hålls av den andra.

Om den första tråden tilldelas det första låset samtidigt som den andra tråden tilldelas det andra låset kommer ett deadlock skapas.

### 89
Är det ok att ignorera deadlock?

### 90
Vad är skillnaden på att förhindra och undvika deadlock?

### 91
Förklara Banker’s algoritm

### 92
Hur kan ett system återhämta sig från deadlock?

### 93
Förklara prefix sum

### 94
Förklara prefix scan

### 95
Förklara odd-even transposition sort

### 96
Varför är det en dålig idé att skapa nya trådar för varje rekursivt anrop i en divide and conquer-algoritm?

Det finns en risk att vi skapar väldigt många gorutiner som i sin tur skapar en overhead vilket tar på datorns resurser. I en 'divide and conquer-algoritm' som quicksort så blir det också allt mindre arbete för varje rekursivt anrop, vilket kanske inte är värt att skapa en helt ny gorutin för. Vi kan heller inte styra antalet trådar som skapas.

### 97
Varför kan det vara svårt att parallelisera rekursiva algoritmer?

Det kan vara svårt av olika anledningar. En anledning är att vi ofta måste ansätta en gorutin till varje rekursivt anrop vilket är problematiskt eftersom vi inte kommer ha kontroll på hur många gorutiner som skapas. Detta kan skapa en omfattande overhead och någonting som vi därmed vill undvika.

### 98
Vad är en barrier

En barriär är en samlingspunkt som ett set trådar måste nå innan någon av dessa trådar får köra vidare. 

### 99
Hur kan en semafor användas för att signalera mellan trådar?

### 100
Förklara hur depth-first search kan paralleliseras med trådar

### 101
Förklara hur breadth-first search kan paralleliseras med trådar

### 102
Förklara hur Prim’s algoritm kan paralleliseras med trådar

### 103
Vi kan hitta det minsta värdet i en lista på linjär tid (𝑂(𝑁 )). Hur lång tid tar det att köra med
𝑃 procecssorer? Motivera.

Vi kan dela upp listan i P segment där P processerorer kollar varsitt segment parallellt. Tidskomplexiteten blir här $O(\frac{N}{P})$.  Varje processor returnerar sedan det minsta värdet från sitt segment. Sedan måste en linjär sökning göras efter det minsta värdet på den lista av returnerade värden. Mängden av dessa värden är P eftersom vi har P processer som returnerar varsitt värde. Tidskomplexiteten blir till sist $O(\frac{N}{P} + P)$.

### 104
Vad krävs för att vi skall erhålla en speedup på 𝑃 med en algorim som körs på 𝑃 procecssorer

### 105
Är det alltid snabbare att parallelisera en algoritm och köra den på så många processorer som möjligt? Motivera.

Nej. Eftersom det kan vara kostsamt för datorn att skapa och köra många processer samtidigt så är det inte alltid snabbare att parallelisera på så många processer så möjligt. Ett exemepel på ett sammanhang där det är dåligt att parallelisera så mycket som möjligt är fråga 103. I 103 kom vi fram till att tidskomplexiteten för att hitta det minsta värdet med P processer var $O(\frac{N}{P} + P)$. Om vi ansätter så många processer som möjligt behöver vi ansätta $N=P$ vilket ger oss tidskomplexiteten $O(\frac{N}{P} + P) = O(\frac{N}{N} + N) = O(N + 1)=O(N)$. Här kommer vi tillbaka till tidskomplexiteten för det seriella fallet. 


### 106
Förklara N-ary-sökning.

### 107
Förklara hur N-ary-sökning kan paralleliseras med trådar

### 108
Förklara lock free

Lock free är en låsningsstrategi där man vill ta bort så mycket av låsningen som möjligt i programmet. I stället använder man verktyg som atomära variabler som garanterar att operationerna på dessa sker på en atomär nivå. Det betyder att vi inte kommer få några race conditions för dessa variabler. I kritiska sektioner låter man processer i stället försöka att gå in och utföra arbetet i den kritiska sektionen för att sedan göra om det om det skulle gå fel.

En lock free algoritm är fri från deadlocks och garanterar progression för programmet. Det finns dock en risk för starvation för vissa processer.

### 109
Förklara wait free

Wait free är i många avseenden lock free men bättre eftersom den garanterar progression per process i stället för progression för programmet. Det innebär att processerna aldrig upplever starvation.

### 110
Vad menas med en optimistisk algoritm (med avseende på ömesidig uteslutning)?

En optimistisk algoritm med avseende på ömsesidig uteslutning är algoritmer som är icke-blockerande, vilket innebär att flera trådar får arbeta på samma resurs samtidigt utan låsning eller med minimal låsning. För att förhindra händelser som att två trådar försöker göra ändringar i en minnesadress samtidigt, låter man varje tråd läsa minneadressens tillstånd innan den börjar konstruera den data som ska sparas där. Sedan Läser man in tillståndet igen och bekräftar att den överensstämmer med den förgående läsningen. Till sist skriver man in datan på minnesadressen. Den tråd som gör sin andra inläsning som kommer visa sig inte stämma överens med den första kommer få börja om och försöka igen.

### 111
Förklara compare and set

### 112
Visa hur compare and set kan användas för att implementera en binär semafor

### 113
Förklara hand over hand locking

Hand over hand locking är ett låsningsprotokoll som används för att parallella trådar ska kunna göra operationer på exempelvis datastrukturer utan att race conditions skapas. Hur hand over hand locking kan förklaras med hjälp av ett exempel. Säg att vi har en länkad datastruktur som man endast kan löpa igenom i en riktning. Vi har också en serie trådar som ämnar göra operationer som ADD, DELETE och UPDATE på listan. För att utföra dessa säkert behöver vi först låta alla element i listan ha en binär semafor. När en tråd sedan börjar löpa igenom listan börjar den först med att låsa det första elementet, sedan det andra. Sedan släpper den första för att sedan låsa det tredje. Tråden släpper sedan det andra för att sedan låsa det fjärde osv. Processen fortsätter tills den når det elementet den söker. Detta element skulle kunna vara det sista elementet då den kanske gör en ADD.

### 114
Vad är nackdelarna med att låsa “för mycket”?

Här är några nackdelar med att låsa "för mycket"

- Trådarna som körs och efterfrågar låsresurserna kan ligga och vänta vid flera tillfällen. När trådarna väntar gör de ingenting vilket blir ett slöseri med datorns resurser.
- Att göra flera låsningar minne och tid i form av operationer vilket gör programmet långsammare.
- Programmet kan bete sig mer synkront istället för asynkront vilket då besegrar syftet med att programmera asynkront. Ett exempel är om vi har en lista som bara en tråd kan sätta in värden i åt gången.

### 115
Vad är nackdelarna med att låsa “för lite”?

Den största nackdelen med att låsa för lite är förmodligen risken du skapar för data korruption på grund av race conditions.

### 116
Vad är fördelarna med en optimistisk algoritm (med avseende på låsning)?

En av fördelerna med en optimistisk algoritm är att du låser betydligt mindre, och i vissa algoritmer kanske du inte låser alls, vilket betyder att du sparar minne och tid (beror dock på).

### 117
Vad är nackdelarna med en optimistisk algoritm (med avseende på låsning)?

### 118
Förklara hur radering i en länkad lista kan implementeras med en optimistisk algoritm

### 119
Ange några problem med att skriva flertrådade program

Här är några problem som är relaterat till att skriva flertrådade program:

- Race conditions - Det förekommer i flera sammanhang när trådar ska dela ett och samma minne. Händelsen att två eller fler trådar försöker skriva till samma minnesadress samtidigt kan skapa data korruption eftersom datan på en minnesadress är många gånger beroende av en sekventiell hantering för att datan ska förbli konsekvent med våra förväntningar. 

- Deadlocks - Ett deadlock orsakas när varje tråd i ett set av trådar inväntar en händelse som endast kan orsakas av en annan tråd i setet för att kunna gå vidare sin exekvering. Programmet som helhet rör sig inte framåt på grund av detta vilket är ett problem.

- Exklusivitet - Ditt program kan ha kritiska regioner i sig som förutsätter att endast en tråd i taget kan vara där. Detta förusätter någon slags exklusiv tillgång till regionen. Ett problem är hur man ska skapa denna exklusivitet.

### 120
Varför kan det vara svårt att sätta samman (compose) flera flertrådade funktioner?

### 121
Vad är en Future?

### 122
Förklara begreppet goroutine

Enligt golangs hemsida är en goroutine en "lightweight thread" som kan exekveras parallellt med annan kod.

### 123
Förklara begreppet cooperative multitasking

### 124
Förklara begreppet asynchronous programming

'Asynchronous programming' är ett sätt att programmera som gestaltas av en icke-blockerande struktur. Det innebär att ett program får exekvera och köra flera kodsegment samtidigt till skillnad från ´synchronous programming´som hade kört dessa kodsegment sekventiellt.

### 125
Förklara begreppet callback

### 126
Vad händer om en blockerade funktion körs av en funktion på event loop

### 127
När bör man använda asynchronous programming?
Det bör användas i sammanhang där ett programmeringsproblem kan delas upp i olika delar där dessa delar har ett löst beroende eller ett oberoende till varandra . Summan av delarnas lösningar blir sedan lösningen till själva problemet. Exempelvis att hitta det minsta värdet i en lista kan lösas med hjälp av 'asynchronous programming´ genom att låta parallella processer/trådar kolla igenom ett set av indexintervall som tillsammans utgör listans indexintervall. För varje intervall letar en process/tråd efter det minsta värdet i det intervallet för att sedan rapportera det till någon gemensam resurs. Sedan kan en annan process/tråd läsa ifrån den resursen och reda ut vilket värde som är störst.

### 128
Vad är en kanal i Go?
En kanal i Go är mer eller mindre än trådsäker/processäker FIFO kö som parallellt körande processer/trådar kan skriva värden till och läsa värden i från.

### 129
Vad gör select i Go?
Select är en konsktruktion i go som används i samband med kanaler där den slumpmässigt väljer att läsa ett värde från någon av kanalerna som har värden på sig. De tomma ignoreras tills det finns värden på den. Detta är användbart om vi exempelvis vill att en gorutin ska kunna läsa från flera kanaler och göra arbete A från kanal A och arbete B från kanal B. Här är ett kort exempel.

```go
package main

import (
    "sync"
    "fmt"
    "time"
)

func main() {
    intChan := make(chan int)
    strChan := make(chan string)
    doneChan := make(chan any)

    var wg sync.WaitGroup

    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            worker(intChan, strChan, doneChan)
        }()
    }
    
    wg.Add(1)
    go func() {
        defer wg.Done()
        time.Sleep(time.Second * 3)
        close(doneChan)
    }()

    wg.Wait()
    fmt.Println("Program is done")
}

func worker(intChan <-chan int, strChan <-chan string, doneChan chan any) {
    for {
        select {
        case <- intChan: 
            // DO A
        case <- strChan: 
            // DO B
        case _, ok := <- doneChan: 
            if (!ok) {
                return
            }
        }
        
    }
}
```

### 130
Förklara begreppet done-kanal

En done-kanal är en kanal som används för att kommunicera till gorutiner att de kan stängas. Exempelvis om en serie gorutiner letar efter något och en gorutine hittar det man letar efter så kan denna rutin meddela någon instans som stänger done-kanalen och därmed alla gorutiner.

### 131
Visa (i Go-liknande kod) hur en goroutine kan avslutas med hjälp av en done-kanal

```go
package main

import (
    "sync"
    "time"
    "fmt"
    )

func main() {
    var wg sync.WaitGroup
    doneChan := make(chan any)
    
    wg.Add(1)
    go func() {
        defer wg.Done()
        worker(doneChan)
    }()

    wg.Add(1)
    go func() {
        defer wg.Done()
        time.Sleep(time.Seconds * 5)
        close(doneChan)
    }()

    wg.Wait()
}

func worker(doneChan <-chan any) {
    for {
        select {
        case _, ok := <- doneChan:
            if !ok {
                return
            }
        default:
        fmt.Println("Doing work...")
        time.Sleep(time.Second)
        }
    }
}
```
I det här programmet skapar vi en function kallad 'worker' som en gorutin kör. Funktionen skapar en while-loop där det utförs något arbete under raden default så länge 'doneChan' är öppen. När 'doneChan' stängs kommer '!ok' vara sann och 'return' kommer köras vilket avslutar funktionen och därmed gorutinen.


### 132
Implementera en funktion i Go som bestämmer det största värdet som skickas på en kanal

```go
package main

import (
	"fmt"
	"math"
	"math/rand"
)

func main() {
    intChan := make(chan int, 100)
    amount := 100
    go sendValues(amount, intChan)
    b := biggestValue(amount, intChan)
    fmt.Println("Biggest value:", b)
}

// HERE IS THE FUNCTION
func biggestValue(amount int, intChan <-chan int) int {
    biggestValue := math.MinInt
    for i := 0; i < amount; i++ {
        x := <- intChan
        if x > biggestValue {
            biggestValue = x
        }
    }
    return biggestValue
}

func sendValues(amount int, intChan chan<- int) {
    for i := 0; i < amount; i++ {
        intChan <- rand.Intn(1001)
    }
}
```

### 133
Implementera en funktion i Go som delar en kanal i flera kanaler (multiplex)

### 134
Vad är ett closure i Go?

En closure är en funktion som har tillgång till resurser som är definierade utanför dess omfång. Här är ett kort exempel:
```go
package main

import "fmt"

func main() {
    x := 2

    test := func() {
        x++
    }
    test()

    fmt.Println(x)
}
```

### 135
Förklara WaitGroup i Go

WaitGroup är en funktionalitet som används för att lägga till goroutines som ska väntas in tills de är klara med sin uppgift innan programmet går vidare till att komma vidare i programmet eller avsluta.

Här är ett exempel:
```go
package main

import (
    "time"
    "sync"
    "fmt"
    )

func main() {
    var wg sync.WaitGroup

    for i := 0; i < 10; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            time.Sleep(time.Second * 2)
        }()
    }

    wg.Wait()
    fmt.Println("Go routines are done")
}
```
Detta programmet skapar 10 goroutines som sover i 2 sekunder för att sedan meddela 'wg' att de är klara. Alla goroutines väntas in vid 'wg.Wait()' innan programmet kör den sista raden.

