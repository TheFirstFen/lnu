from hash import init_hash
import string
import random
import matplotlib.pyplot as plt


new_hash = init_hash

number_of_repeats = 10000

# Test Uniformity
list_of_buckets = [0] * 256
for i in range(number_of_repeats):
    random_word = "".join(random.choice(string.ascii_lowercase) for i in range(random.randint(20,40)))
    list_of_buckets[new_hash.hash(random_word)] += 1

plt.subplot(1, 2, 1)
plt.bar(range(len(list_of_buckets)), list_of_buckets, color="Blue")
plt.title("Uniformity buckets, "+ str(number_of_repeats)+ " iterations")
plt.xlabel("Bucket")
plt.ylabel("Bucket size")


print("string: aaaa as hash, " + str(new_hash.hash("aaaa")))
print("string: aaab as hash, " + str(new_hash.hash("aaab")))


# Test Small changes
other_list_of_buckets = [0] * 256
new_string = "aaaaa"
string_list = list(new_string)
print(new_hash.hash(new_string))
for i in range(1000):
    start_hash = new_hash.hash(new_string)
    random_letter = "".join(random.choice(string.ascii_lowercase))
    string_list[random.randint(0, len(string_list) - 1)] = random_letter
    other_list_of_buckets[abs(start_hash-new_hash.hash("".join(string_list)))] += 1
    end_hash = new_hash.hash("".join(string_list))
plt.subplot(1, 2, 2)
plt.bar(range(len(other_list_of_buckets)), other_list_of_buckets, color="Red")
plt.title("Small changes in a string, "+ str(1000)+ " iterations")
plt.xlabel("Change in hash value")
plt.ylabel("Number of string with a certain change in hash value")
plt.show()



