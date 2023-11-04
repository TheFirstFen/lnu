# Mini-project report

Members: Samuel Berg and Love Billenius\
Program: Software Engineering\
Course: 1DT901\
Date of submission: 2022-11-05

## Introduction

In this project we where first supposed to be using builtin functions to count the amount of unique words in a textfile, and also get the top ten most occurring words that were 5 characters or longer in length. For the second part of the project we were supposed to create two different data structures. One of them was a binary search tree, and the other was a hash set. Both of them came with code skeletons which contained functions needed to implement. There was also some test programs included that we got to use to check if our code was valid. The third and final part was implementing the data structures we created in part two to do the same thing we did in part one not using the builtin functions `set` and `dict`. And get the same result as we did in part one.

## Part 1: Count unique words 1

  The `life_of_brian` text file had 13 219 words and `swedish_news` text file had 14 053 824 words in them.

  For the top ten function we used a dictionary and a list of all words. For each new word, we added an entry with the value one, and for each existing we incremented the existing value with one.

  ```python
  for item in lst:
      items[item] = items.get(item, 0) + 1
  ```

  Afterwards we sorted the dictionary after the values, and reversed the sorted dictionary to then return the first ten elements after having it sorted.

  ||life_of_brian|swedish_news_2020|
  |:--------------:|:---------:|:----:|
  |**Unique words**|1997|380018|
  |**Nr 1 word**|Brian: 368|Säger: 47514|
  |**Nr 2 word**|Crowd: 161|Under: 45096|
  |**Nr 3 word**|Centurion: 121|Kommer: 42347|
  |**Nr 4 word**|Mother: 104|Efter: 36591|
  |**Nr 5 word**|Right: 100|Eller: 30716|
  |**Nr 6 word**|Crucifixion: 78|Också: 30113|
  |**Nr 7 word**|Pilate: 68|Andra: 27189|
  |**Nr 8 word**|Pontius: 64|Finns: 27046|
  |**Nr 9 word**|Rogers: 52|Sedan: 24918|
  |**Nr 10 word**|There: 44|Skulle: 23550|

## Part 2: Implementing data structures

  The given requirements for this part was that we would construct a hashset and a binary search tree in python, without using any of the already included sets and maps in python. We were not allowed to modify some parts of code skeletons given, which in turn meant that all functions in BstMap were needed to implement recursively.

  ```python
  def add(self, word: str) -> None:
      if self.size > len(self.buckets):
          self.rehash()

      if not self.contains(word):
          self.buckets[self.get_hash(word)].append(word)
          self.size += 1
  ```

  We add entries to the hash set by first checking whether we would need to do a rehash or not. If it would be needed, then we would first run a rehash, Afterwards the process would be the same as if a rehash wouldn't be necessary. A hash would be taken of the entry, normalized to the amount of buckets, and then added to the bucket corresponding to the hash, and afterwards increment the size by one.

  We compute our hash value by starting on a prime number which in this case is `hash_value = 7`. For every character in a given word we take the current value of  `hash_value` and multiply it by *31*, add the ASCII/Unicode value of the current character and set the variable to this computation. This will then be repeated for every character in a given iterable. After the entire words hash value has been computed it is divided by the current total amount of buckets and the remainder value that is then given is the bucket we allocate the word to. We got inspiration from this <https://stackoverflow.com/questions/2624192/good-hash-function-for-strings>.

  We compute the rehashing by taking all the current buckets and assigning them to an local variable and then generating a new "list" of buckets with dubble the amount of buckets. Then setting the size of that "list" equal to zero and then adding back all of the values assigned to the local variable to the new "list" one by one.

  The example output differs from out output in `hash_main.py`, which occurs due
  to us using a more efficient hashing algorithm.

  ```python
  def put(self, key: Any, value: Any) -> None:
      if self.key == key:
          self.value = value
      elif key < self.key:
          if self.left is None:
              self.left = Node(key, value, None, None)
          else:
              self.left.put(key, value)
      else:
          if self.right is None:
              self.right = Node(key, value, None, None)
          else:
              self.right.put(key, value)

  def max_depth(self) -> int:
      left, right = 0, 0

      if self.left is not None:
          left = self.left.max_depth()
      if self.right is not None:
          right = self.right.max_depth()
          
      return max(right, left) + 1
  ```
  
  For `put` we check if the key is equal to this nodes key, if that is true then we set this nodes value to the value passed in. if the key is less than this nodes key, then we check if the node left of this node is None. If it is, then we create a new node that we put left of this node. If there however is a node left of this node, then we call that nodes put method with the same values that we got. We then do the same but for right.

  To compute the `max_depth` we first create a left and right variable, then we first check the lest node for the root if the left node is not none then we call this function recursively for the left node and the result of that call will be equal to the `left` variable create in the start of the function. If the left node is none then we check the right node if it is not none then we put the `right` variable equal to the recursive call of this function for the right node. When both the left and right node of current node is equal to none then we return the greater of `left` & `right` + 1.

  There isn't any differences in the results given in `bst_main.py`

