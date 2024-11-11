# Instuderingsfrågor svar

# Kvar
12, 13, 16

# 3
Global interpreter lock i python som stoppar trådar från att exekvera parallellt. Detta påverkar trådade program genom att förhindra dem från att utnyttja flerkärniga processorer när trådarna utflr cpu-bound arbete.

# 18
En atomär variabel nås genom sync.atomic och modifieras i sin helhet utan att andra trådar har möhlighet att se den i ett ofullständigt tillstånd vilket ger konsistens utan låsning.

# 20 
Happens befor i en minnesmodell innebär att något måste hända före den andra händer. det vill säga en relation emllan till exemple
tvår processer därd en ena måste ske för den andra då det klanske behlövs en variable eller liknande.

# 21
Enligt javas minnesmodell kan man ej garantera utkommet nät rvå trådar modifirear en delad variabel. Skulle det inte finnas lås eller andra mekanismer vet man inte hur de kommer agera och kan leda till race conditions och ordningen har ingen garanti

# 22
En multicore cpu innebär en flerkärning processor. En sådan rocessor har flera oberoende kärnor där exekveringart ich läsningar kan utföras parallellt. Det innebär då att man kan öa processorns maxkapacitet.

# 23
Skillnaden är att concurrency handlar om struktur med paralleism handlar om utförande. Att parallellt utför två saker innebör att dessa körs samtisigt menas att göra en concurrent algorith är designmlnstret som skpas föä r att hantera föera ippgifter samtisdgt.

# 24
Att ett program är embarrasingly parllell innebär att det kan köras parallellt i flera trådar utan möjlighert att påverjka varandra. Man kan alltså utföra flera saker på en delad lista till exemple utan att andra trådar påverkas av varandra. 

# 25
Om du till exempel har en lista med tusentals bilder och du ska hitta just en specifik bild kan du låda flera trådar leta samtisigt i olika delar av listan. Detta gör att du kan förkorta tiden det tar att hitta en specifik bild markant. När trådarna inte heller påverkas av varnadra är riskn för deadlocks race conditions ocvh liknande miniaml.

# 26
Ett operativsystem fungerar sopm en mellanhand mellan användaren och hådvaran den ger ett läsbart användargränssnitt. Operativsystemet sköter och styr tuillgpngen tillnhåtdvaran. Den tilldelar processer oh program och gör dartorn effektivare i den mån möjligt. Det gör det öjligt för anändaren att styra dess tillgångar via ett användargränssnitt och gömer den största komplexitetent i hårdvaran. 

# 29
I system mode har man tillgång til hela datorns hårdvara och funktioner medan i user mode har ma begränsad tillgång. Detta ger ett sjkydd till datorn så att användaren inte kan uitföra alltför skadliga saker på datorn uatn istället skyddas. När den befinner sig i system mode så kan denutföra allt men då finns det risk att skada systemet om man inte vet vad man gör.

# 30
NY - processen har precis skapats och fått sin information
REDO  - processen väntar på att bli tilldelad resurser för att kunna köras
KÖR - Processen jkörs och den utför sin uppgift
VÄNTANDE - processen väntar på information som behövs för att ikunna köra vidare
AVLUTAD - processen har körts och utöfrt suitt uppdrag

# 31
STACK - I stacken lagras de lokala variavbelr och information om trådar och funktionmer, dynamisk och sköts avv processen
HEAP - Sköts av utvexcklaren och är en dynamsik mineesallokering under programkörning
DATA - Globala varieabler 
TEXT - Maskinkoden och progeraminstruktioner

# 32
I PCB lagras information om en process, däribland, stack, heap, minne, status, räknaren säkerhet, prioritetit tillsåtnd, o.s.v.

# 33
Context swithch är när operativsystemet lagrar information om en priocess tillstånmd för at senare kunna exekvera vidare den och till exemple köra en process med högre prioritet istället. Den lagrar informationen om processens tillstånd i pcbn och skiftaer resurserna till en annan procerss och nåär den senare ska årerupptas laddas informationen fårn pcbn och processen slutflörs

# 38
respnsivitet, maximering, rättvisa

# 48
isolation innebär att en process körs i sitt egan minnesutrymme medans encapsultation innebär att procesen endast kommer åt sina egna resurser och drtata


