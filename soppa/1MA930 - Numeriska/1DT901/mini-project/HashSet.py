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
        hash_val = 0
        # takes each character in word and also enumerates by 1
        for i, char in enumerate(word):
            # add the ascci value + a hash maker to current hash value
            # using prime numbers to decrease amount of zero buckets
            hash_val += ord(char) % 999959 * 27 ** i
        bucket = hash_val % self.bucket_list_size()
        return bucket

    # compute a linear search for empty bucket to minimize zero bucket ratio
    def linear_s(self, bucket, word):
        for str in self.buckets[bucket]:
            # if word already exists dont change bucket
            if str == word:
                return bucket
        # if bucket is empty dont change bucket
        if len(self.buckets[bucket]) == 0:
            return bucket
        # if the bucket is not empty get a new bucket
        else:
            # if bucket was empty add 2 to the bucket
            n_bucket = bucket + 2
            # modulo it by amount of buckets to stay inside index range
            ne_bucket = n_bucket % self.bucket_list_size()
            return ne_bucket

    # Doubles size of bucket list
    def rehash(self):
        # save a copy of the old buckets
        c_buckets = list(self.buckets)
        # for loop that creates a new empty list with double amount of buckets
        for i in range((self.bucket_list_size() * 2)):
            if i < self.bucket_list_size():
                self.buckets[i] = []
            else:
                self.buckets.append([])
        # changes size to 0
        self.size = 0
        # add the copied values to new buckets with new hash value
        for i in range(len(c_buckets)):
            for str in c_buckets[i]:
                self.add(str)

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

    # Returns a string representation of the set content
    def to_string(self):
        n_str = "{ "
        # check all buckets and add to n_str, separate by whitespace
        for i in range(self.bucket_list_size()):
            if self.bucket_list_size() > 0:
                for str in self.buckets[i]:
                    n_str += str + " "
        n_str += "}"
        return n_str

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        # check which bucket word should be in
        bucket = self.get_hash(word)
        n_bucket = self.linear_s(bucket, word)
        # check each word in bucket if they corresponf to provided word
        for str in self.buckets[n_bucket]:
            # if word contains return True
            if word == str:
                return True
        # if it doesnt contain word return false
        return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        count = 0
        h = self.get_hash(word)
        n_bucket = self.linear_s(h, word)
        # calculate which bucket word is in if exists
        for str in self.buckets[n_bucket]:
            # for each word in bucket checked remember its index
            count += 1
            # if word exists pop it out by taking the index remembered
            if str == word:
                self.buckets[n_bucket].pop(count - 1)
                # decrease size
                self.size -= 1

    # Returns the size of the bucket with most elements
    # always remember the highest bucket size and compares it to each new
    def max_bucket_size(self):
        temp = 0
        for i in range(self.bucket_list_size()):
            count = 0
            for str in self.buckets[i]:
                # for each string in bucket add 1 to count
                count += 1
            # when finished counting compare to previous max bucket
            if count > temp:
                # if its larger store that new value in temp
                temp = count
        # returns the largest bucket size
        return temp

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        zero_b = 0
        # checks all buckets and adds 1 to zero_b if its an empty bucket
        for i in range(self.bucket_list_size()):
            if self.buckets[i] == []:
                zero_b += 1
        # when all zero- buckets have been checked divide by amount of buckets
        z_b_r = zero_b / self.bucket_list_size()
        # returns the rounded zero bucket ratio
        return round(z_b_r, 4)
