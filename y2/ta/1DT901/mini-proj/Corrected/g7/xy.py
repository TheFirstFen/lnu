import matplotlib.pyplot as plt
import math

x = [n/10 for n in range(0, 100)]
y = [math.sin(i) for i in x]
plt.plot(x, y)    # Deafult, lines connecting the dots
plt.show()

x = [n/4 for n in range(0, 40)]
y1 = [math.sin(i) for i in x]
y2 = [math.cos(i) for i in x]
plt.plot(x, y1, 'ro')      # ro ==> red circles
plt.plot(x, y2, 'b+')      # b+ ==> blue plus
plt.title('Sinus and cosinus')
plt.xlabel('x in range 0 to 10')
plt.ylabel('sin(x) as red, cos(x) as blue')
plt.show()


fig, (ax1, ax2) = plt.subplots(1, 2)  # Two plots called ax1 and ax2
x = [n for n in range(0, 20)]
y = [i**5 for i in x]

ax1.plot(x, y)
ax1.set_xlabel('n in range 0 to 20')
ax1.set_ylabel('n^5')
ax1.set_title('n vs n^5, non-logarithmic y-axis')
ax2.plot(x, y)
ax2.set_xlabel('n in range 0 to 20')
ax2.set_ylabel('n^5')
ax2.set_title('n vs n^5, logarithmic y-axis')
ax2.set_yscale('log')
plt.show()
