n = int(input())

nums = [int(input()) for _ in range(n)]
nums.sort()

_num = -1
cnt = 0
ans = 0

print(nums)

for i in range(n):
    if nums[i] != _num:
        if cnt % 2 == 1:
            ans += 1

        cnt = 1
        _num = nums[i]
    else:
        cnt += 1

if cnt % 2 == 1:
    ans += 1

print(ans)
