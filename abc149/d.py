n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
t = input()

ans = 0

for i in range(n):
    computer = t[i]
    if i >= k:
        if computer == t[i - k]:
            continue

    if computer == 'r':
        ans += p
    elif computer == 's':
        ans += r
    else:
        ans += s

print(ans)
