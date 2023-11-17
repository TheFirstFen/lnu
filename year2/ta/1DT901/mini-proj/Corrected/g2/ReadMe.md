************************

# Robotic Lawnmower Project Report 
Members: Linus Lorensson  
Program: Master of Software engineering
Course: 1DT901  
Date of submission: 2023-11-03  

### Introduction  
Our project consisted of creating a robotic lawn mower simulation. when using different maps we get a plot with results of where the lawn mower went and what kind of coverage it had.

### 1. Present Ground Maps

Here are the 2 chosen ground maps, ``small.csv`` and ``own.csv``.

<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/small.png" height="400" width="400"/>
<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/My%20own.png" height="400" width="400"/>

- ``small.csv`` had a total area of 30x27 (m^2) totaling 810 square meters, 208 m^2 of which is the house and other obstacles. That would make the lawn 600 m^2 and covering 74.32% of the total plot.

- ``own.csv`` has a total area of 20x25 (m^2) totaling 500 square meters, 92 m^2 of which is house and obstacles. That would make the lawn 408 m^2 and covering 81.6% of the total plot.

The base scenario for ``own.csv`` is a house with a backyard with a fenced section at the top with trees symmetrically placed along it. Near the middle there's garden furniture along with a lone apple tree.

### 2. Coordinate Map
To start reading in the map i use my reader function that import from the ``scaler.py`` file.
This function goes through the "``Name.csv``" file row by row and adds each row to a list, replacing each L, O or S with their corresponding number. In this case i replace L with 0, S with 1 and O with 2.

```python
while count < scaler:
    if i == "L":
        col_list.append(0)
    elif i == "S":
        col_list.append(1)
	elif i == "O":
		col_list.append(2)
	count += 1
```
As you can see in this code here, it creates a list that then adds it to the row_list. This is the list that becomes the coordinate map. As you can see it also repeats the number and row based on a scaler value, this is how the map gets upscaled if the users wants to.

When this coordinate map is first created the X axis is flipped.

```python
    row_list, path, scaler = map_gen(name, scaler)
    cord_map = row_list.copy()
    cord_map.reverse()
```
So to fix this I use the reverse function to flip the list on the x axis. Now X = 0 and Y = 0 is the actual origo, or the bottom left on the plot when printed.

To later determine if the "trace" hits an obstacle or not, I used the following code to check for this. 

```python
	new_x = x + (dx / N)
	new_y = y + (dy / N)

	if new_x < 0 or new_x >= len(move_map):
		break
	if new_y < 0 or new_y >= len(move_map[0]):
		break
```
First I make 2 variables for the new x and y coordinates. I then check if these new coordinates would land outside the map. If it passes all checks it then assigns these new_x and new_y values to be the new coordinates of the lawn mower.

### 3. Trace (Grade E requirement)

First step of the trace starts from the start square, also known as 1 on the coordinate system. Once found it's recorded using the history function that adds the coordinates of the steps to a list.
This is done every time a new step that isn't into an obstacle or outside the map has been taken.

```python
	if move_map[int(new_x)][int(new_y)] == 2:
		break
```

If the move breaks here because the new coordinates was a wall or outside the map. It goes back to the main function where if the time is not longer than set time limit, it calls the move function again. Takes a new random direction from the direction function and goes until either time runs out, it hits a wall or lands outside again. This is on repeat until the time has run out.

Below you can see 2 maps of the traces after running ``small.csv`` and ``own.csv`` on a time limit of 2 hours.

<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/small_trace.png" height="400" width="400"/>
<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/own_trace.png" height="400" width="400"/>

### 4. Coverage (Grade C requirement)
I did my program a bit differently, at first I encountered some problems with working with multiple coordinate systems so instead of using 2 different systems, I use 1 for both computing trace and coverage. I do this by scaling the entire first coordinate system by the scaler that user inputs at the start of the program.

Once the lawn mower has been simulated for ``X`` amount of time. I then extrapolate the coordinates from the ``move_history`` and change all the squares that have been cut by changing the corresponding square to ``3`` instead of ``0`` if it is found to be cut in ``move_history``. I changed this later on the B (with percentages) and A grade mower, as I moved a section of this code to another function to continuously update the map for what has been cut.

