n = int(input())
v = list(map(int, input().split()))

v.sort()

output = v.pop(0)

for i in range(n - 1):
    output = (v.pop(0) + output) / 2

print(output)
