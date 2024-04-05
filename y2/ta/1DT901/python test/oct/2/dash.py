def add_dash(s):
    if s == "":
        return ""
    else:
        ret = "-"
        for c in s:
            ret += c + "-"
        return ret


# Main program starts
strings = ["Jonas", "n", ""]
for s in strings:
    print(s, "==>", add_dash(s))
