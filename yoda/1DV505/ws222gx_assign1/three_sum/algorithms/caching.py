def caching(lst, target):
    unique_pairs = set()
    for i in range(len(lst) - 2):
        cash = set()    # reset it to find unique combinations
        for j in range(i+1, len(lst)):
            needed_value = (target - lst[i]) - lst[j]
            if needed_value in cash:
                unique_pairs.add((lst[i], needed_value, lst[j]))

            cash.add(lst[j])
    return unique_pairs
