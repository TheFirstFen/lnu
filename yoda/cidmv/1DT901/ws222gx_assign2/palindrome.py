def is_palindrome(s):
    lst = [chr for chr in s.lower() if chr.isalpha()]
    return lst == lst[::-1]


print(is_palindrome("Was it a rat I saw?"))
print(is_palindrome("Was it a ra I saw?"))
print(is_palindrome("Was! it a@ car or a cat i saw.?"))
