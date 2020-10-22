n = int(input())
a = list(map(int, input().split()))
q = int(input())

ans = sum(a)
no_nums = [0] * (10 ** 5 + 1)

for i in range(n):
    no_nums[a[i]] += 1

for i in range(q):
    b, c = list(map(int, input().split()))
    
    ans += (c - b) * no_nums[b]
    no_nums[c] += no_nums[b]
    no_nums[b] = 0

    print(ans)
