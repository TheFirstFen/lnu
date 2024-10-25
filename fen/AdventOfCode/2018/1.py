import sys
D = open(sys.argv[1].read().strip()
X = []
for line in D.split('\n'):
    line = line.strip()
    X.append(int(line))
print(max(X))