Below you can see both the ``line_map`` and ``coverage`` plot of ``small.csv`` and ``own.csv`` that has been set to run with a time limit of 2 Hours scaled up by, in my case ``multiplier = 5``

<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/small_coverage.png" height="400" width="400"/>
<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/own_coverage.png" height="400" width="400"/>

Below follows a few questions. Motivate your answers and your assumptions.

+ How do the two parameters ∆t and N (``scaler`` in my code) influence the coverage?

I see the variable ``∆t`` as basically increasing the resolution of the ``move_history`` by ``∆t`` times, N in my code is called ``scaler`` and that variable increase the resolution of the ``lawn map`` and practically "decreases" the size of the lawn mower. 

+ What can you say about the effective cutting width? What parameters influence it?

Basically the only thing influencing the cutting width would be ``N`` in this case, since that variable in essence "stretches" the lawn but the mower stay the same size. So the effective cutting width would be in the ballpark of 1 to 2 over N (1~2/N), my reasoning to that being that if you look at the lawnmower cutting diagonally sometimes it cuts 2 squares that are next to each other as shown bellow

+ What is a reasonable workload (hours of work per day) for the robot to handle ground map ``small.csv``? 

Judging from the coverage map averaging around 55% after 2 hours, I would say that if it cut for about 2 to 3 hours, 3 times a week the lawn should on average be at a decently cut height. Without wasting too much electricity on running the lawn mower whenever possible. 

### 5. Multiple Simulations (Grade B requirement)
Add support for multiple simulations in a single run of the program that makes it possible to compute average and standard deviation for the coverage for a given map after a given time.

- Compute and present, after 10 simulations, the average and standard deviation for the coverage after 2 hours for the ground maps ``small.csv`` and ``my_map.csv``?

Here are the best and worst runs from running ``small.csv`` 10 times.

<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/small_best.png" height="400" width="400"/>
<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/small_worst.png" height="400" width="400"/>

The run had an average cut of 53% with a standard deviation of 2.8%.

Here are the best and worst runs from running ``own.csv`` 10 times.

<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/own_best.png" height="400" width="400"/>
<img src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/own_worst.png" height="400" width="400"/>

The run had an average cut of 65% with a standard deviation of 2.9%.

- What lawnmower time is needed to get a 90% coverage for the ground maps ``small.csv`` and ``my_map.csv``? How did you compute the required lawnmower time?

On average the lawnmower took 21575 seconds or around 6 hours to get the ``small.csv`` map 90% cut. Where as on ``own.csv`` it took an average of 18520 seconds to get 90% of the lawn cut.

I computed these times by making the user either decide on a needed percentage of the lawn to be cut or setting a time limit for the lawn mower. If the user decides to use the percentage option I instead of cutting until a set time has passed, I make sure that the lawn has been cut by using a while statement as seen here.

```python
    elif choice == 2:
        while cover < percent:
```
Where ``cover`` is the current percentage of the lawn that has been cut, and ``percent`` is the variable the user input at the start of the simulation and also the cut-off for when the lawnmower should stop cutting the lawn. The code above here is seen in my ``move`` function, but also found in the ``main_sim`` function.

### 6. Improved Simulation (Grade A requirement)
I was thinking that maybe instead of only using a randomized angle on impact of wall. make the mower change direction randomly at an user-input interval. For example make the mower turn a random direction ever ``4`` meters it's moved or a random interval, or upon impact of the wall of course.

After trying this out i find that some settings can sometimes outperform the only collide turn algorithm. But it's also inconsistent since im currently using a ``randint`` function to get a random number of how many moves to make before we turn.

For example I used the following code to make a random interval of moves the mower have to take at the minimum, if it does not collide with a wall before the end of the interval. The robot then makes a turn in a random direction directed by the ``direction`` function.
```python
least_tries = random.randint(N ** 2, N ** 4)
```
I got an average time of 18319 seconds to cut 90% on ``own.csv``. Which is an improvement, but.. the next time I ran with the same settings I got an average time of 15906 seconds. Which means that this algorithm CAN beat the original, but it is way more inconsistent.

To test my theory instead of only running 10, I ran 100 simulations at 90% coverage, the average time I got was 17274 seconds. This compared to when running the original algorithm 100 times at 90% coverage that gave an average time of 17920 seconds. This would lead me to believe that the proposed algorithm of turning sometime between ``x`` and ``y`` time could be further optimized to finding the best interval of time. The interval of time I used is shown above, where ``N`` is ``∆t``.

