
def is_palindrome(s):
    # Remove non-letter
    clean = ""
    for c in s:
        if c.isalpha():
            clean += c.lower()

    # Compare with reverse
    return clean == clean[::-1]


# Program starts
text = "Ni talar bra latin!"
print(text,  is_palindrome(text))
