def two_pointer(lst, target):
    unique_pairs = set()
    lst = sorted(lst)  # Two-pointer requires a sorted list

    # first pointer
    for fP in range(len(lst) - 2):  # Use `-2` for the three-pointer approach
        if fP > 0 and lst[fP] == lst[fP - 1]:
            continue

        left_p = fP + 1     # left to right pointer
        right_p = len(lst) - 1  # right to left pointer

        while left_p < right_p:
            needed = lst[fP] + lst[left_p] + lst[right_p] - target

            # if needed = 0 we have found 3 values for the target
            if needed == 0:
                unique_pairs.add((lst[fP], lst[left_p], lst[right_p]))

                # if left pointer and right pointer & also there is duplicates
                # increase or decrease the pointers
                while left_p < right_p and lst[left_p] == lst[left_p + 1]:
                    left_p += 1
                while left_p < right_p and lst[right_p] == lst[right_p - 1]:
                    right_p -= 1

                # take one step to the left or left
                left_p += 1
                right_p -= 1

            # when the needed is less then 0 we know we need a bigger value
            elif needed < 0:
                left_p += 1
            else:   # we need lower value
                right_p -= 1

    return unique_pairs
