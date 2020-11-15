n = int(input())

dots = []
for i in range(n):
    x, y = list(map(int, input().split()))
    dots.append({"x": x, "y": y})

x_vertical = []
y_vertical = []
katamuki = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if dots[j]['x'] == dots[i]['x']:
            x_vertical.append(dots[j]['x'])
        elif dots[j]['y'] == dots[i]['y']:
            y_vertical.append(dots[j]['y'])
        else:
            k = (dots[j]['y'] - dots[i]['y']) / (dots[j]['x'] - dots[i]['x'])
            katamuki.append(k)

if len(katamuki) != len(list(set(katamuki))) or len(x_vertical) != len(list(set(x_vertical))) or len(y_vertical) != len(list(set(y_vertical))):
    print('Yes')
else:
    print('No')

