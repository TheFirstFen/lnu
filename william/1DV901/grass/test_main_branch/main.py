import numpy
from A_algorithm import main as A_sim
from test_main_branch.base_algorithm import main as base_sim


def simulate(path, multiplier, times, choice,
             minutes, max_percentage):

    simulations = [A_sim, base_sim]
    simulations_info = []
    for sim in simulations:
        show_maps = False
        percentages = []
        times_lst = []
        for i in range(times):
            info = sim(path, multiplier, minutes, max_percentage,
                       choice, show_maps)
            percentages.append(info[0])
            times_lst.append(info[1])
            if i + 1 == times-1:
                show_maps = True

        avg_percentage = round(sum(percentages) / len(percentages), 2)
        std_percentage = round(numpy.std(percentages), 2)
        avg_time = round(sum(times_lst) / len(times_lst), 2)
        std_time = round(numpy.std(times_lst), 2)

        simulations_info.append([avg_percentage, std_percentage])
        simulations_info.append([avg_time, std_time])

    return simulations_info


times = int(input("How many runs do you want it to do? "))


choice = int(input("Do you want any certain percentage(0) "
                   "or a certain time (1)? "))

user_percentage = 0
user_minutes = 0

if choice == 0:
    user_percentage = int(input("What percentage? "))

else:
    user_minutes = int(input("How many minutes? "))

ground_map = input("Which ground map do you want to simulate? ")
ground_map = 'ground_maps/' + ground_map + '.csv'
multiplier = int(input("What multiplier do you want to use? "))

simulation_results = simulate(ground_map, multiplier, times, choice,
                              user_minutes, user_percentage)


if choice == 1:
    print("\nA algorithm")
    print('The standard deviation after ',
          f'{times} run(s) is {simulation_results[0][1]}')
    print('The average percentage taken is is ',
          f'{simulation_results[0][0]}& after {times} run(s)')

    print('\nBase algorithm')
    print('The standard deviation after ',
          f'{times} runs is {simulation_results[2][1]}')
    print('The average percentage taken is is ',
          f'{simulation_results[2][0]}% after {times} run(s)')

else:
    print("\nA algorithm")
    print('The standard deviation after ',
          f'{times} run(s) is {simulation_results[1][1]}')
    print('The average time taken is is ',
          f'{simulation_results[1][0]} second(s) after {times} run(s)')
    print('\nBase algorithm')

    print('The standard deviation after ',
          f'{times} run(s) is {simulation_results[3][1]}')
    print('The average time taken is is ',
          f'{simulation_results[3][0]} second(s) {times} run(s)')
