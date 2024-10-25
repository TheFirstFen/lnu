#  calculating abcd and dcba (same but backwards)
def get_number(a, b, c, d):
    abcd = a*1000 + b*100 + c*10 + d
    dcba = d*1000 + c*100 + b*10 + a
    return abcd, dcba


#  Testing for every single value of a, b, c and d

for a in range(1, 10):
    for b in range(1, 11):
        for c in range(1, 11):
            for d in range(1, 10):
                abcd, dcba = get_number(a, b, c, d)
                if (dcba/abcd == 4):
                    solution = a, b, c, d

print("The four different digits A, B, C, D such that the number DCBA is 4 "
      "times greater than ABCD is", solution)
