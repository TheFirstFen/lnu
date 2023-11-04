# Computing and displaying
for i in range(1, 10):
    for k in range(1, 10):
        for o in range(0, 10):
            for j in range(0, 10):
                IKOJ = i*1000 + k*100 + o*10 + j
                JOKI = j*1000 + o*100 + k*10 + i
                if IKOJ * 4 == JOKI:
                    print("DCBA: ", JOKI)
