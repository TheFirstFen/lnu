# Answer to PDF

## part 1

* Liga
* Tabel
* Lab
* Domare
* Tävling
* Resultat
* Gymnaster
* Organisatörer
* Ledare
* Administratörer

### De olika delarna

* Lag som innehåller Ledare och Gymnaster
* Liga som innehåller Organisatörer, Administratörer, Domare, Tabel och Tävlingsresultat
* Tävlingar som innehåller Datum, Tid, Deltagare, poäng per gren och plats

## part 2

I komponenten lag finnns Ledare och Gymnaster och den har som uppgift att hålla koll på de olika medlemarna i ett lag samt vad de har för roll i laget. Det ska även gå att ändra informationen i laget om en individ har rätt behörighet. Som en ledare ska kunna läga till och ta bort gymnaster från laget samt ändra information om gymnasterna och sig själv. Medan Gymnasterna ska kunna ändra sin egna information.

I komponenten Liga kan administratörer lägga till/ ta bort / ändra information Organisatörer, Domare och lag som deltar. Organisatörerna Skapar senad tabelen som innehåller de olika lagen. Från tävlingarna tillkommer sedan ett resultat som sedan uppdaterar ligan och de olika lagens poäng.

I komponenten Tävlingar ska Datum, tid och plats kunna ses av alla lag i ligan och organisatörerna ska kunna ändra informationen om en tävling flyttas. Resultatet av vilket lag som vann och hur många poäng alla lag samt gymnaster fick ska synas och kunna ändras/ läggas till av organisatörerna efter en tävling eller under en tävling. Domarna ska kunna läga in poäng men de ska kontrolleras av organisatören eller administratörer innan det går igenom. Tävlingar måste ha tillgång till Lag komponenten och Liga komponenten för att veta vilka som deltar och vilka som ska delta samt ha tillgång till Domare samt kunna rapportera resultat.
