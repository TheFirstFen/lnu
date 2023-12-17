# Lab 2

Här kommer rapporten som tillhör lab 1 för 1DT907 kursen från [Samuel Berg](<sb224sc@student.lnu.se>)

## Hur man kör Main*.java programmen

Först och främst så tar vi och kör det följande kommandot i terminalen/consolen. Detta gör vi för att compile:a vår .java filer till filer så går att köra.

***Notera:*** Eftersom jag kör på linux så är jag ej helt säker om det är samma kommandon på windows, hoppas det ändå ska funka då jag skickar med .class filerna också. Om jag känner till wondows korrekt lägg till `.java` när du ska köra filerna i wondows med `java MainX.java` exempelvis.

```bash
javac *.java
```

För att köra något av *Main* programmen, skriv en av de följande kommandona in i din terminal/console. I ordning från topppen ner.

1. kör main programmet för `Problem 1` algorithmen

2. kör main programmet för `Problem 2` algorithmen

3. kör main programmet för `Problem 3` algorithmen

4. kör main programmet för `Problem 4` algorithmen

5. går att köra `Problem 5` men ej bra implementerad eller totalt funktionell.

6. kör main programmet för `Problem 6` algorithmen

```bash
java Main1
java Main2
java Main3
java Main4
java Main5
java Main6
```

## Problem 1

Jag löste resizningen för queue:n genom att vid varje enqueue kolla om `size == queue.length` om den var det så ökade jag köns storlek med en faktor av `2`. På liknande sätt vid en dequeue så kollar jag om `size == queue.lenght / 4` om snat så reducerade jag köns storlek med en faktor `2`. för redovisning så här ser min enqueue funktion ut:

```java
public void enqueue(Obj obj) {
        if (obj == null) {
            throw new IllegalArgumentException("Cannot be null");
        }

        if (size == queue.length) {
            resize(2 * queue.length);
        }

        queue[size++] = obj;
    }
```

Skillnaden med enqueue implementationen och dequeue implementationen är att in enqueue kollas det om den behöver resize:as innan insättning medans i dequeue kollas det efter borttagning.

## Problem 2

För detta experiment så byggde jag up ett AVL och ett BST träd med 10 000 000 noder i början för att han en förhoppningsvis tydligare tidsskillnad i resultaten. När det vart gjort så körde jag på dessa träd ett "general case test" vilket tar tiden då en mängnd olika tal skall i ordning sättas in, sökas upp och tas väck ur trädet och ta tiden för varje operation för hela mängnden tal. Efter detta är gjort så skrivs det ut i terminalen för BST respektive AVL tärdet deras tider för att gör de olika operationerna för den ängden tal vi hade samt att vi skriver ut höjden på trädet från root:en till yttersta noden. Ett exemple resultat som blev är det följande:

```text
BST:
insert: 4.0109 s
search: 2.7219 s
delete: 3.4082 s
height: 60

AVL:
insert: 4.7135 s
search: 2.6945 s
delete: 4.0048 s
height: 28

Diff (AVL - BST):
insert: 702.6044 ms
search: -27.3676 ms
delete: 596.5343 ms
height: -32
```

Där vi också tar och reprensentera skillnaden i tid för operationerna för de olika träden. som vi kan se så har AVL trädet som förväntat en längre insättnings och uttagnings tid jämfört med BST trädet men en effektivare sök operation då AVL trädet balanserar sig under upp byggnaden jämfört med BST trädet vilket kan ses på `height` noteringen i Diff delen där vi kan se att höjden från root:en till yttersta node för AVL trädet är 32 noder närmare än för BST trädet vilket leder till den ökade prestandan i sökning. Detta vart dock endast generela fallet om vi tar och tittar på bästa samt värsta fallet så kommer utskriften i terminalen möjligen se ut som följande:

```text
Best case:
Time to insert, search & delete 16383 objects
BST test: completed
AVL test: completed

BST:
insert: 1.0566 ms
search: 3.1272 ms
delete: 2.0912 ms
height: 14

AVL:
insert: 2.0998 ms
search: 3.4103 ms
delete: 3.3879 ms
height: 14

Diff (AVL - BST):
insert: 1.0433 ms
search: 283.0750µs
delete: 1.2966 ms
height: 0
```

