def two_pointer(lst, target):
    unique_pairs = set()
    lst = sorted(lst)  # Two-pointer requires a sorted list

    for fP in range(len(lst) - 2):  # Use `-2` for the three-pointer approach
        if fP > 0 and lst[fP] == lst[fP - 1]:  # Skip duplicate values for the fixed pointer
            continue

        left_p = fP + 1
        right_p = len(lst) - 1

        while left_p < right_p:
            summa = lst[fP] + lst[left_p] + lst[right_p] - target
            if summa == 0:
                unique_pairs.add((lst[fP], lst[left_p], lst[right_p]))

                # move side to side to avoid left pointer and right pointer to be dups
                while left_p < right_p and lst[left_p] == lst[left_p + 1]:
                    left_p += 1
                while left_p < right_p and lst[right_p] == lst[right_p - 1]:
                    right_p -= 1

                # increase the pointers for the sequence
                left_p += 1
                right_p -= 1
            elif summa < 0:
                left_p += 1
            else:
                right_p -= 1

    return unique_pairs


