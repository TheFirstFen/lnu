income= int(input("Please provide monthly income: ")) #här får man skriva sin inkomst
if income > 0 and income < 38000: print("Corresponding income tax: ", round(income * 0.3))
#här om inkomsten mellan 0 och 38000 ska den avrundas och multiplaseras med 0.3 för veta hur mycket kommer pengar bli kvar efter räntan.

elif 38000 <= income <= 50000: #Om inkomsten inte uppfyller det första villkoret, kontrolleras det om inkomsten ligger mellan 38000 och 50000.
    x= 38000 * 0.3 #här har jag beräknat Först skatten för de första 38000 med en skattesats på 30%.

    y= (income - 38000) * 0.35 #Sedan beräknade jag skatten för beloppet över 38000 (upp till inkomsten) med en högre skattesats på 35%.
    print("Corresponding income tax: ", round(y + x)) #De två skattebeloppen läggs ihop och det totala skattebeloppet visas, avrundat till närmaste heltal.

else: #Om inkomsten inte uppfyller något av de två tidigare villkoren (dvs. om inkomsten är över 50000), går koden in i detta villkor.
    x = 38000 * 0.3 #Precis som tidigare beräknas skatten för de första 38000 med en skattesats på 30% och för inkomsten mellan 38000 och 50000 med en skattesats på 35%.
    y = (50000 - 38000 ) * 0.35 
    z = (income - 50000) * 0.40 #För all inkomst över 50000 används den högsta skattesatsen på 40%.
    print("Corresponding income tax: ", round(x + y + z)) #De tre skattebeloppen läggs ihop och det totala skattebeloppet visas, avrundat till närmaste heltal.

