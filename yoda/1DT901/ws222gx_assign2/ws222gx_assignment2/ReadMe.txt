Assignment 2:

Uppgifter:
    countdigits.py
    birthday_candles.py
    abcd.py
    pi_approx.py
    salary_revision.py
    drunken_sailor.py

Min tanke med countdigits var att gå igenom varje tal för sig och kolla om det är 0, udda eller jämnt tal

birthday_candles tänkte jag så här med, jag vet max åldern, så en for loop behövs, jag vet hur många ljus det är per låda samt att år = ljus
därmed tänkte jag att så länge åldern är större än antalet ljus som existerar så lägs det till en låda samt 24 ljus
och för varje år som går så tas antalet ljus bort genom att subtrahera åldern från ljus antalet
och om det behövs en låda till då printas det annars printas det inget då det är onödig information

abcd uppgiften var min tanke att använda fyrdubblad loop som det stod i uppgiften samt att återanvända mig av get_number variablen för att även få ut dcba och inte bara abcd talet
för att sedan multiplcera abcd med 4 och sen kolla om abcd == dcba och om de är de printa talen på abcd och annars fortsätter den och kollar alla tal

När jag skulle börja koda pi_approx så var min tanke att först få fram uträkningen för distansen mellan punkterna, som jag sedan skulle kunna använda för att avgöra om punkten var i cirkeln
efter detta skapade jag en loop som höjer N med r alltså N upphöjt i r, vilket blir tydligare en att hård koda in de 3 N värdena.  

På salary_revision så var min tanke att dela upp uträkningarna i 3 funktioner, en för medianen, en för medelvärdet 
och till sist skillnaden. Sen gick mitt fokus över till hur jag skulle få inputen från en string till en integer lista, 
därmed splita jag strängen och sedan konverterade varje tal till en integer list

Mitt tanke sätt på drunken_sailor var att dela upp problemet i 3 delar, där den främsta delen var att simulera varje "sailor's" rörelse
nästa del var att kolla om "sailorn" var i området som var angivet av boundary variablen och därmed kunna avgöra om "sailorn" är i eller utanför området
den sista delen var att gå igenom antalet "sailor's" och sätta ihop funktionerna för att sedan få ut ett resultat om hur många som ramlade av