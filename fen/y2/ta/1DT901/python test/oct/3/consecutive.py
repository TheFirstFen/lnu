def get_consecutive(s):
    if len(s) > 1:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return s[i]
    return None


print(get_consecutive("aabcdd"))
