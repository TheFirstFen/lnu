import matplotlib.pyplot as plt
import random as rdm

# Frequencies for 10000 two dice rolls
freq = 11*[0]
for i in range(10000):
    r = rdm.randint(1, 6)+rdm.randint(1, 6)
    freq[r-2] += 1
print(freq)

# Show bar chart
x_pos = list(range(1, 12))   # [1,2,3,..., 10,11]
labels = [str(n+1) for n in x_pos]  # ['2','3', ... '11','12']
plt.bar(x_pos, freq)
plt.xticks(x_pos, labels)    # Give each position a label
plt.title("Two dice frequencies, rolls = 10000")
plt.xlabel("Two dice sums")
plt.ylabel("Count")
plt.show()
