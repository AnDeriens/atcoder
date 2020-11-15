s = sum([sum(list(map(int, input().split()))) for _ in range(3)])

if s % 3 == 0:
    print('Yes')
else:
    print('No')
