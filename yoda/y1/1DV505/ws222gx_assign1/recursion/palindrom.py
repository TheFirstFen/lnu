

def check_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return check_palindrome(s[1:-1])

    return False


true_cases = ["", "x", "annna", "madam", "abcdefedcba", "yyyyyyyyy"]
false_cases = ["programming", "university", "microbiology",
               "counterproductive", "exaggeration"]


print("Expected results to be all True")
for i in true_cases:
    result = check_palindrome(i)
    print(result)

print("\nExpected results to be all False")
for j in false_cases:
    result = check_palindrome(j)
    print(result)
