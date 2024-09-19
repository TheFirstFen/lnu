### Uppgift 1: Funktionella Komponenter och deras Ansvar

1. **Pet Management**:
   - **Ansvar**: Hantera information om olika husdjur tillgängliga för försäljning, inklusive detaljer som ras, ålder, pris och hälsostatus. Anställda kan lägga till, uppdatera och ta bort djur från inventariet.

2. **Customer Management**:
   - **Ansvar**: Hantera kundprofiler inklusive kontaktinformation, preferenser och orderhistorik. Låter kunder registrera sig och uppdatera sin information. Kunder kan se tillgängliga husdjur och produkter.

3. **Order Processing**:
   - **Ansvar**: Hantera kundbeställningar för husdjur och relaterade produkter. Systemet fångar beställningsdetaljer och spårar orderstatus från mottagande till leverans.

4. **Product Management**:
   - **Ansvar**: Hantera olika produkter som säljs i butiken, såsom djurmat, leksaker och tillbehör. Anställda kan lägga till nya produkter, uppdatera produktinformation och övervaka lagernivåer.

5. **Service Management**:
   - **Ansvar**: Hantera tjänster som erbjuds av butiken, som grooming och träning. Kunder kan boka tjänster och anställda kan hantera servicekalendrar och avtalade tider.

6. **Supplier Management**:
   - **Ansvar**: Hantera leverantörer som tillhandahåller husdjur och produkter till butiken. Spårar leverantörsinformation och hanterar beställningar till leverantörer.

7. **Reporting**:
   - **Ansvar**: Generera rapporter om försäljning, lagernivåer och kundorder för att stödja beslutsfattande och affärsanalys.

### Uppgift 2: Beroenden mellan Komponenter

1. **Pet Management**:
   - **Requires Interface**: 
     - Kunddata från **Customer Management** för att se vilka kunder som är intresserade av specifika djur.
     - Orderinformation från **Order Processing** för att avgöra vilka djur som är sålda.
   - **Provides Interface**:
     - Information om husdjur till **Customer Management** och **Order Processing** för att kunder ska kunna se tillgängliga husdjur och beställa dem.

2. **Customer Management**:
   - **Requires Interface**:
     - Produktinformation från **Product Management** för att visa kunder tillgängliga produkter.
     - Orderhistorik från **Order Processing** för att visa kundernas tidigare beställningar.
   - **Provides Interface**:
     - Kunddata till **Order Processing** för att skapa och hantera kundbeställningar.
     - Kundpreferenser till **Pet Management** och **Service Management**.

3. **Order Processing**:
   - **Requires Interface**:
     - Kunddata från **Customer Management** för att skapa och hantera beställningar.
     - Produktinformation och lagernivåer från **Product Management**.
     - Tillgängliga tjänster och tider från **Service Management**.
   - **Provides Interface**:
     - Orderstatus till **Customer Management** och **Pet Management**.
     - Försäljningsdata till **Reporting**.

4. **Product Management**:
   - **Requires Interface**:
     - Leverantörsinformation från **Supplier Management** för att hantera produktinköp.
   - **Provides Interface**:
     - Produktinformation och lagernivåer till **Customer Management**, **Order Processing** och **Reporting**.

5. **Service Management**:
   - **Requires Interface**:
     - Kundbokningar från **Customer Management**.
   - **Provides Interface**:
     - Tjänsteinformation och tillgänglighet till **Order Processing** och **Customer Management**.

6. **Supplier Management**:
   - **Requires Interface**:
     - Beställningsinformation från **Product Management**.
   - **Provides Interface**:
     - Leveransinformation till **Product Management**.

7. **Reporting**:
   - **Requires Interface**:
     - Försäljningsdata från **Order Processing**.
     - Lagernivåer från **Product Management**.
     - Kunddata från **Customer Management**.
   - **Provides Interface**:
     - Rapporter till företagsledningen.

### Uppgift 3: UML Komponentdiagram

Jag kommer att skapa ett komponentdiagram som visar de identifierade komponenterna och deras interfaces.

### Uppgift 4: Fysisk Arkitektur

Systemet består av följande delar:

1. **Server för Backend och Databas**:
   - **Mjukvara**:
     - Databas (t.ex. MySQL eller MongoDB) för att lagra data om husdjur, kunder, produkter, ordrar och leverantörer.
     - Backend-applikation (t.ex. baserad på Java, Python eller Node.js) för att hantera affärslogik och API:er.

2. **Webbserver**:
   - **Mjukvara**:
     - Webbserver (t.ex. Apache eller Nginx) för att serva frontend-applikationen.
     - Frontend-applikation (t.ex. baserad på Angular, React eller Vue.js) som användargränssnitt för anställda och kunder.

3. **Kundens Enheter**:
   - **Mjukvara**:
     - Webbläsare eller mobilapplikation för att interagera med systemet.

4. **Administrativa Enheter**:
   - **Mjukvara**:
     - Desktop-applikation eller webbgränssnitt för administrativ personal att hantera systemet.

### Uppgift 5: UML Deploymentdiagram

Jag kommer att skapa ett UML deploymentdiagram som visar hur systemet är distribuerat över de fysiska enheterna och hur komponenterna är kopplade till varandra.

### Förklaring av UML Deploymentdiagram

Diagrammet ovan visar den fysiska arkitekturen för Pet Shop Management Systemet:

1. **Web Server (Frontend)**:
   - Hanterar frontend-applikationen som användare interagerar med via sina webbläsare eller mobila appar.
   - Kommunicerar med backend-servern för att hämta och skicka data.

2. **Backend Server (API & Business Logic)**:
   - Hanterar all affärslogik och API-ändpunkter. Tar emot förfrågningar från frontend och skickar relevant data.
   - Kommunicerar med databasen för att läsa och skriva data.

3. **Database Server (Data Storage)**:
   - Lagrar all data för systemet, inklusive information om husdjur, kunder, produkter, ordrar och leverantörer.
   - Tar emot och hanterar förfrågningar från backend-servern.

4. **Customer Device (Browser/App)**:
   - Kunder använder sina enheter (t.ex. mobiler eller datorer) för att interagera med systemet via en webbläsare eller app.

5. **Admin Device (Desktop/Web Interface)**:
   - Anställda och administratörer använder administrativa enheter för att hantera systemets data och processer via ett webbgränssnitt eller en skrivbordsapplikation.

Kommunikationen mellan enheterna är representerad av pilar som visar riktningen av dataflödet. 

Vill du att vi går vidare med att justera eller utöka detta diagram?
