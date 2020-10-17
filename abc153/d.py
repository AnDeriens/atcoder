h = int(input())

h_bin = format(h, 'b')

ans = 0
for i in range(len(h_bin)):
    ans += 2 ** i

print(ans)
