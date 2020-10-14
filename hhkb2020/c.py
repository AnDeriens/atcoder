n = int(input())
p = list(map(int, input().split()))

s_list = [False for i in range(n)]

ans = 0
x_max = 0


for i in range(n):
    x = p[i]
    s_list[x] = True


    if ans != x:
        print(ans)
    else:
        for j in range(ans + 1):
            if p[j] != 
