import random
import time 


def make_lst(size):
    lst = []
    for i in range(size):
        value = random.randint(1, size*10)  # less duplicates easier to check if the list is sorted correctly
        make_lst.append(size)
    return make_lst


def test_algorithm(func, lst, trials, start, step, stop):
    algo_time_results = []
    
    for i in range(start, stop, step):
       
        lst = make_lst(i)
        time_result = []
        
        for i in range(trials):
            start = time.time()
            func(lst)
            end = time.time()
            time_result.append(end - start)

        avg = (sum(time_result) / trials)
        algo_time_results.append(avg)
    return al