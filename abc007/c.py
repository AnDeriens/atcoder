import queue

dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

field = []

# フィールド情報を取得
for _ in range(r):
    _s = input()
    field.append(_s)

# 訪れたフラグを保持
visited = [[False] * c for _ in range(r)]

# queを初期化
# 次に訪れる座標をqueにいれていく
q = queue.Queue()
q.put((sx - 1, sy - 1, 0))

ans = 0
while not q.empty():
    x, y, d = q.get()

    if x == gx - 1 and y == gy - 1:
        ans = d
        break

    if visited[y][x]:
        continue

    visited[y][x] = True
    for dx, dy in dxdy: 
        if 0 <= x + dx < c and 0 <= y + dy < r:
            if visited[y + dy][x + dx] == False and field[y + dy][x + dx] == '.':
                q.put((x + dx, y + dy, d + 1))


print(ans)
