from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
    #   return(hash(word))
    #   hashsum += ((current character position) + length of word) ** ascii value for current character
        hashsum = 0
        for idx, c in enumerate(word):
            hashsum += (idx + len(word)) ** ord(c)
        return hashsum
    
       

    # Doubles size of bucket list
    def rehash(self):
        """ Lecture notes """
        bucketListSize = self.bucket_list_size()
        copyBuckets = [[] for i in range(bucketListSize)]
        # copy buckets to copyBuckets
        for i in range(bucketListSize):
            copyBuckets[i] = self.buckets[i]
        # clean buckets
        for i in range(bucketListSize):
            self.buckets[i] = []
        # dubble buckets
        self.buckets = [[] for i in range(bucketListSize*2)]
        self.size = 0
        # add copyBuckets to buckets
        for i in range(len(copyBuckets)):
            #self.add(''.join(copyBuckets[i]))
            self.add(copyBuckets[i])
            

    # Adds a word to set if not already added
    def add(self, word):
        """ Lecture notes. Collisions and Open address and linear probing """
        """ https://en.wikipedia.org/wiki/Hash_table """
        """ https://runestone.academy/ns/books/published/pythonds/SortSearch/Hashing.html"""
        hashValue = self.get_hash(word)
        buckets = self.bucket_list_size()
        element = hashValue % buckets
        #print(f"hash: {hashValue} element: {element} word: {word}")
        #print(self.buckets)
        found = True
        while self.buckets[element] != [] and found:
            if self.buckets[element] == word:
                found = False
            element = element + 1
            element = element % buckets
        if found:
            self.buckets[element] = word
            self.size = self.size + 1
        #print(self.buckets)
        if self.size == self.bucket_list_size():
            self.rehash()
            #print(f"rehash: {self.size}")
        return

    # Returns a string representation of the set content
    def to_string(self):
        """ Lecture notes """
        str = "{ "
        buckets = self.bucket_list_size()
        for i in range(buckets):
            str = str + " " + ''.join(self.buckets[i])
        str = str + " }"
        return (str)
        

    # Returns current number of elements in set
    def get_size(self):
        return (self.size)


    # Returns True if word in set, otherwise False
    def contains(self, word):
        buckets = self.bucket_list_size()
        hashValue = self.get_hash(word)
        element = hashValue % buckets
        found = False
        while self.buckets[element] != [] and not found:
            if self.buckets[element] == word:
                found = True
            else:
                element = element + 1
                element = element % buckets
        return (found)
            
          
    # Returns current size of bucket list
    def bucket_list_size(self):
        return (len(self.buckets))


    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        buckets = self.bucket_list_size()
        hashValue = self.get_hash(word)
        element = hashValue % buckets
        found = False
        while self.buckets[element] != [] and not found:
            if self.buckets[element] == word:
                found = True
            else:
                element = element + 1
                element = element % buckets
        if found:
            self.buckets[element] = []
            self.size = self.size - 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        buckets = self.bucket_list_size()
        maxsize = 0
        for i in range(buckets):
            if len(self.buckets[i]) > maxsize:
                maxsize = len(self.buckets[i])
        return (maxsize)

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        buckets = self.bucket_list_size()
        zeroBuckets = 0
        for i in range(buckets):
            if self.buckets[i] == []:
                zeroBuckets = zeroBuckets + 1

        return (float((buckets - zeroBuckets) / buckets))

