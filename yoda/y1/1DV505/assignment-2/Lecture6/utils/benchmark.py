import random
import time


# brought from a1
def make_lst(size: int, orderd):
    if not orderd:
        lst = []
        for i in range(size):
            value = random.randint(1, size*10)
            lst.append(value)
    else:
        lst = [i for i in range(size, 0, -1)]
    return lst


def test_algorithm(funcs: list, trials: int, range_values: tuple,
                   orderd):
    # stores the avg time for each function for each trial
    algo_time_results = {key: [] for key in range(len(funcs))}
    sizes = []

    for i in range(*range_values):
        lst = make_lst(i, orderd)
        sizes.append(i)
        # stores every time for each trial for each function
        total_times = {key: 0 for key in range(len(funcs))}

        for j in range(trials):
            for func in range(len(funcs)):
                start_time = time.time()
                funcs[func](lst.copy())  # Run the algorithm
                end_time = time.time()
                total_times[func] += (end_time - start_time)

        # after every round of a certain list size calculate avg time
        # for that trial for each function
        for func in range(len(funcs)):
            avg_time = total_times[func] / trials
            algo_time_results[func].append(avg_time)

    return algo_time_results, sizes
