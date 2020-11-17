import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

al = itertools.permutations(range(1, n + 1))

a = 0
b = 0
i = 0
for v in al:
    i += 1
    same_p = True
    same_q = True
    v = list(v)
    for j in range(n):
        if v[j] != p[j]: 
            same_p = False
            break
    if same_p:
        a = i

    for j in range(n):
        if v[j] != q[j]: 
            same_q = False
            break
    if same_q:
        b = i
print(abs(a - b))
