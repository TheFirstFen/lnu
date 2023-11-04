# Read multiple space separated integers from keyboard
text = input("Provide salaries: ")
words = text.split()
ints = [int(w) for w in words]

ints.sort()

# Beräkna medianen genom median formeln
a = len(ints)
if a % 2 == 0:
    median = (ints[a//2] + ints[a//2-1])/2
else:
    if a % 2 == 1:
        median = ints[a//2]
print("Median:", median)

# Beräkna average genom average genom att ta totalen av ints delat på len(ints)
total = sum(ints)
average = total // len(ints)
print("Average:", average)

# Beräkna gap genom att ta största värdet subtraherat med minsta värdet
gap = max(ints) - min(ints)
print("Gap:", gap)
