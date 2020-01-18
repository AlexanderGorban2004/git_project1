n = int(input())
b = {}
w = [0, 1, 2, 3, 4, 5, 6, 7]

for t in range(n):
    a = int(input())
    if a < 8:
        if 8 - a not in b:
            b[8 - a] = [a]
        else:
            b[8 - a] = b[8 - a][0] + a
    else:
        if a % 8 not in b:
            b[a % 8] = [a]
        else:
            b[a % 8] = b[a % 8][0] + a
for t in b:
    for t1 in b:
        if t + t1 != 8:
            w.append()



