n = input()
s = sum(list(map(int, list(n))))

if s % 3 == 0:
    print(0)
    exit()

if len(n) == 1:
    print(-1)
    exit()

for _n in n:
    if (s - int(_n)) % 3 == 0:
        print(1)
        exit()

if len(n) == 2:
    print(-1)
    exit()

if s % 3 == 2:
    if len(list(filter(lambda x: x % 3 == 1, list(map(int, list(n)))))) >= 2:
        print(2)
        exit()
else:
    if len(list(filter(lambda x: x % 3 == 2, list(map(int, list(n)))))) >= 2:
        print(2)
        exit()

print(-1)
