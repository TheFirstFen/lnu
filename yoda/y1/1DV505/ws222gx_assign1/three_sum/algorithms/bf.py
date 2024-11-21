def brute_force(lst, target):
    unique_pairs = set()

    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                v1, v2, v3 = lst[i], lst[j], lst[k]
                needed = (v1 + v2 + v3) - target
                if i == j or k == i or k == j:
                    continue
                if needed == 0:
                    unique_pairs.add((v1, v2, v3))

    return list(unique_pairs)
