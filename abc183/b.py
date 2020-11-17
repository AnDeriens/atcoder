sx, sy, gx, gy = list(map(int, input().split()))

print((((gx - sx) * sy) / (gy + sy)) + sx)