Running the new algorithm on the ``small.csv`` map 100 times at 90% coverage I got an average time of 21294 seconds, running it on the old algorithm 100 times at same coverage yielded an average time of 21310 seconds. This might just mean that either the algorithm of turning on based intervals either isn't it's optimal value and needs further testing, OR the map is just not suitable for this specific algorithm.

From further testing it seems that this change in the algorithm seem to have barely any effect to actual coverage. I've run it multiple times (over 1000 times but usually in intervals of 10 to 100 times) and the result is unfortunately not very consistent. So as a final attempt at trying to find out wether my algorithm actually was better or not I ran 1000 simulations of each scenario which you can see bellow. Hopefully this will show a better average number to prove which one would be the better option.

First off I ran the small map with the old only turn when hit wall algorithm and these are the results.

- To cut 90% of ``small.csv`` using the "only turn on obstacle hit", it took an average run time of 21419 seconds. 

<img title="Best run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/best_of_1000_small_old.png" height="400" width="400"/>
<img title="Worst run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/worst_of_1000_small_old.png" height="400" width="400"/>


After that I ran same algorithm on my ``own.csv`` map and these are the results.
- To cut 90% of ``own.csv`` using the "only turn on obstacle hit", it took an average run time of 18313 seconds. 

<img title="Best run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/best_of_1000_own_old.png" height="400" width="400"/>
<img title="Worst run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/worst_of_1000_own_old.png" height="400" width="400"/>

I then ran my "change direction after ``X`` steps or on hitting wall" algorithm. On ``small.csv``, these are the results. 
- To cut 90% of ``small.csv`` using the "only turn on obstacle hit", it took an average run time of 21391 seconds. 

<img title="Best run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/best_of_1000_small_new.png" height="400" width="400"/>
<img title="Worst run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/worst_of_1000_small_new.png" height="400" width="400"/>

And lastly the lousy named algorithm on ``own.csv``, these are those results.
- To cut 90% of ``own.csv`` using the "only turn on obstacle hit", it took an average run time of 17902 seconds. 

<img title="Best run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/best_of_1000_own_new.png" height="400" width="400"/>
<img title="Worst run" src="https://gitlab.lnu.se/1dt901/student/cidmv-ht23-2/mini-project/-/raw/main/images/worst_of_1000_own_new.png" height="400" width="400"/>

So with these final results I can say that there is in fact, "some" improvement to this over the old algorithm.
With these comparisons, on ``small.csv`` the old algorithm did a run on an average of 21419 seconds. Where as my algorithm did it on an average of 21391 seconds, on average 28 seconds faster! And on ``own.csv`` the old algorithm ran on average 18313 seconds where as mine did an average of 17902 seconds, that's an average of 411 seconds faster! These are all small and probably within the margin of error, but an improvement in my eyes non the less.

 I feel this paints a better picture for my algorithm. Although the changes in behavior are minimal, as you can see the turns after ``X`` distance seems to have an impact on results, however minimal they are.

## Project conclusions and lessons learned
### Technical issues 
- What were the major technical challenges as you see it? What parts were the hardest and most time consuming?

Mainly understanding the algorithmic thinking behind the mower and where to start.

- What lessons have you learned? What should you have done differently if you now were facing a similar problem.

More immediate questions to teacher or teacher assistant to get input on where to get started. Although doing it first without input help my solution to this assignment be more unique.. I hope, while still retaining functionality.

- How could the results be improved if you were given a bit more time to complete the task.

I would have had without a doubt time to fix a better algorithm for A grade. I think working alone had a big impact on this though as having a partner that i could divide my work with would allow more time for A grade programming. But still, I do not regret working alone.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?

Worked by myself so I didn't really have any issues with communications.

- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.	
	* Estimate hours spend each week (on average)
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.

 I did everything by myself. The lab opportunities was of great help to me for brainstorming and focus on getting stuff done. On average I think I spent about 15 hours a week in some shape or form.

 I have learnt a lot. Notably how to think about lists and how they're structured, I had a big issue with surface level copying lists where editing 1 of the lists edited all of the lists, even tho they were individually added lists. I think that would be a great idea to learn about that in a previous lab assignment. Surface and deep level list manipulation would have been great to know before this mini-project.



