a, b, c = list(map(int, input().split()))

turn_a = c == 0

for i in range(1000):
    if turn_a:
        a -= 1
    else:
        b -= 1

    turn_a = not turn_a

    if a < 1:
        print('Aoki')
        exit()
    if b < 1:
        print('Takahashi')
        exit()


