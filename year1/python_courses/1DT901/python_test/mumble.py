def mumbler(text):
    new_str = ''
    for i in range(len(text)):
        if i % 2 != 0:
            new_str += '@'
        else:
            new_str += text[i]
    return new_str


# Demo Code
original_str = 'The Dark Side of the Moon'
print('Original text:')
print(original_str)
print('After call to function:')
print(mumbler(original_str))
