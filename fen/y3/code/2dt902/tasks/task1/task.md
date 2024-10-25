# 2DT902

## Övning 1 - Systematisk Nedbrytning

### **Komponenter/Components**

    - Registrering
    - Rekrytering
    - Lag
    - Domare
    - Aktiviterter/grenar
    - Liga
    - Event
    - Tränare/Ledare
    - Orginisationer
    - Tävlande
    - Administratörer
    - Tabell
    - Resultat
    - Datum/Tid
    - Plats
    - Portal/Informations uppvisning
    - Deltagare

### 1. **Identifiera viktiga abstraktioner (delsystem eller komponenter)**

1. **Core-managmentsystem**

    1. **Användarhanteringssystem/User-managementsystem**
        - Hanterar alla användare (administratörer, domare, tävlande, ledare, lagmedlemmar).
        - Användarregistrering och inloggning, hantering av roller och rättigheter.

    2. **Tävlingshanteringssystem/Event-managementsystem**
        - Skapar och hanterar säsonger, tävlingar, möten och specifika grenar.
        - Schemaläggning av tävlingar, lags deltagande och registrering av gymnaster till tävlingar.

    3. **Domarhanteringssystem/Referee-managementsystem**
        - Tilldelar kvalificerade domare till olika grenar.
        - Poängsättning och hantering av domarnas bedömningar.
        - Hantering av regler och poängräkningslogik (ta bort högsta och lägsta poäng, räkna medelpoäng, etc.).

    4. **Resultathanteringssystem/Result-managementsystem**
        - Samlar poäng för alla gymnaster och lag.
        - Beräknar slutresultat för varje tävling och sammanställer slutresultaten för möten och säsonger.
        - Hanterar publicering av resultat till användare.

2. **Portal och presentationssystem/Portal and presentation-system**
   - Huvudsaklig ingång för alla användare (administratörer, domare, lagmedlemmar, publik).
   - Presenterar tävlingar, gymnaster, resultat och annan relevant information.
   - Möjliggör enkel navigering och interaktion för slutanvändare.

   1. **Rapporterings- och analysverktyg/Repporting- and analysistool**
        - Genererar rapporter för administratörer om prestationer, resultat och deltagande.
        - Tillhandahåller statistik över säsonger och tävlingar.

### 2. **Beskrivning av varje komponent och ansvar**

1. **Användarhanteringssystem**
   - **Ansvar**: Hantering av användarroller (administratörer, domare, gymnaster, lagledare) samt autentisering och rättighetshantering.
   - **Tjänster**:
     - Användarregistrering och -inloggning.
     - Rollhantering (ex. administratör, domare, gymnast).
     - Auktorisering och rättighetskontroll.

2. **Tävlingshanteringssystem**
   - **Ansvar**: Planera och hantera säsonger, möten, tävlingar och grenar.
   - **Tjänster**:
     - Skapa säsonger och möten.
     - Schemaläggning av tävlingar och registrering av lag/gymnaster.
     - Hantering av tävlingsformat (individuella och lagbaserade tävlingar).

3. **Domarhanteringssystem**
   - **Ansvar**: Hantering av domare och deras poängsättning.
   - **Tjänster**:
     - Tilldelning av domare till tävlingar.
     - Poängsättning för varje gren och gymnast.
     - Hantering av bedömningsregler och poängberäkning.

4. **Resultathanteringssystem**
   - **Ansvar**: Beräkning och sammanställning av resultat.
   - **Tjänster**:
     - Beräkning av individuella poäng och lagpoäng.
     - Hantering av tävlingsresultat och säsongsresultat.
     - Resultatpublicering och åtkomst.

5. **Portal och presentationssystem**
   - **Ansvar**: Huvudingång för alla användare och presentation av information.
   - **Tjänster**:
     - Visa tävlingar, resultat och laginformation.
     - Tillgänglighet till nyheter och uppdateringar.
     - Portal för lagledare att hantera laginformation och gymnaster.

