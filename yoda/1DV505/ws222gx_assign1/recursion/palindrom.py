def is_palindrome(s, first, last):
    if first >= last:
        return True

    if s[first] == s[last]:
        first += 1
        last -= 1
        return is_palindrome(s, first, last)
    return False


def check_palindrome(s):
    if s == "":
        return True
    elif len(s) == 1:
        return True

    first, last = 0, len(s)-1
    return is_palindrome(s, first, last)


true_cases = ["x", "annna", "madam", "abcdefedcba", "yyyyyyyyy"]    # True case
false_cases = ["programming", "university", "microbiology",
               "counterproductive", "exaggeration"]


for i in true_cases:
    result = check_palindrome(i)
    print(result)

for j in false_cases:
    result = check_palindrome(j)
    print(result)
