import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限

h, w = map(int, input().split())
c_h, c_w = map(int, input().split())
d_h, d_w = map(int, input().split())
s = [list(input()) for i in range(h)]

# ゴール設定
s[d_h - 1][d_w - 1] = 'g'

# stack作成
stack = [[c_w - 1, c_h - 1]]
visited = [[0 for i in range(w)] for j in range(h)]
visited[c_h - 1][c_w - 1] = 1

walk_dx_dy = [[1,0],[0,1],[-1,0],[0,-1]]

magic_dx_dy = []
for i in range(5):
    for j in range(5):
        magic_dx_dy.append([i - 2, j - 2])

cnt = 0

def dfs(visited, stack, dx_dy, s, x, y, walked):
    for i in range(len(dx_dy)):
        n_x, n_y = x + walk_dx_dy[i][0], y + walk_dx_dy[i][1]
        if 0 <= n_x < h and 0 <= n_y < w and visited[n_x][n_y] == 0 and s[n_x][n_y] != '#':
            visited[n_x][n_y] = 1
            stack.append([n_x, n_y])
            walked.append([n_x, n_y])

    return [stack, visited, walked]

def dfs(visited, stack, dx_dy, s, x, y, walked):
    for i in range(len(dx_dy)):
        n_x, n_y = x + walk_dx_dy[i][0], y + walk_dx_dy[i][1]
        if 0 <= n_x < h and 0 <= n_y < w and visited[n_x][n_y] == 0 and s[n_x][n_y] != '#':
            visited[n_x][n_y] = 1
            stack.append([n_x, n_y])
            walked.append([n_x, n_y])

    return [stack, visited, walked]



while stack:
    x, y = stack.pop()
    walked = []
    stack, visited, walked = dfs(visited, stack, walk_dx_dy, s, x, y, walked)

    if visited[d_h - 1, d_w - 1] == 1:
        print(cnt)
        exit()
    else:
        while walked:
        x, y = walked.pop()
        walked = []
        stack, visited, walked = dfs(visited, stack, magix_dx_dy, s, x, y, walked)

