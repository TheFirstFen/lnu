from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List[str]] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for _ in range(8)]

    # Computes hash value for a word (a string)
    '''
    https://stackoverflow.com/questions/2624192/good-hash-function-for-strings

    Uses prime numbers to get as different hash values as possible.
    Has A starting hash_value of 7 and for every character in the
    given word change the hash_value to the value current hash_value
    times 31(another prime number) + the ord() value of current character.
    '''
    def get_hash(self, word: str) -> int:
        hash_value = 7
        for character in word:
            hash_value = hash_value * 31 + ord(character)
        return hash_value % len(self.buckets)

    # Doubles size of bucket list
    '''
    Set current bucket list to a temporary variable then generates a
    new bucket list for twice it current size and resets size to 0
    then for each "bucket" in the temporary variable add it to the
    new bucket list
    '''
    def rehash(self) -> None:
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(len(self.buckets) * 2)]
        self.size = 0

        for bucket in old_buckets:
            for element in bucket:
                self.add(element)

    # Adds a word to set if not already added
    '''
    First checks if we should rehash and then checks if current given word
    exists, if not then we get the hash value of the word and place it in
    that numbered bucket and increment size by 1, if word exists do nothing
    '''
    def add(self, word: str) -> None:
        if self.size > len(self.buckets):
            self.rehash()

        if not self.contains(word):
            self.buckets[self.get_hash(word)].append(word)
            self.size += 1

    # Returns a string representation of the set content
    def to_string(self) -> str:
        return "{ " + " ".join(sum(self.buckets, [])) + " }"

    # Returns current number of elements in set
    def get_size(self) -> int:
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word: str) -> bool:
        if word in self.buckets[self.get_hash(word)]:
            return True
        return False

    # Returns current size of bucket list
    def bucket_list_size(self) -> int:
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word: str) -> None:
        if self.contains(word):
            self.buckets[self.get_hash(word)].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self) -> int:
        max_elements = 0
        for bucket in self.buckets:
            if max_elements < len(bucket):
                max_elements = len(bucket)

        return max_elements

    # Returns the ratio of buckets of length zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self) -> float:
        zero_buckets = 0
        for bucket in self.buckets:
            if len(bucket) == 0:
                zero_buckets += 1

        return zero_buckets / self.bucket_list_size()
