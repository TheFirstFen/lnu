
### About Markdown

Markdown is an easy-to-use plain text formatting syntax created by John Gruber.

To write a text in Markdown you need a Markdown editor. Fortunately VS Code comes with an easy-to-use Markdown editor. Hence, open a markdown file (.md file) in VS code and press ``preview`` in the upper right corner and you will see the Markdown code side-by-side with a view showing the rendered text.

To get started using Markdown we suggest that you open the file you are currently reading (ProjectTemplate.md), or (better) [this file](https://homepage.lnu.se//staff/jlnmsi/python/2021/Macdown.zip), in a Markdown editor and compare the rendered result with the given markdown code. Then Google various markdown tutorials to understand markdown symbols that are not obvious from the given examples. A few examples:

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

Try to be short and precise. We expect more than 2000, but less than 4000, words. 

Assume that the reader knows about Python. Give a reference and explain techniques introduced that we havn't presented in the course.

In what follow we give you the **mandatory report headlines** and brief comments about what we expect each section to contain. Make sure to remove our comments (and the Markdown intro above) in your final report.


************************

# Mini-project report 
Members: Donald Duck and Mickey Mouse  
Program: Software Technology  
Course: 1DV501 or 1DT901  
Date of submission: 2022-11-XX

## Introduction  
A brief introduction including a presentation of the project tasks. Present the project as a part of the course 1DV501/1DT901.  

## Part 1: Count unique words 1
The text should include:
- How many words did each of the two text files 
``life_of_brian`` and ``swedish_news_2020`` have?
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.

## Part 2: Implementing data structures
- Give a brief presentation of the given requirements
- For the hash based word set (HashSet), present (and explain in words):
 	* Python code for function ``add``, how to compute the hash value, and rehashing.
 	* Point out and explain any differences from the given results in ``hash_main.py``
 	
- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
 	* Point out and explain any differences from the given results in ``bst_main.py``.

## Part 3: Count unique words 2
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.
* What is the bucket list size, max bucket size and zero bucket ratio for HashSet, and the total node count, max depth and leaf count for BstMap, after having added all the words in the two large word files? (Hence, eight different numbers.)
* Explain how max bucket size and zero bucket ratio can be used to evaluate the quality of your hash function in HashSet. What are optimal/reasonable/poor values in both cases?
* Explain how max depth and leaf count can be used to evaluate the efficiency of the BstMap. What are optimal/reasonable/poor values in both cases?


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



