## Uppgift: abcd

### Problem
Uppgiften går ut på att skapa alla möjliga kombinationer av bokstäverna a, b, c och d.

### Lösning
För att lösa detta problem använde jag en `for`-loop och `range`-funktionen för att iterera över alla tal från 1 till 4. Jag indenterade `for`-loopen för att få alla möjliga kombinationer av a, b, c och d. Eftersom jag hade svårt att bygga dessa kombinationer i en och samma funktion, skapade jag en separat funktion kallad `get_number` som tar emot 4 argument och bygger ett tal med dessa argument. Slutligen använde jag `if`-satsen för att jämföra talen och utföra önskad åtgärd.

## Uppgift: birthday_candles

### Problem
Uppgiften kräver att vi räknar ut hur många födelsedagsljus som behövs för ett antal år och sedan utför en jämförelse.

### Lösning
Denna uppgift var den svåraste i assignment två. Jag använde en `for`-loop för att iterera över åren och beräkna antalet ljus som behövs med hjälp av ett `while`-loop som ökar antalet ljus tills det är tillräckligt för året. Sedan minskade jag antalet ljus baserat på året och utförde en jämförelse med en `if`-sats.

## Uppgift: countdigits

### Problem
Uppgiften går ut på att skapa ett program som räknar antalet siffror i en given input och rapporterar resultatet.

### Lösning
För att lösa denna uppgift skapade jag tre variabler som initialt är satta till 0. Sedan använde jag `if`-satsar för att kontrollera inputen och ökade respektive variabel med 1 om villkoren var uppfyllda.

## Uppgift: drunken_sailor

### Problem
Uppgiften innebär att simulera rörelsen av berusade sjömän på en rutnät och räkna antalet sjömän som hamnar i vatten.

### Lösning
Jag började med att skapa variabler för rutnätet, steg och antalet sjömän som anges av användaren genom input. Jag skapade även variabler för att räkna antalet torra och våta sjömän. För att hålla koll på varje sjömans aktuella plats använde jag en dictionary med nycklarna 'X' och 'Y' som representerar x- och y-koordinaterna. Jag använde en `for`-loop för att iterera över varje sjöman, kontrollerade om de hamnade utanför rutnätet och ökade antingen det torra eller våta sjömännen beroende på deras plats.

## Uppgift: salary_revision

### Problem
Uppgiften går ut på att ta emot en lista med löner som input och beräkna medianen eller medelvärdet beroende på listans storlek.

### Lösning
Jag skapade två funktioner: `user_input` och `revision`. Första funktionen tar hand om användarinput och omvandlar det till en lista av löner med hjälp av `split()`-metoden. Därefter använde jag en `for`-loop för att konvertera talen från sträng till heltal (int) eller returnera ett felmeddelande om omvandlingen misslyckades. I `revision`-funktionen använde jag `len` och `sorted` inbyggda funktioner för att sortera listan och kontrollera dess storlek. Om listan hade ett udda antal element, använde jag det mittersta värdet som medianen, annars beräknade jag medelvärdet av de två mittersta värdena.

## Uppgift: pi_appfox

### Problem
Uppgiften går ut på att uppskatta värdet av pi (π).

### Lösning
Jag skapade en funktion `approx_pi(n)` som tar ett antal punkter `n` som input. Inuti funktionen genererar jag slumpmässiga punkter inom ett kvadratiskt område och räknar sedan hur många av dessa punkter som hamnar inom en cirkel som är inskriven i kvadraten. Genom att använda det förhållandet kan jag uppskatta pi (π). Jag beräknar sedan felmarginalen genom att jämföra resultatet med det verkliga värdet av pi.

Jag testar funktionen med olika antal slumpmässiga punkter och rapporterar resultatet, inklusive uppskattningen av pi och felmarginalen.