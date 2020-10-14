card = [[] for _ in range(3)]

for i in range(3):
    card[i] = list(map(int, input().split()))

n = int(input())

nums = [0] * n
for i in range(n):
    nums[i] = int(input())


for i in range(3):
    for j in range(3):
        card_num = card[i][j]
        for num in nums:
            if card_num == num:
                card[i][j] = 0

ans = False

for i in range(3):
    if card[i][0] == 0 and card[i][1] == 0 and card[i][2] == 0:
        ans = True
    if card[0][i] == 0 and card[1][i] == 0 and card[2][i] == 0:
        ans = True

if card[0][0] == 0 and card[1][1] == 0 and card[2][2] == 0:
    ans = True
if card[0][2] == 0 and card[1][1] == 0 and card[2][0] == 0:
    ans = True

if ans:
    print('Yes')
else:
    print('No')

