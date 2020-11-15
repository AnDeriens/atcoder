h, w, n, m = list(map(int, input().split()))

denkyu = [()] * n

chizu = [['.' for _ in range(w)] for _ in range(h)] 
ans_chizu = [['.' for _ in range(w)] for _ in range(h)] 

for i in range(n):
    x, y = list(map(int, input().split()))
    denkyu[i] = (x, y)

for _ in range(m):
    x, y = list(map(int, input().split()))
    chizu[1][1] = '|'

for (a, b) in denkyu:
    a -= 1
    b -= 1
    for x in range(a, -1, -1):
        if chizu[b][x] == '.':
            ans_chizu[b][x] = '*'
        elif chizu[b][x] == '|':
            break
    for x in range(a, w):
        if chizu[b][x] == '.':
            ans_chizu[b][x] = '*'
        elif chizu[b][x] == '|':
            break
    for y in range(b, -1, -1):
        if chizu[y][a] == '.':
            ans_chizu[y][a] = '*'
        elif chizu[y][a] == '|':
            break
    for y in range(y, h):
        if chizu[y][a] == '.':
            ans_chizu[y][a] = '*'
        elif chizu[y][a] == '|':
            break

ans = 0

for x in range(w):
    for y in range(h):
        if ans_chizu[y][x] == '*':
            ans += 1

print(ans)
