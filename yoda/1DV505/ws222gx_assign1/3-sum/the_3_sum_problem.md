# The 3-sum problem
## William Schröder

## I. Introduction
This report will detail what the 3-sum problem is, how the 3-sum problem can be solve using various of algorithms. Finally it will involve experiments showing how diffrent algorithms are faster than others.

### A. Problem Formulation
The 3-sum problem works like this: given a N size list of integers find all the combinations of 3 pairs that sum up to a given target. Where each instance of triplet has to be unique meaning that (5, 3, 2) is the same triplet as (2, 3, 5) and (3, 5, 2).

### B. Experminetal Setup
The experiments were conducted on a **Lenovo ideapad 5 pro** that has a AMD Ryzen 7 5000th series. When comparing the algorithms against each other the algorithms will have been ran on the same size list and with the same elements in that list. 

### C. Brute Force
The brute force algorithm uses three for loops where the first loop starts from 0 and goes to n-2 because there is 3 for loops so to avoid 

```py
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

    return list(unique_pairs)
```

#### Brute Force Experiments

#### Time Complexity


### II. Faster Approaches

### A. The two-pointer approach


### B 3-sum with caching


### C. Experiments with faster algorithms


### Summary and conclusions

