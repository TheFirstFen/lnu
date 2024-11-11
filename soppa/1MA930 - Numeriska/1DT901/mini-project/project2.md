# Mini-project report 
Members: Minh Anh Pham and Jesper Wingren
Program: Software Technology  
Course: 1DV501 or 1DT901  
Date of submission: 2022-11-06

## Introduction  
For the course 1DV501/1DT901 a project has been assigned. This project is about understanding hashing and binary search trees. In order to get a good understanding of the data structures, two large text files from previous assignments will be used as input data. These text files are called "Life of Brian and "Swedish News". The assignment can be divided into three parts:

1. Count unique words using Python's set and dictionary
2. Implement two data structures suitable for working with words as data: a) A hash based set, and b) a binary search tree (BST) based map (dictionary).
3. Use your two data structures to repeat Part 1 (counting unique words)

## Part 1: Count unique words 1
Task 1 is divided into two parts. the first part is to create a program in order to count the number of unique words for a specific file. In our case we used the files "life_of_brian" and "swedish_news_2020". Running the program gave us 2034 unique words for "life_of_brian" and 387407 for "swedish_news_2020". 

The second task is to create a program that presents and counts the 10 most used words for each of the two files in part 1. In order to implement the top 10 list a few fuctions had to be created. Firstly a function that counts the amount of occurrences a word is presented in the file. Our function looks like this: 

```python
def count_occurances(path, name):
    dct = {}
    # opens and reads file
    with open(path + "/data/" + name, "r") as file:
        for line in file:
            s_line = line.strip()
            # adds to dictionary if word is longer than 4
            if len(s_line) > 4:
                if s_line not in dct:
                    dct[s_line] = 0
                dct[s_line] += 1
        # create a sortable list from dictionary
        items = list(dct.items())
        # returns sorted list
        return sorted(items, key=lambda tpl: tpl[1])[::-1]
```
The program begins with finding my current path. it then calls the function count_occurences(code above) with the current path and the file name of the file to be read. The function works by first opening the targeted file. The code then reads each line in the text file and strips it using the strip function. It then checks if the length of the word is more than 4 and if that is the case it controls if found word is already in dictionary. If the word is not already in dictionary it creates a new key with said word with value 1. If the word found already exists in dictionary it increases its value by 1. After all lines in file have been read it creates a list of tuples with kat-value pairs. The function then returns the list sorted from highest value to lowest. After returning this list back to the main part of the program it calls for a second function, print_top10. this function works using a for loop which repeats 10 times. The function uses the length of the words to make the output look better. This prints out each of the first 10 words in the list provided. It then returns to the main part of the program where the process repeats with the new file to be read. 


the Top-10 list for life of Brian: 
1.  brian          368
2.  crowd          161
3.  centurion      121
4.  mother         104
5.  right          99
6.  crucifixion    78
7.  pilate         68
8.  pontius        64
9.  rogers         52
10. there          44

The Top-10 list for Swedish News:
1.  under          54049
2.  säger          47548
3.  efter          44094
4.  kommer         42859
5.  eller          32261
6.  också          30479
7.  sedan          30396
8.  andra          28077
9.  finns          27584
10. många          26819

## Part 2: Implementing data structures

Hash:

A Hash table is a data structure that is used to retrieve loads of data very fast. It works by calculating a value for each index number (bucket) in a given array. The value is determined by the ascii code of letters in a word. The value is then modulo by the amount of buckets inside of the array, to determine in which bucket the element should be added to in our array.   

We computed our Hash value by enumerating and using prime numbers. Our code goes the following:

```python
def get_hash(self, word):
    hash_val = 0
    # takes each character in word and also enumerates by 1
    for i, char in enumerate(word):
        # add the ascci value + a hash maker to current hash value
        # using prime numbers to decrease amount of zero buckets
        hash_val += ord(char) % 999959 * 27 ** i
    bucket = hash_val % self.bucket_list_size()
    return bucket
```
The reason behind using modulo on a prime number is because it reduces the amount of zero buckets. We found out throughout testing that using a large prime number will give us the lowest amount of zero buckets, hence the number 999959. The lower the zero buckets we have the faster hash table. To further reduce the zero buckets we make use of a linear search. The linear search works by checking if the bucket found is empty or not. If it's empty it adds our element into the bucket, if it's not empty it gets a new bucket by moving 2 buckets to the right. At last we use modulo on the value by the amount of buckets in our array, for it to stay inside the index range. 

The rehashing functions gets called when the number of elements is the same as the amount of buckets. It saves and makes a copy of all the old buckets and thereafter creates a new empty list with buckets but doubling the amount. The function then takes each element in copied buckets and adds them to the new bucket list using the add function.

Add is the function that adds the elements to the buckets in the ways explained above. Our Def add looks like this:
```python
# Adds a word to set if not already added
def add(self, word):
    # if time to rehash call the rehash function
    if self.size >= self.bucket_list_size():
        self.rehash()
    # if it doesnt already contain word add it to bucket
    if not self.contains(word):
        # calculate bucket using get_hash and bucket list size
        bucket = self.get_hash(word)
        # check if a linear search can move it to a empty bucket
        n_bucket = self.linear_s(bucket, word)
        # add it to bucket and increase size
        self.buckets[n_bucket].append(word)
        self.size += 1
```

