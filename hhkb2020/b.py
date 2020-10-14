h, w = list(map(int, input().split()))

cnt = 0

space = [['' for _ in range(w + 2)] for _ in range(h + 2)] 

for _h in range(h):
    s = input()
    space[_h + 1] = [''] +  list(s) + ['']


for i in range(1, h + 1):
    for j in range(1, w + 1):
        current = space[i][j]
        if current == '#':
            continue

        if space[i + 1][j] == '.':
            cnt += 1
        if space[i][j + 1] == '.':
            cnt += 1

print(cnt)
