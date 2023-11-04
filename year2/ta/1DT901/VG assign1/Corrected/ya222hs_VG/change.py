prise= int(input("Price: ")) #här har jag börjat med prist, att sktiva priste med hälp av input. 
payment= int(input("Payment: ")) #Och här för de pengerna som ska betalas 
change=payment-prise #Priset kommer dras från det som kommer betalas, och har kopplat dem med en variabel "change"
change=round(change) #avrundat för att få ett heltal, alltså utan öre
tu=change//1000 #här för att veta hur mycket change får jag i tx. 1000, 500 och 200 osv.
tu1=change%1000
fe=tu1//500
fe1=tu1%500
tv=fe1//200
tv1=fe1%200
hu=tv1//100
hu1=tv1%100
fem=hu1//50
fem1=hu1%50
tjo=fem1//20
tjo1=fem1%20
tio=tjo1//10
tio1=tjo1%10
f=tio1//5
f1=tio1%5
t=f1//2
t1=f1%2
t1=round(t1)
print("Change:", change,"kr\n" #här har jag printat all införmation jag har räknat uppåt
    +"\t1000kr bills:", tu,"\n"
    +"\t500kr bills:", fe,"\n"
    +"\t200kr bills·", tv,"\n"
    +"\t100kr bills:", hu,"\n"
    +"\t50kr bills:", fem,"\n"
    +"\t20kr bills:", tjo,"\n" 
    +"\t10kr coins:", tio,"\n"
    +"\t5kr coins:", f,"\n"
    +"\t2kr coins:", t,"\n"
    +"\t1kr coins:", t1,"\n")