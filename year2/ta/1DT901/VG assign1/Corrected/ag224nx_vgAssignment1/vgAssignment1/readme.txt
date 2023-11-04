Assignment 1 (VG-uppgifter)

Uppgift #7 sumofthree.py
Borjade med att anvandaren fick mata in ett tresiffrigt heltal genom int(input(...)).
For att lyckas plocka ut var siffra för sig till varsin variabel gjordes foljande:

Plocka ut första siffran ur det tresiffriga talet: a1= numbers/100      # hur manga ganger talet går att delas med hundra
                                                                    OBS: kunde anvant numbers // 100 istallet men i.o.m.
                                                                    att talet skulle vara tresiffrigt spelar det ingen
                                                                    storre roll
Med hjalp av % och // kunde resterande tva siffror plockas ut. De utplockade siffrorna summeras på slutet m.h.a. addition 
och printas ut.

Uppgift #8 change.py
For att anvandaren sjalv skulle kunna mata in bade en faktura och hur mycket pengar som ska anvands for att betala hyran
anvandes int(input()). Nedanfor gors en utrakning som raknar ut hur mycket eller hur lite anvandaren för tillbaka i vaxel
m.h.a. formeln:  c = pay - pr. Enligt instruktionerna till uppgiften skulle vaxeln sedan delas upp efter 1000-sedlar,
500-sedlar osv. For att dela upp vaxeln i olika sedlar anvande jag %  och //. Vaxeln i sedlar och mynt avrundades
med round(). M.ha. print() skrevs vaxeln ut på slutet.

Uppgift #14 tax.py
M.h.a. int(input()) kunde anvandarens inkomst matas in i siffror. Efter det raknades skatten for hur stor inkomst anvandaren 
har i extra1, extra2 och extra3 ut for respektive skatte-grupp. Skatten avrundades for sig med round(). For att avgora
i vilket intervall anvandarens inkomst hamnade i anvandes if - else for varje intervall. Print funktionen anvandes inne i
if - else for att printa ut hur mycket anvandaren behover skatta for sin inkomst. Denna print funktionen anvandes 
for varje inkomst-intervall (inkomst-intervall: under 38000, mellan 38000 till 50000, över 50000)



