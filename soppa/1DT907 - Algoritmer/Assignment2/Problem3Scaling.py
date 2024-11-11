import matplotlib.pyplot as plt

# Results from the Java program
insert_sizes = [1000, 5000, 10000, 50000, 100000, 250000, 500000]
insert_times = [5.776583, 1.263, 1.688667, 8.441625, 14.94125, 16.185083, 28.473709]

get_sizes = [500, 2500, 5000, 25000, 50000, 125000, 250000]
get_times = [0.415375, 0.455958, 0.9145, 5.116416, 10.661, 25.237459, 58.519042]

delmax_sizes = [1000, 5000, 10000, 50000, 100000, 250000, 500000]
delmax_times = [0.272417, 0.276542, 0.353625, 1.790167, 0.885458, 2.307792, 2.191333]

swapprio_sizes = [1000, 5000, 10000, 50000, 100000, 250000, 500000]
swapprio_times = [0.078041, 0.357333, 0.719291, 3.803875, 3.124875, 8.093459, 14.477584]

# Scatterplot for insert times
plt.figure(figsize=(10, 6))
plt.scatter(insert_sizes, insert_times, label='Insert Time', color='blue')
plt.title('Insert Time Growth')
plt.xlabel('Number of Inserts')
plt.ylabel('Time (milliseconds)')
plt.legend()
plt.show()

# Scatterplot for get times
plt.figure(figsize=(10, 6))
plt.scatter(get_sizes, get_times, label='Get Time with double the size', color='green')
plt.title('Get Time Growth')
plt.xlabel('Number of Gets')
plt.ylabel('Time (milliseconds)')
plt.legend()
plt.show()

# Scatterplot for delmax times
plt.figure(figsize=(10, 6))
plt.scatter(delmax_sizes, delmax_times, label='Delmax Time', color='red')
plt.title('Delmax Time Growth')
plt.xlabel('Number of Delmax')
plt.ylabel('Time (milliseconds)')
plt.legend()
plt.show()

# Scatterplot for swapprio times
plt.figure(figsize=(10, 6))
plt.scatter(swapprio_sizes, swapprio_times, label='Swapprio Time', color='purple')
plt.title('Swapprio Time Growth')
plt.xlabel('Number of Swapprio')
plt.ylabel('Time (milliseconds)')
plt.legend()
plt.show()