6. **Rapporterings- och analysverktyg**
   - **Ansvar**: Generera rapporter och statistik.
   - **Tjänster**:
     - Rapporter över prestationer och resultat.
     - Statistik för säsonger, möten och tävlingar.
     - Analys av deltagande och prestationer över tid.

### 3. **Identifiera beroenden mellan komponenterna**

- **Användarhanteringssystem** är en grundläggande komponent som alla andra delsystem är beroende av för att hantera rättigheter och autentisering av användare.
- **Tävlingshanteringssystem** är beroende av **Användarhanteringssystemet** för att registrera gymnaster och lag, och beroende av **Domarhanteringssystemet** för att tilldela domare till tävlingar.
- **Domarhanteringssystemet** är beroende av **Tävlingshanteringssystemet** för att veta när och var domare behövs.
- **Resultathanteringssystemet** tar in data från **Domarhanteringssystemet** och **Tävlingshanteringssystemet** för att beräkna resultat och poäng.
- **Portal och presentationssystemet** är beroende av alla andra delsystem för att visa rätt information för slutanvändare.
- **Rapporterings- och analysverktygen** tar data från **Resultathanteringssystemet** och **Tävlingshanteringssystemet** för att skapa rapporter och analyser.

### 4. **Nedbrytning av en komponent – Tävlingshanteringssystem**

#### Ansvar:
- Planera säsonger, tävlingar och möten.
- Schemaläggning och lagregistrering.
- Hantering av olika tävlingsformat och grenar.

#### Intern struktur:
1. **Säsongshantering**
   - Ansvarar för att skapa och hantera hela tävlingssäsongen.
   - Innehåller information om möten och tävlingar.

2. **Mötesschemaläggning**
   - Sköter schemaläggning av tävlingsdagar och specifika grenar.
   - Hanterar tidplaner för tävlingar och resursallokering (platser, domare, etc.).

3. **Grenhantering**
   - Skapar och hanterar olika grenar för varje tävling.
   - Ser till att rätt format och regler följs (t.ex. damtävlingar med balansbom, fristående etc.).

4. **Lag- och gymnastregistrering**
   - Hanterar registrering av lag och gymnaster för tävlingar och specifika grenar.
   - Inkluderar stöd för att ange vilka grenar en gymnast ska tävla i.

5. **Kommunikation med domare och resultat**
   - Integreras med **Domarhanteringssystemet** för att tilldela domare till olika grenar.
   - Skickar information om resultat till **Resultathanteringssystemet**.


## Instuderingsfrågor

Diskutera gärna i grupp med försök att hitta svaren själv i boken eller i bilderna från föreläsningarna.

    1. Vilka är utmaningarna som arkitekturarbetet tar sig an?

    2. Varför är arkitekturdesign viktigt?

    3. Vilka är skillnaderna mellan design på en hög och en låg nivå?

    4. Ge exempel på vad som bidrar till att göra mjukvarusystemen och utvecklingen av dem komplexa.

    5. Hur kan vi hantera, reducera eller till och med ta bort komplexiteten i utvecklingen och i det mjukvaruintensiva systemet?

    6. Vad är en "architecture runway"? Vilka problem försöker en sådan hantera och hur är det tänkt att man skall arbeta med den? Översiktligt svar bara!

    7. Stegvis förfining och iteration kan tillämpas på exempelvis systematisk nedbrytning. På vilket sätt är begreppen abstraktion, hierarki, modularitet och inkapsling viktiga begrepp/principer i detta sammanhang? Ge gärna ett exempel.

    8. Diskutera ”elements”, ”elements interaction design” och ”elements internal design” kopplat till ditt svar för fråga 7. Vad ser du för eventuella likheter och skillnader?

    9. Ge några exempel på vad som kan påverka ett arkitekturdesignsteg (architectural drivers)

    10. Gör en lista där du kortfattat beskriver vad olika UML-diagram kan användas till för att fånga arkitekturen i ett mjukvaruintensivt system och självklart även enskilda arkitekturbeslut.


Övningsuppgift - systematisk nedbrytning

