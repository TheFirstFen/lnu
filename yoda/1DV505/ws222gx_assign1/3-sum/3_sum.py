import time
import matplotlib.pyplot as plt


def brute_force(lst, target):
    unique_pairs = set()

    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                v1, v2, v3 = lst[i], lst[j], lst[k]
                summa = v1 + v2 + v3
                if i == j or k == i or k == j:
                    continue
                if summa == target:
                    unique_pairs.add((v1, v2, v3))

    return unique_pairs


def two_pointer(lst, target):
    unique_pairs = set()
    lst = sorted(lst)  # Two-pointer requires a sorted list

    for fP in range(len(lst) - 2):  # Use `-2` for the three-pointer approach
        if fP > 0 and lst[fP] == lst[fP - 1]:  # Skip duplicate values for the fixed pointer
            continue

        left_p = fP + 1
        right_p = len(lst) - 1

        while left_p < right_p:
            summa = lst[fP] + lst[left_p] + lst[right_p] - target
            if summa == 0:
                unique_pairs.add((lst[fP], lst[left_p], lst[right_p]))

                # move side to side to avoid left pointer and right pointer to be dups
                while left_p < right_p and lst[left_p] == lst[left_p + 1]:
                    left_p += 1
                while left_p < right_p and lst[right_p] == lst[right_p - 1]:
                    right_p -= 1

                # increase the pointers for the sequence
                left_p += 1
                right_p -= 1
            elif summa < 0:
                left_p += 1
            else:
                right_p -= 1

    return unique_pairs


def caching(lst, target):
    cash = set()
    unique_pairs = set()
    k = 0
    for i in range(len(lst) - 2):
        for j in range(len(lst) - 1):
            summa = lst[k] + lst[i] + lst[j] 
            if summa in cash:
        cash.add(lst[])

def benchmark_function(test_func, target=50, min_size=0, max_size=1000,
                       step=50, trials=5):
    size_lst = list(range(min_size, max_size + 1, step))
    avg_times = []

    for size in size_lst:
        print(f"Now running size: {size}")
        times = []
        lst = list(range(1, size + 1))

        for _ in range(trials):
            start_time = time.time()
            test_func(lst, target)  # Run the passed-in function
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)

        avg_time = sum(times) / trials  # Calculate average time for this list size
        avg_times.append(avg_time)
        target += 10  # Adjust target incrementally

    # Plotting the results
    return avg_times, size_lst


avg_times_bf, size_lst = benchmark_function(brute_force)
avg_times_tP, size_lst = benchmark_function(two_pointer)

plt.plot(size_lst, avg_times_bf, "-+r")
plt.plot(size_lst, avg_times_tP, "-+b")
plt.xlabel("List Size")
plt.ylabel("Average Execution Time (s)")
plt.show()