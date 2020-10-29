s = input()

noB = 0
ans = 0

for _s in list(s):
    if _s == 'B':
        noB += 1
    else:
        ans += noB
        

print(ans)
