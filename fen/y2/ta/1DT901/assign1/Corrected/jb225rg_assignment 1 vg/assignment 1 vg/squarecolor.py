#input plats
p = input("Enter a chess square identifier (e.g. e5): ")

#Seperating the letter and number and making them into ther own variables
l = p[0] #letter
n = int(p[1]) #number

#First devide them by every second row since they then start with the same colour
if l == "a" or l == "c" or l == "e" or l == "g":
    if n%2 == 0:    #if the number is even the colour is white
        print(p, "is White.")
    else:           #if the number is odd the colour is black
        print(p, "is Black.")

else:  #if they dint start with a, c, e, or, g.
    if n%2 == 0:  #even means black
        print(p, "is Black.")
    else:         #odd means white
        print(p, "is White.")