Medans värsta fallet:

```text
Worst case:
Time to insert, search & delete 16383 objects
BST test: completed
AVL test: completed

BST:
insert: 2.2255 s
search: 1.7053 s
delete: 272.3140µs
height: 16383

AVL:
insert: 3.2341 ms
search: 2.0042 ms
delete: 2.2163 ms
height: 14

Diff (AVL - BST):
insert: -2.2223 s
search: -1.7033 s
delete: 1.9439 ms
height: -16369
```

Från detta kan vi se att om det som ska sättas in i träden är i korrekt ordning för att bygga upp trädet perfekt så är BST trädet ganska överlägset jämfört med AVL trädet, men om vi tar en titt på värsta fallet så ser vi att AVL trädet totalt sätt för mängden tal är effektivare på insättning samt upp sökning men förlorar när det kommer till borttagning då AVL trädet bygger om sig själv då det blir för obalanserat. Väldigt tydligt också med höjd skillnaden på träden är att AVL trädet är att föredra i detta fall.

I min åsikt så hade jag sagt att det är mycket mer lämpligt med ett balanserat träd då man hanterar stora data mängder på grund av att om det växer i snitt eller värsta fallet kommer BST trädet att bli så obalancerat att det kan ta uppåt flera minuter om inte mer att nå något som ligger ytterst i trädet jämfört med AVL trädet som kommer att ha byggt om sig själv till att ge oss snabbaste möjliga anslutning till värdet oavsett insättnings ordning.

## Problem 3

Min implementation har de krävda funktionerna så här ser `insertPerson()` ut:

```java
public void insertPerson(String name, int prio) {
    if (size == arr.length) {
        resize();
    }

    arr[size] = new Person(name, prio);
    size++;
    Quicksort.quickSort(arr, 0, size - 1);

    // * Att använda detta vart enda sättet jag hittade för att kunna
    // * hantera mer än 10 000 presoner i kön. (kolla följande kommentar)

    // Arrays.sort(arr, 0, size, Comparator.comparingInt(p -> p.prio));
}
```

Enligt mina tester så ser jag att jag har 3 av de 4 funktioner na som är beroende på antalet personer i kön den enda som är icke beroende av detta är `getPerson()` detta är på grund av att för att få detta tar jag bara personen på index `0` i array:et. De andra tre som är beroende på antalet personer enligt mina experiment är beroende på sorterings algoritmen man använder till att sortera efter prioritet vilket jag skapade en quicksort variant för `Person` object:et vilket ger mig StackOverflowException om jag har fler än `10 000` personer i kön. Snitt tider jag får ifrån min testning är följande:

```text
Testing getPerson(): 9.2070µs (Person{name='test61', prio=0})
Testing insertPerson(): 10.7418 ms (Person{name='Alice', prio=0})
Testing swapPriority(): 800.8949 ms (swaped Person{name='Alice', prio=0} & Person{name='Adam', prio=7})
Testing deleteMinPriority(): 727.5847 ms (Person{name='test61', prio=0})
```

Dessa tider känns något rimliga då man tänker på hur allt vart implementerat samt att jag använder en egen quicksort variant för att sortera personerna i kön. De 3 so beror på storleken av kön enligt mina beräkningar har en tids komplexitet lik sorteringsalgorithmen vilket ger dem en ungifärlig tidskomplexitet på `O(n log(n))`.

## Problem 4

Jag gjorde 100 stycken experiment och fick fram i slutet det följande:

