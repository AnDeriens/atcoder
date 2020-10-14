n, m = list(map(int, input().split()))

num = [-1] * (n + 1)

for i in range(m):
    s, c = list(map(int, input().split()))

    if num[s] != -1 and c != num[s]:
        print(-1)
        exit()

    if s == 1 and c == 0:
        print(-1)
        exit()

    num[s] = c

for i in range(1, n + 1):
    if num[i] == -1:
        num[i] = 0

num.pop(0)
num = int(''.join(map(str, num)))

if num < 1:
    print(100)
    exit()

print(num)
