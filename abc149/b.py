a, b, k = list(map(int, input().split()))

if k >= a:
    takahashi = 0

    if b <= k - a:
        takagi = 0
    else:
        takagi = b - k + a
else:
    takahashi = a - k
    takagi = b

print(takahashi, takagi)
