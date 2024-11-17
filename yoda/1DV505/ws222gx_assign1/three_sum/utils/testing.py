import time
from .plotting import make_plot


def benchmark_function(test_func, range_values: tuple, trials: int = 5):
    target = 10
    size_lst = list(range(*range_values))
    avg_times = []

    for size in size_lst:
        times = []
        lst = list(range(1, size + 1))

        for trial in range(trials):
            start_time = time.time()
            test_func(lst, target)
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)

        avg_time = sum(times) / trials
        avg_times.append(avg_time)
        target += 10

    return avg_times, size_lst


def fluctuations(func, name: str, range_values: tuple, trials: int = 3):
    avg_times_total = []
    for i in range(trials):
        current_avg_time = []
        current_avg_time, size_lst = benchmark_function(func, range_values, 5)
        avg_times_total.append(current_avg_time)

    labels = [f"Run {i+1}" for i in range(trials)]
    make_plot("List size", "Time in seconds", size_lst, avg_times_total,
              labels, f"Fluctuations amongst {trials} for {name}", fluc=True)
