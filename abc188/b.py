n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

r = 0
for i in range(n):
    r += a[i] * b[i]

if r == 0:
    print('Yes')
else:
    print('No')

