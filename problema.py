with open('c:/Users/smalk/Desktop/input.txt', 'r') as f:
    m = [[int(num) for num in rand.split(' ')] for rand in f]
linii = len(m)
corn1 = 0
for i in range(0, linii):
    for j in range(0, linii):
        if m[i][j] == m[0][0]:
            corn1 += 1
corn2 = 0
for i in range(0, linii):
    for j in range(0, linii):
        if m[i][j] == m[0][linii-1]:
            corn2 += 1
corn3 = 0
for i in range(0, linii):
    for j in range(0, linii):
        if m[i][j] == m[linii-1][0]:
            corn3 += 1
corn4 = 0
for i in range(0, linii):
    for j in range(0, linii):
        if m[i][j] == m[linii-1][linii-1]:
            corn4 += 1
print(corn1, corn2, corn3, corn4)