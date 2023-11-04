# read input
i = input('Provide salaries: ')
sal = i.split()
ints = [int(s) for s in sal]


# formulate and coumputing results
def median(ints):
    ints.sort()
    length = len(ints)
    if length % 2 != 0:
        i = length // 2
        med = ints[i]
    else:
        i1 = length // 2
        i2 = i1 + 1
        med = (ints[i1] + ints[i2]) / 2
    return med


def average(ints):
    s = sum(ints)
    length2 = len(ints)
    ave = round(s/length2)
    return ave


def gap(ints):
    g = max(ints) - min(ints)
    return g


# result
print('Median: ', median(ints))
print('Average: ', average(ints))
print('Gap: ', gap(ints))