This function works by first checking if it is time to rehash. If that is the case it first calls the rehash function before continuing to add the provided word.
It then checks if the hash table already consist of inputted word by calling for the contain function which returns true if word already exists. In that case it just skips the function. If the words doesnt exist it finds it correct bucket using the get_hash function and the linears_s function. When a bucket has been found it appends that word to found bucket and increases the size by 1.

The way our results differ from the hash_output is that we get a different order in the to-string function. This is because it depends on what hash function you use. Different hash functiouns put words in different buckets hence the order changes. The value of max bucket is different too, but it is also because of the get_hash function being different and the words landing in each bucket differentiate. The zero bucket ration in our program is the same but this is just a coincidence as it is also reliant on the get_hash function. But because there are so little amount of elements it happened to be the same.

Bst Map:

Bst stands for Binary search tree. Binary trees are a data structure that uses nodes called root, parents and children. Each node can have at most 2 children named left child or right child. The nodes are ordered in a certain manner usually by the order left children< parent< right children, and this order calls recursively across the tree.

The way we structure our tree is with a function called put. Our put function looks like following:

```python
# inputs provided key and value into tree
def put(self, key, value):
    # check side of root to put new key and value into
    if key < self.key:
        # if its an empty spot, create a new node
        if self.left is None:
            self.left = Node(key, value)
        # if not empty call for function again
        else:
            self.left.put(key, value)
    elif key > self.key:
        if self.right is None:
            self.right = Node(key, value)
        else:
            self.right.put(key, value)
    # if key already exist replace with new value
    else:
        self.key = key
        self.value = value
```

The code starts of with creating a root(which is not in this function). Thereafter it checks for which side of the root the provided key belongs to. If node on that side is "none" it creates a new node with provided key and value. if node is not empty it calls the current function recursively with that node as it's root. If the key already exists it assigns the new value provided. And it continues doing this for the entirety of both the left and the right side of the tree. 


Max depth is a function that returns the max depth of the tree. The depth length is determined by the longest root to leaf path, counted in nodes. The code for accomplishing this feat looks like this: 

```python
def max_depth(self):
    if self.left is not None and self.right is not None:
        le = self.left.max_depth()
        ri = self.right.max_depth()
        if le > ri:
            return le + 1
        else:
            return ri + 1
    if self.left is not None:
        return 1 + self.left.max_depth()
    elif self.right is not None:
        return 1 + self.right.max_depth()
    else:
        return 1
```
This code works by checking the right and the left node and compares their max depth. It starts by checking if left and right is not none. If that's the case it starts by checking the max depth of the left side by recalling the function with the current left node as its new node. Thereafter it continues calling for it function until a leaf node is found. When the leaf node is found it returns the value 1. The value 1 is then returned to previous node which compares it to its other child if it has one otherwise just return that value plus 1 up all the way til the root. So to summarize the function it takes the root and compares which child of the root has the max depth and returns that to the main program. 

Differences given in bst_main from bst_output are none because we are inputting the words in the same order. The tree will be the same hence the output wont be different. 

## Part 3: Count unique words 2

This part is very similar to task 1 but this time we will generate the 10 most used words with the help of our data structures. When solving this we started by defining two functions. One function which takes a list as input and removes all words with 4 or less letters in it. It returns a new list only consists of words longer than 4. The other function is the same as in part 1, it prints the top 10 words in a more readable way using the length of the words.
Then the main program starts with getting current path and creating a new empty map from bstmap. We then open the file and starts to reading and stripping each line in file. We also assign the value 0 to num. We then use the get function in bstmap to check if word already exists in bst. If the word does not exist use the put function to put the new word in with value 1. If the word already existed in bst we get the current value of that word using the get function. We then input that word with same key and the value being 1 plus the umber retrieved from word as key. This updates the value of the key by 1. The start of the main program is shown in the code below.
```python
with open(path + "/data/brian_13391_words.txt", "r") as file:
    for lines in file:
        num = 0
        line = lines.strip()
        # if word from file doesnt exist in tree create new node with value 1
        if map.get(line) is None:
            map.put(line, 1)
        # if word exist retreive its value and add 1, then return with new value
        else:
            num = map.get(line)
            map.put(line, num + 1)
```
After this we created a new empty list and using as_list function added the key, value pairs created to the list. Then using sort we sorted the list from highest value to lowest. The function remove_u4 is then called for which removes all key, value pairs with a key shorter than 4. This returns a new list which is sliced so only the top 10 words are left in the list. Then using the top 10 function the program prints the top 10 list. After that using the bstmap functions size, max_depth and count_leafs those values are printed. When all results for life of brian are printed we start again by creating a new map for swe_news and the whole main part is repeated with a new file. 

Results from unique words for both files using a hashtable:

### Life of brian results:

Unique words:

2034

