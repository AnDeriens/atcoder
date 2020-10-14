n, m = list(map(int, input().split()))
w = list(map(int, input().split()))

l = [0] * (m + 1)
v = [0] * (m + 1)

s_weight = [0] * (n + 1)
s = 0
for i in w:
    s += i
    s_weight[i+1] = s

l_max = 0
l_max_index = 0
v_min = 100000001 
v_min_index = 0 

for i in range(1, m + 1):
    x, y = list(map(int, input().split()))
    l[i] = x  
    v[i] = y  

    if x > l_max:
        l_max = x
        l_max_index = i

    if v_min > y:
        v_min = y
        v_min_index = i

if v_min >= s:
    print(0)
    exit()

# ??
