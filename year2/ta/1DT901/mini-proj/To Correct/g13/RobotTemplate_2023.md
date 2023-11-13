************************

# Robotic Lawnmower Project Report 
Members: Julia Bergön och Alexandra Klingvall  
Program: Master of Softwere Engineering  
Course: 1DT901  
Date of submission: 2023-11-04

### Introduction  
As a final task as a part of the course 1DT901 is to program a robotic lawnmower. This report will not only provide an overview of the project's objectives and scope but also delve into the methodologies, technical components, and challenges encountered throughout the process. 

### 1. Present Ground Maps

![Alt text](<Screenshot 2023-11-02 at 12.40.52-1.png>)

``small.csv`` Has a total area of 810 m^2 where of 603 m^2 are grass. That corresponds to 74% of the total area.

![Alt text](<Screenshot 2023-11-04 at 12.10.16.png>)

``my_map.csv`` Has a total area of 625 m^2 where of 240 aregrass. Thet corresponds to 33.6% of the total area.

``my_map.csv`` The map we have created shows a house woth a terrace, driveway and pool. Along the driveway as well as in the top right there are trees planted to work as obstacles here. From the house in the backyard there is a path leading to a pool. The starting-point for the mower at this house is to the right of the terrace aling the house wall.


### 2. Coordinate Map
We start by reading the chosen ``.csv`` file, we then save each line with the entries seperated into a list. We then change the entries from ``L, O, S`` to ``0, 1, 2`` for the visualization. Lastly we reverse the order of the lists inside the bigger list in order for the visualization code to put them in the cprrect order.

To know if the coordinate is outside or we check the potential step and checks if it is within the correct ``x`` and ``y`` coordinates. Then also if its position on the map is inside an obstacle.

```python
def is_outside(x, y,):
    if x >= len(cords_map) or x <= 0:
        return True
    elif y >= len(cords_map[0]) or y <= 0:
        return True
    if cords_map[int(x)][int(y)] == 1:
        return True
    else:
        return False
``````

With the ``x`` and ``y`` coordinates we dont have to do anything about the values being floats since it is still clear if it is smaller or larger than a decided value. However, checking if it is inside an obstacle doesnt work with floats. Here we use the ``x`` and ``y`` coordinates and make them into the closest (rounded downwards) int, which we then use to chec if the square if an obstacle or not.

### 3. Trace (Grade E requirement)
As described previously we difined a function 'def is_outside' that returnes a boolean value. If it returnes 'True' the mower is on the edge of the map or is about to hit an obstecle. However if it returnes 'False' the mower is still on the lawn on the map. This function was used when creating the function 'def one_step', to help calculate when the lawnmower needs to change direction.

The function 'def one_step':

````python
def one_step(x, y, new_ang, speed):
    x = x + speed * math.cos(new_ang) * dt  # xv
    y = y + speed * math.sin(new_ang) * dt  # yv
    return x, y
``````

This is the main function that takes all the steps.
It all begins with a program that iteretes through the map to find the start coordinates. With the start coordinates we could use both functions in a while loop to make all the steps through the given time span.

````python
while a < (h * 3600) / dt:
    x, y = one_step(x, y, new_ang, speed)
    if is_outside(x, y) is True:
        while is_outside(x, y) is True:
            new_ang = random.uniform(0, 2*math.pi)
            x, y = one_step(x, y, new_ang, speed)
            if is_outside(x, y) is True:
                # take a step back
                x, y = one_step(x, y, new_ang, -speed)
            else:
                xc.append(x)
                yc.append(y)
    else:
        xc.append(x)
        yc.append(y)
    a += 1
``````

Here it is shown how we start of with the start-coordinates and send them into the one step function to make the first step. After that we use the  is_outside function in an if statement to calculate if the lawnmower was about to hit an obstecle or go outside the map. While is_outside is True, one_step will calculate a new direction.

To be able to trace all the steps we also used two lists where we saved all the x and y coordinates seperatly. The coordinates were saved while an if statement using the function is_outside reurned False.



### 4. Coverage (Grade C requirement)
When running the program 10 times:
 - For ``small.csv`` the coverage ranges between 49-55% with 52.6% being the average.
![Alt text](<Screenshot 2023-11-03 at 12.44.28.png>)

- For ``my_map.csv`` the coverage varied a lot, ranging from 45-70% with 58% being the average.

![Alt text](<Screenshot 2023-11-03 at 12.47.19.png>)

	
1. N decides the amount of squares used in the coverage map. If N is a bigger number there are more squares. For a swuare to be count as cut, there has to be saved coordinates within the coordinates of the square. If there are less squares, the smaller that N is, there are a larger possibility of the mower meing inside the square. Therefore, the smaller N is, the higher the coverage-percentage will be. 

    A similar thing happens with ∆t. ∆t decised the distance between each saved coordinate the mower visits. If the distance is longer then there will be fewer saved point in the end whivh can leed to entire squares in the coverage map meing missed. Therefore to get a more exact result ∆t should me a smaller number.


2. The cutting width is influenced by the variable ∆t. Since the mower only can cut ine square at a time, if the squares are smaller then the cutting with is smaller. Therefore for the coverage, the variable that influences it is N.

3. With four hours daily the mower continuously mows aproximately 70-80% of the lawn, leading to the grass always being freshly cut.


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 

Getting the coverage map to work was difficult. The map kept being shown rotated and morrored. I eventially figured it out with reversing the list and taking the transpode before going through the coordinates to later chane it back to its original order for the visualization to be correct. If facing the same problem again we should take a step back and think it through step by step. What exactly is happening now and what is it that should happen instead, and from there work on a soltion to said problem. If we had more time we could have done more then we did now. Initially we had plans to go for a higher grade but with time manegement issues and poor planning we did not accomplish that this time.

### Project issues

In our team we worked a lot seperatly, but also made sure that the other person knew all of the changes when they were made. Both of us spent a lot of time on the project seperatly, but we sat together for two hours twice a week. The time we spent together was too really understand eachothers code and also help eachother if one would have gotten stuck on a problem.

Julia
- 
Responsible for:
- Reading the data and making it into a list
- is_outside()
- Visualizations
- Movement (Eccept one_step)
- Coverage
- Report
    - Coordinate map
    - Coverage
    - Parts of gound maps
    Project issues

Personally i found that coverage was the most diffictlt part. Creating the bigger map took a long time to make. Also, the cut parts kept showing up mirrord and transposed from the actual map. Figuing out how to fix that was one of the things that took longer for me. 

For a future time I would have started earlier with the project. It took us a few days to get started and i believe that if we would have gotten stardet earlier we probably would have had time for more.

I believe spent 6 hours weekly on average outside if the 4 hours we worked together.


Alexandra
-

For me I would have to say that the most callenging
parts have been to really understand how to tackle the different parts of the project. For eample how to create a function is not hard, but here the logic behind the functions was something that I struggled with. Also the usage of matplotlib was something that I found rather confusing. That was something I personally never have seen before and using it could be kind of difficult before one could understand the logic easier.
Though this project I have learnd that it really takes time to develop software and getting started as fast as possible is always the best solution. If we were given a similar problem I would get started sooner so that one had more time developing and making the code better and more effective.
If we were given more time I am sure that we would have made several


