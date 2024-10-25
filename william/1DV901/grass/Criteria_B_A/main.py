import numpy
from A_algorithm import main as A_sim
from base_algorithm import main as base_sim


def simulate(path, multiplier, times, choice, minutes,
             max_percentage, algorithm_choice, delta_t):
    choices = [A_sim, base_sim]

    if algorithm_choice == 3:
        simulations = choices
    else:
        simulations = [choices[algorithm_choice - 1]]

    simulations_info = []

    for sim in simulations:
        show_maps = False
        percentages = []
        times_lst = []
        for i in range(times):
            if i + 1 == times:
                show_maps = True
            info = sim(path, multiplier, minutes, max_percentage,
                       choice, delta_t, show_maps)
            percentages.append(info[0])
            times_lst.append(info[1])

        avg_percentage = round(sum(percentages) / len(percentages), 2)
        std_percentage = round(numpy.std(percentages), 2)
        avg_time = round(sum(times_lst) / len(times_lst), 2)
        std_time = round(numpy.std(times_lst),)

        simulations_info.append([avg_percentage, std_percentage,
                                 avg_time, std_time])
    return simulations_info


algo_choice = int(input('Which algorithm do you want to simulate? '
                        'A_algorithm(1), base_algorithm(2), both(3): '))
times = int(input("\nHow many runs do you want it to do? "))
delta_t = float(input("\nWhat do you want ∆t to be? "))
choice = int(input('Do you want any certain percentage(0) '
                   'or a certain time (1)? '))

user_percentage = 0
user_minutes = 0

if choice == 0:
    user_percentage = int(input("\nWhat percentage? "))
else:
    user_minutes = int(input("\nHow many minutes? "))

ground_map = input("\nWhich ground map do you want to simulate? ")
ground_map = 'ground_maps/' + ground_map + '.csv'
multiplier = int(input("What multiplier do you want to use? "))


simulation_results = simulate(ground_map, multiplier, times, choice,
                              user_minutes, user_percentage,
                              algo_choice, delta_t)


for i, sim in enumerate(simulation_results):
    if algo_choice == 1 or algo_choice == 3:
        print("\nA algorithm")
        if choice == 1:
            print('The standard deviation after',
                  f'{times} run(s) is {sim[1]}')
            print('The average percentage taken is',
                  f'{sim[0]}% after {times} run(s)')
        else:
            print('The standard deviation after',
                  f'{times} run(s) is {sim[3]}')
            print('The average time taken is',
                  f'{sim[2]} second(s) after {times} run(s)')

    if algo_choice == 2 or algo_choice == 3:
        print('\nBase algorithm')
        if choice == 1:
            print('The standard deviation after',
                  f'{times} runs is {sim[1]}')
            print('The average percentage taken is',
                  f'{sim[0]}% after {times} run(s)')
        else:
            print('The standard deviation after',
                  f'{times} run(s) is {sim[3]}')
            print('The average time taken is',
                  f'{sim[2]} second(s) after {times} run(s)')
