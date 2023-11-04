sum= int(input("Provide a three digit number: ")) #kopplade variebeln med "input" för de tre slumpmässiga talen och användt "int" för att det ska vara bara heltal.

rightmost_digit = sum % 10 #använde modulus för att veta siffran som är längst till höger.

middle_digit = (sum // 10) % 10 #här delat siffran med tio och sen modulus för att vet talen som är i mitten

leftmost_digit = sum // 100 #här delat talen med 100 för att bli av med de två siffrana, den mittersta och den längst till höger.

total= rightmost_digit + middle_digit + leftmost_digit #sist har jag adderat dem och kopplat dem i en och samma variabel.

print(f"Sum of digits: {total}") #här har jag printat det totala summan.