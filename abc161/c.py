n, k = list(map(int, input().split()))

if n == k:
    print(0)
    exit()
elif n > k:
    n = n % k

# n < k

m = k - n
print(min(n, m))