zero bucket ratio:

0.2563

max bucket size:

5

bucket list size

2048

### Swe news results:

Unique words:

387407

zero bucket ratio:

0.3833

max bucket size:

7

bucket list size

524288

The value for max bucket size and zero bucket ratio can be used to evaluate the quality of a hash function in HashSet. The ultimate goal is to get the smallest number possible. For life of Brian the most reasonable max bucket size would be 2-3 and the zero bucket ratio somewhere in the 30-40%. Swedish news is a larger text file thus a higher value is more reasonable. In our case we got the max bucket to 7 and the zero bucket ratio to 0.3833 A poor value would be higher numbers than previously discussed as it would be a inefficient data structure, meaning it would be slow to compute the results. 

Results for top 10 for both files using bst:
### Top 10 words in life of brian:
1.  brian          368
2.  crowd          161
3.  centurion      121
4.  mother         104
5.  right          100
6.  crucifixion    78
7.  pilate         68
8.  pontius        64
9.  rogers         52
10. there          44

Number of tree nodes: 2034

Max depth: 27

Number of leaf nodes: 656

### Top 10 words in swedish news:
1.  under          54049
2.  säger          47548
3.  efter          44094
4.  kommer         42859
5.  eller          32261
6.  också          30479
7.  sedan          30396
8.  andra          28077
9.  finns          27584
10. många          26819

Number of tree nodes: 387407

Max depth: 120

Number of leaf nodes: 127713

The way you determine the quality of a binary tree is by its max depth and leaf count. The lower the value of max depth and the higher the amount of leaf nodes the better quality of a binary tree. In our case Life of Brian gave us a max depth value of 27 with 656 number of leaf nodes. For Swedish news we got a max depth value of 120 with 127713 number of leaf nodes. These number are reasonable since it´s a very big file and thus the expected results are quite large. A poor value would be to have a max depth of a few hundred since this would imply a very deep tree. A deep tree gives a long computing time.
## Project conclusions and lessons learned

### Technical issues 

We also spent a lot of time before understanding the recursive function calls needed in bstmap. Due to this it took some time creating the first few functions but after coming more into how it actually works the rest of the functions went smoothly to write. The group had some challenges with getting a good get_hash function to reach a low zero bucket ratio which we spent some time trying to improve. We think the way we handled the writing of the code was very good because we focused on one thing at a time and firstly tried to understand what we were working on. Like first we read up on what a binary search tree is and how it works not just directly starting to write functions. Then we just tried different ways of approaching functions until realising how it should be done. This resulted in a slower start but made us increase in speed the further we came into the project. 
If we would have had a little more time on the project we could have made the top 10 word using bst function work a little bit quicker by improving our bst map. We also could have reduced the zero bucket ratio even more. 

### Project issues

We used a repository in gitlab to work in the same code which proved to come with some challenges. This was due to conflicts and some things appearing even though we couldnt find any but this was figured out after some time.
The team used an app called discord to communicate and organize the work. The app allowed us to easily get a hold of each other if a problem occurred and helped us with scheduling meetings. The team mainly focused on getting the coding part done in school as a group but due to one of the members having to commute to school a lot of coding was done at home. Working as a group at home didn't prove to be any problem since discord allows voice calls with screenshares. Communication happened frequently both in school and online, often talking about how the different task could be tackled. 

Jesper Wingren,

Part 1 I worked on because it didn´t take so long to create and was fairly simple. Then on part 2 we did most of our work together but I focused more on the bst while Liam focused more on the hash to begin with. As we both had an understanding of both dataclasses we could discuss with each other and help each other as for example i helped with the get hash function because he got stuck. We explained the functions for each other as we created them so we could understand all the functions in both dataclasses. This was done in combination when writing the report as we tried to combine writing the report with understanding the different dataclasses. Part 3 I wrote the unique words quick because it was pretty much the sam as in part 1 but the top 10 word we worked together to finish to project. We wrote maybe half the report each and I spent maybe 15 to 20 hours each week working on the project.

Minh Anh Pham,

All of our work was done as a team but with each member taking a special responsability for certain parts of the project. Task one was mostly done by Jesper since he had a good idea of how to handle the given problem. Task two was a bit more difficult so we decided to specialize in different areas of the problem. My job was to specialize in Hash while Jesper choose to take care of the binary tree. After learning our different data structures we taught them to each other and proceeded with the coding. While the binary tree went well I struggled with finding a good Hash value with a low bucket ratio. But with the help of Jesper we eventually found an acceptable bucket ratio. The third task was done much as a team and didn't prove to be much of a problem. The estimated time spent each week was around 15 hours.

As a group,

We have now understood more about data structures especially hash and binary trees. The project gave us a better idea on what it's like to work as a duo in coding, with the help of gitlab. We felt like much of the work was done well with a good amount of teamwork. The only thing we would like to improve more on the future is that we had more meetings in place rather than online or communicate more frequently when writing. Because it created some conflicts which we had to spend unnecessary time figuring out. We definitely should communicate more frequently and communicating in a way where you avoid collisions.
