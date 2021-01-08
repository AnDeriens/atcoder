n, x = list(map(int, input().split()))
s = input()

for i in range(n):
    if s[i] == 'o':
        x += 1
    else:
        x = max(x - 1, 0)

print(x)

