# Info from user
sal = input("Salaries separated by a space: ")
# String to a list
diff = sal.split()
sal = [int(a) for a in diff]
# Variables
med = 0
avr = 0
gap = 0
# Computing
if len(sal) % 2 != 0:
    med = sal[round(len(sal) / 2)]
else:
    med = (sal[round(len(sal) / 2)] + sal[round(len(sal) / 2 + 1)]) / 2
for i in range(len(sal)-1):
    avr += sal[i]
gap = max(sal) - min(sal)
# Displaying
print("Average:", avr, "\n", "Median:", med, "\n", "gap:", gap)
