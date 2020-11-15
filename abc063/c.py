n = int(input())

tensu = []
seiseki = 0

for i in range(n):
    s = int(input())
    seiseki += s
    tensu.append(s)

sorted_tensu = sorted(tensu)

reducer = 0

if seiseki % 10 == 0:
    for x in sorted_tensu:
        if x % 10 != 0:
            reducer = x
            break
    else:
        reducer = seiseki

print(seiseki - reducer)
