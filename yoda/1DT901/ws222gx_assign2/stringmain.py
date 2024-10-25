import string_functions

result_concat = string_functions.concat("abc", 3)
print(f"concat('abc', 3) = {result_concat}")

result_concat = string_functions.concat("hej", 1)
print(f"concat('hej', 1) = {result_concat}")

# Testfall för count
result_count = string_functions.count("hello", "l")
print(f"count('hello', 'l') = {result_count}")

result_count = string_functions.count("programming", "g")
print(f"count('programming', 'g') = {result_count}")

result_count = string_functions.count("banana", "x")
print(f"count('banana', 'x') = {result_count}")

# Testfall för reverse
result_reverse = string_functions.reverse("hello")
print(f"reverse('hello') = {result_reverse}")

result_reverse = string_functions.reverse("python")
print(f"reverse('python') = {result_reverse}")


# Testfall för first_last
result_first_last = string_functions.first_last("abc")
print(f"first_last('abc') = {result_first_last}")

result_first_last = string_functions.first_last("12345")
print(f"first_last('12345') = {result_first_last}")

result_has_two_X = string_functions.has_two_X("XOXOX")
print(f"has_two_X('XOXOX') = {result_has_two_X}")

result_has_two_X = string_functions.has_two_X("XOXOXO")
print(f"has_two_X('XOXOXO') = {result_has_two_X}")

# Testfall för has_duplicates
result_has_duplicates = string_functions.has_duplicates("hello")
print(f"has_duplicates('hello') = {result_has_duplicates}")

result_has_duplicates = string_functions.has_duplicates("abcde")
print(f"has_duplicates('abcde') = {result_has_duplicates}")
