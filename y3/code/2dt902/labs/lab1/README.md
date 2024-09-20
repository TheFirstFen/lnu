# 2DT902 : Assaignment 1 : ![Samuel Berg]<sb224sc@student.lnu.se>

## Uppgift 1.
Fokusera på funktionaliteten i beskrivningen. Vilka funktionella
komponenter kan du identifiera? Vilket ansvar (funktionellt) har respektive
komponent? Svara i text med komponentnamn och beskrivning av ansvaret

**User/Supplier components**
- User Authentication & Registration
    * Account creation
    * Login
- Profile Management
    * Delivery Address
    * Payment Information/Option
    * Order Managment(including previous orders)
- Search & Products Management
    * Start page with popular/recommended products
    * Search feature

**Employee components**
- Product management
    * Manage availability of products
    * Manage services
- Manage Customer accounts
    * View Delivery optins
- Manage Orders
    * Change order status
    * Cancel/Refund Orders
- Supplier Management
    * Manage Supplier Information
- Reporting
    * View Daily/Weekly/Monthly/Yearly reports

**Transaction components**
- Cart
    * Adding & Removing of products
- Delivery Options
    * Pick-up at store
    * Delivery Service
- Payment API
    * Third-party payment integration
- Reporting
    * Number of Sales
    * Value of Sales
    * Number of Sold Products(of each product)

**Communication components**
- Order status
    * Notified on updates on your order(recived, sent, deliverd, ready for pick-up)
- Product reviews/feedback
    * Can leave reviews on products and services that they have ordered and recived
- Reporting
    * Collect Summary of Reviews

**Data storage component**
- Stores the data of all other components

The ***user/supplier component*** **Motivate!!**

The ***employee component*** **Motivate!!**

The ***transaction component*** **Motivate!!**

The ***communication component*** **Motivate!!**

The ***data storage component*** **Motivate!!**


## Uppgift 2. 
Analysera beroenden mellan komponenter. Vilka funktioner som andra
komponenter ansvarar för behöver en komponent för att fullfölja sitt ansvar avseende
den funktionalitet som den fått allokerat?
Svara i text och identifiera funktionalitet som andra komponenter behöver. Beskriv
dem som ”provides” interface för komponenten. På samma sätt dokumenterar du
funktionalitet en komponent behöver i ”requires interface”.

## Uppgift 3.
Rita ett UML komponentdiagram med de komponenter du identifierat, koppla
samman komponenterna med interface, providesßà requires.

## Uppgift 4.
Fundera lite på den fysiska arkitekturen (systemarkitekturen). Vilka delar består
systemet av, vilka enheter ingår och vilken mjukvara installeras på respektive enhet?
Redovisa i textform.

## Uppgift 5.
Rita ett UML deploymentdiagram som illustrerar det du identifierat i uppgift 4.
