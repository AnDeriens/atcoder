n = int(input())
a = list(map(int, input().split()))

p = 0
for i in range(n):
    p += 1 / a[i]

print(1 / p)
