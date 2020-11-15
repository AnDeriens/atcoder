n = int(input())

ans = n 

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        a = i
        b = int(n / i)
        ans = min(ans, a + b - 2)

print(ans)

