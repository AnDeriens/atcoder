n = int(input())
a = list(map(int, input().split()))

ans = True

for x in a:
    if x % 2 == 0:
        if x % 3 != 0 and x % 5 != 0:
            ans = False

if ans:
    print('APPROVED')
else:
    print('DENIED')
