r_1, c_1 = list(map(int, input().split()))
r_2, c_2 = list(map(int, input().split()))

if r_1 == r_2 and c_1 == c_2:
    print(0)
    exit()

if r_1 + c_1 == r_2 + c_2 or r_1 - c_1 == r_2 - c_2 or abs(r_1 - r_2) + abs(c_1 - c_2) <= 3:
    print(1)
    exit()

if r_1 == r_2 and c_1 != c_2:
    if abs(c_2 - c_1) % 2 == 0:
        print(2)
    else:
        print(3)
    exit()

if r_1 != r_2 and c_1 == c_2:
    if abs(r_2 - r_1) % 2 == 0:
        print(2)
    else:
        print(3)
    exit()

x = r_1
y = c_1
if (c_2 - c_1) * (r_2 - r_1) > 0:
    k = (r_2 + c_2 - r_1 - c_1) // 2
    x += k
    y += k
else:
    k = ((r_2 - c_2) - (r_1 - c_1)) // 2
    x += k
    y += k

if abs(x - r_2) + abs(y - c_2) > 3:
    print(3)
else:
    print(2)

