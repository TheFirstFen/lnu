
### About Markdown

Markdown is an easy-to-use plain text formatting syntax created by John Gruber.

To write a text in Markdown you need a Markdown editor. Fortunately VS Code comes with an easy-to-use Markdown editor. Hence, open a markdown file (.md file) in VS code and press ``preview`` in the upper right corner and you will see the Markdown code side-by-side with a view showing the rendered text.

To get started using Markdown we suggest that you open the file you are currently reading (RobotTemplate.md), or (better) [this file](https://homepage.lnu.se//staff/jlnmsi/python/2021/Macdown.zip), in a Markdown editor and compare the rendered result with the given markdown code. Then Google various markdown tutorials to understand markdown symbols that are not obvious from the given examples. A few examples:

Python code markup:

```python
def max(a,b):
	if a > b:
		return a
	else:
		return b
```

Inserting images (using HTML markup):

<img src="http://homepage.lnu.se/staff/jlnmsi/python/2020/cos_sin.png" width="400"/>


This is a table with left- , center-, and right-allgned columns:

| Left Aligned  | Center Aligned  | Right Aligned |
|:------------- |:---------------:| -------------:|
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |

The left- and right-most pipes (`|`) are only aesthetic, and can be omitted. The spaces don’t matter, either. Alignment depends solely on `:` marks in the lines under the column titles.

## Regarding the report template

The template below is in English. Feel free to write your report in Swedish or English. 

We expect each team to present their report as their README.md in the Gitlab repository.

Assume that the reader knows about Python. Give a reference and explain techniques introduced that we havn't presented in the course.

In what follow we give you the **mandatory report headlines** and brief comments about what we expect each section to contain. Make sure to remove our comments (and the Markdown intro above) in your final report.

The report for the lawnmower project is not really a complete report where you decribe your results and everything you have done. It more like a list  of separate exercises focusing on different parts of the project.

Finally, try to be short and precise but still readable.  


************************

# Robotic Lawnmower Project Report 
Members: Donald Duck and Mickey Mouse  
Program: Master of ...   
Course: 1DT901  
Date of submission: 2023-11-XX

### Introduction  
A brief introduction including a presentation of the project task. Present the project as a part of the course 1DT901.  

### 1. Present Ground Maps
The text should include:

- Two matplotlib plots displaying the maps ``small.csv`` and ``my_map.csv``.
- For each displayed map, present the map area (m^2) and lawn area (m^2 and percentage).
- Describe the scenario that is the base for your map ``my_map.csv``.

### 2. Coordinate Map
The coordinate map ``coord[X][Y]`` is a mapping from integer coordinates ``X,Y`` to what type of ground (Obstacle, Lawn, Start) we have at this point. 

- Explain how you computed this map starting from the ground map. Feel free to provide short code fragments as a part of your explanation.
- During the trace calculation, the coordinate map is used to decide whether we are outside the lawn or not. Show and explain the Python code used to decide if a certain trace position ``x,y`` (floats) is outside the lawn or not.

### 3. Trace (Grade E requirement)
The text should include:

- The trace is a sequence of steps ``x,y``. Explain how we go from one step to another. The explanation should include how we handle obstacle bounces. 
- Present two matplotlib plots displaying the trace after 2 hours for the ground maps ``small.csv`` and ``my_map.csv``.	

### 4. Coverage (Grade C requirement)
To compute the coverage we divide each square meter into a smaller ``N x N`` grid.

- What is the coverage after 2 hours for the ground maps ``small.csv`` and ``my_map.csv`` using a ``5 x 5`` grid? Also, present two corresponding matplotlib plots displaying the coverage. 	

Below follows a few questions. Motivate your answers and your assumptions.

+ How do the two parameters ∆t and N influence the coverage?
+ What can you say about the effective cutting witdh? What parameters influence it?
+ What is a reasonable workload (hours of work per day) for the robot to handle ground map ``small.csv``? 

### 5. Multiple Simulations (Grade B requirement)
Add support for multiple simulations in a single run of the program that makes it possible to compute average and standard deviation for the coverage for a given map after a given time.

- Compute and present, after 10 simulations, the average and standard deviation for the coverage after 2 hours for the ground maps ``small.csv`` and ``my_map.csv``?
- What lawnmower time is needed to get a 90% coverage for the ground maps ``small.csv`` and ``my_map.csv``? How did you compute the required lawnmower time?

### 6. Improved Simulation (Grade A requirement)
Try to make the simulation more realistic and/or suggest changes in the Robot AI that improves the coverage. Explain your improvements and present experiments and matplotlib visualizations that motivates and/or evaluates them. Show results for the two ground maps ``small.csv`` and ``my_map.csv``. 


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming?
- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
- How could the results be improved if you were given a bit more time to complete the task.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.
 	* Estimate hours spend each week (on average)
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.



