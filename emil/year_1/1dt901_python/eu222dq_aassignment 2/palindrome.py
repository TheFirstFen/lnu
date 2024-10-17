def is_palindrome(s):
    s = s.replace(' ', '')
    if s == s[::-1]:
        return True
    else:
        return False


while True:
    str_in = input("Enter a string: ").lower()
    print(f"{str_in} {is_palindrome(str_in)}")