## Part 3: Count unique words 2

  ||life_of_brian|swedish_news_2020|
  |:--------------:|:---------:|:----:|
  |**Unique words**|1997|380018|
  |**Nr 1 word**|Brian: 368|Säger: 47514|
  |**Nr 2 word**|Crowd: 161|Under: 45096|
  |**Nr 3 word**|Centurion: 121|Kommer: 42347|
  |**Nr 4 word**|Mother: 104|Efter: 36591|
  |**Nr 5 word**|Right: 100|Eller: 30716|
  |**Nr 6 word**|Crucifixion: 78|Också: 30113|
  |**Nr 7 word**|Pilate: 68|Andra: 27189|
  |**Nr 8 word**|Pontius: 64|Finns: 27046|
  |**Nr 9 word**|Rogers: 52|Sedan: 24918|
  |**Nr 10 word**|There: 44|Skulle: 23550|

  ```python
  items = bst.BstMap()
      for item in lst:
          a = items.get(item)
          if a is None:
              a = 0
          items.put(item, a + 1)
  ```

  To get the top ten most occurring words we iterated through all words (including duplicates) which were longer than 4 in length. We then checked if the word was a key in our bst map. If it was then we took the value and incremented it with one. If it wasn't then we inserted the word with a value of one. Afterwards we used the bst maps .as_list() which in turn gave a list of tuples of the bst map. We then sorted that list based on the value (which were a count of how many time the key had occurred), took the reverse of that, and returned the first ten tuples. The code used to count words is inserted above.
  
  Max bucket size is the total amount of entries that end up with the same hash. They are the elements put in the same bucket, and is computed by calculating the length of all buckets, and then returning the largest one.
  
  Zero bucket ratio is the total amount buckets that are empty, divided by the total amount of buckets. This turns out to be the percentile of empty buckets to non-empty ones.

  Max depth is the deepest point of the tree. Which is the point that has the most amount of branches between itself and the root.

  Leaf count is the amount of ending points of the tree, the ones without any branches from themselves with the only branch attached to them is from the point in the previous "level" of the tree.

  ||life_of_brian|swedish_news_2020|
  |:--------------:|:---------:|:----:|
  |**Max bucket size**|8|7|
  |**Zero bucket ratio**|0.37646484375|0.4847869873046875|
  |**Max depth**|23|44|
  |**Leaf count**|469|121283|

  The HashSet have a list containing multiple "buckets", which in turn are lists. When a hash is calculated of a word, then the hash is normalized to the amount of buckets in the HashSet. The number that is calculated is the bucket where the entry is put. In an optimal world all entries would be in separate buckets, but since there isn't any perfect hashing-function, then some entries are bound to have the same hash, and since there isn't infinite amount of buckets, a normalization will have to happen, which in turn assures that even more entries will end up at the same bucket. The zero bucket ratio is the ratio of empty to non-empty buckets, and the max bucket size is how many elements the largest bucket have. In a true utopia the values for those would be 0% and 1 respectively. In our more disappointing reality this will end up at around ~50% and around half of the elements respectively. Really bad values would be ~95% for zero bucket ratio and for max bucket size next to all elements.

  Max depth of the tree can be used to know how balanced the tree is on each side of the head/root node. For a tree which contains 367 348 elements the optimal max depth would be 19. A reasonable max depth for the same tree would be around 40, and a poor max depth would be upwards of 80+ in max depth. The optimal value is the output of `log2(x)` rounded to closest integer where `x` is the total amount of nodes in the tree.

  Leaf count can be used in the same way as max depth, which is to determine how balanced the tree actually is. If we take the same tree as mentioned in max depth the optimal leaf count would be 183 674 leafs in the tree. A reasonable amount of leafs for that same tree would probably be about 120 000 to 130 000 leafs, with a poor value being at about 90 000 to 100 000 or less. The optimal amount of leafs are computed by `(2^(n-1) - 2^(n-2)) + ((x - 2^(n-1))/2)` where `n` is the max depth of the tree and `x` is the total amount of nodes in the tree.

## Project conclusions and lessons learned

  The project have been great for becoming comfortable in python as a whole. Apart from that, we both have learnt how these data structures work, thorough building them.

### Technical issues

  The hardest was not to the language or programming grammars. We both have experiences programming in object oriented languages before, so there wasn't anything odd about that. The hardest thing was instead to figure out how to think about the problem. None of us had for instance written neither a hashset, nor a binary search tree before. Once that was figured out, then it was smooth sailing.

  To be completely honest. Both me and my parter are fairly skilled in programming. We have learnt how these data structures work, and are now more confident in python. However we have not learnt any new concepts or anything like
  that.

  We finished the project long before the deadline. There isn't anything that we can think of that would improve the project. I am certain that something could be improved, but not anything that comes to mind.

### Project issues

  Both me and my partner just worked when we wanted to. We communicated daily on what we had done, and how we did it. We also worked together during lab sessions.

#### Love

  The work division came rather naturally, we both wrote code when we wanted to and told the other part of what we had done. In the end I did a bit more on part one because I was exited to code when the project was released. Then we both did a lot on part two during laboration sessions, and in the end Samuel ended up writing a bit more than me on that part.

  In average I would estimate that I spent around 4 to 5 hours a week on the project, including lab sessions.

  I really cannot think of anything that I would have done differently. I like that we worked when we felt like working, and it was challening in a good and fun way to solve the tasks before the presentations dropped. I was thinking of doing the project myself in the beginning, but I am glad that I worked on this with Samuel, since we both have a "passion" for programming, and it have been rather nice to have someone to solve the problems with. The main lessons learnt would be how a Hashet and Binary Search Tree work, recursion, git, and perhaps python in general.

#### Samuel

  We did not really divide the project up in between us we just did what we felt like when we felt like it and merged it all together nicely by the end.
  Part wise I would say part one was more Love and part two was more my doing. Part three was a joint effort in doing and the report we have either done together at lab sessions or divided it up in equal bits and pieces.

  I would estimate that I spent about 4 hours a week including lab sessions.

  I can not really think of anything that we could have done differently really, the main reason for this would be that we both know that the other person had previous knowledge in programming and there for could rely on the other person to put in the required work needed to complete the project on time. I think I have gotten more knowledgeable in python and gotten a bit more used to git especially through the command line. This was also a fun thins to do as to finishing up this course and in general a great learning experience.
