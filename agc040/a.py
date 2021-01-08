s = input()

nums  = [0] * (len(s) + 1)
rnums = [0] * (len(s) + 1)
n = len(s)

conti = 0
max_conti = 0
for k in range(1, len(s) + 1):
    if s[k - 1] == '<':
        conti += 1
    else:
        conti = 0
    max_conti = max(conti, max_conti)
    nums[k] = max_conti

conti = 0
max_conti = 0
for k in range(1, len(s) + 1):
    if s[-k] == '>':
        conti += 1
    else:
        conti = 0

    max_conti = max(conti, max_conti)
    rnums[n - k] = max_conti

print(nums, rnums)

ans = 0
for i in range(n + 1):
    ans += max(nums[i], rnums[i])

print(ans)
