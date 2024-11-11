s = input("String to check if palindrome? ")
low_s = s.lower()


def reverse(x):
    rev = ""
    for char in x:
        rev = char + rev
    return rev


def is_palindrome(x):
    st = ""
    for char in x:
        if 97 <= ord(char) <= 122:
            st = st + char
    rev_s = reverse(st)
    if st == rev_s:
        return True
    else:
        return False


if is_palindrome(low_s):
    print(f'Yes "{s}" is a palindrome')
else:
    print(f'No "{s}" is not a palindrome')