```text
Heapsort is the most efficient algoritm with time: 2.3710 ms and for recursion depth: 5
Heapsort is the most efficient algoritm with time: 491.3070µs and for recursion depth: 10
Heapsort is the most efficient algoritm with time: 453.8310µs and for recursion depth: 15
Heapsort is the most efficient algoritm with time: 459.5050µs and for recursion depth: 20
Heapsort is the most efficient algoritm with time: 455.2870µs and for recursion depth: 25
Heapsort is the most efficient algoritm with time: 444.4350µs and for recursion depth: 30
Heapsort is the most efficient algoritm with time: 431.9000µs and for recursion depth: 35
Heapsort is the most efficient algoritm with time: 467.8730µs and for recursion depth: 40
Heapsort is the most efficient algoritm with time: 450.2750µs and for recursion depth: 45
Heapsort is the most efficient algoritm with time: 496.2370µs and for recursion depth: 50
Heapsort is the most efficient algoritm with time: 472.3280µs and for recursion depth: 55
Heapsort is the most efficient algoritm with time: 463.9240µs and for recursion depth: 60
Insertionsort is the most efficient algorithm with time: 137.6630µs and for recursion depth: 65
Insertionsort is the most efficient algorithm with time: 356.7390µs and for recursion depth: 70
Insertionsort is the most efficient algorithm with time: 246.5370µs and for recursion depth: 75
Insertionsort is the most efficient algorithm with time: 369.9100µs and for recursion depth: 80
Insertionsort is the most efficient algorithm with time: 120.3720µs and for recursion depth: 85
Insertionsort is the most efficient algorithm with time: 362.5530µs and for recursion depth: 90
Insertionsort is the most efficient algorithm with time: 116.0810µs and for recursion depth: 95
Insertionsort is the most efficient algorithm with time: 353.1370µs and for recursion depth: 100
```

Detta gäller då vi kollar på en array med 1 000 element och går i steg av `5` med depth med quicksort innan jag skapar kopior av array:et för att sortera det sorterade array:et med heap- respektive insertionsort.

## Problem 6

Från min tester med mina olika shellsort sekvenser så får jag att tidskomplexiteten stämmer någlunda väl överäns med vad som representerads i wikipedia artiklen som medgavs med uppgiften. Jag får resulta liknande följande:

```text
Testing for array size of 100000
ShellSort w seq: hibbard, time: 47.2076 ms
ShellSort w seq: sedgewick, time: 30.7012 ms
ShellSort w seq: knuth, time: 36.5370 ms

Testing for array size of 200000
ShellSort w seq: hibbard, time: 75.7807 ms
ShellSort w seq: sedgewick, time: 68.1272 ms
ShellSort w seq: knuth, time: 76.2070 ms

Testing for array size of 300000
ShellSort w seq: hibbard, time: 99.6089 ms
ShellSort w seq: sedgewick, time: 105.0120 ms
ShellSort w seq: knuth, time: 120.5488 ms

Testing for array size of 400000
ShellSort w seq: hibbard, time: 137.0622 ms
ShellSort w seq: sedgewick, time: 144.4007 ms
ShellSort w seq: knuth, time: 156.3455 ms

Testing for array size of 500000
ShellSort w seq: hibbard, time: 168.0282 ms
ShellSort w seq: sedgewick, time: 180.3242 ms
ShellSort w seq: knuth, time: 217.6204 ms

Testing for array size of 600000
ShellSort w seq: hibbard, time: 263.0259 ms
ShellSort w seq: sedgewick, time: 238.5287 ms
ShellSort w seq: knuth, time: 230.5272 ms

Testing for array size of 700000
ShellSort w seq: hibbard, time: 241.2289 ms
ShellSort w seq: sedgewick, time: 267.4571 ms
ShellSort w seq: knuth, time: 298.7250 ms

Testing for array size of 800000
ShellSort w seq: hibbard, time: 333.1191 ms
ShellSort w seq: sedgewick, time: 314.2258 ms
ShellSort w seq: knuth, time: 351.3146 ms

Testing for array size of 900000
ShellSort w seq: hibbard, time: 392.4427 ms
ShellSort w seq: sedgewick, time: 405.3004 ms
ShellSort w seq: knuth, time: 462.7835 ms

Testing for array size of 1000000
ShellSort w seq: hibbard, time: 471.7961 ms
ShellSort w seq: sedgewick, time: 503.8592 ms
ShellSort w seq: knuth, time: 574.7555 ms
```

Dessa resultaten tycker jag verkar rimliga vid denna storlek på input array och verkar också skala på ett sätt enligt den adviserade tidskomplexiteten.
