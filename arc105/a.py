a,b,c,d = list(map(int, input().split()))

a_index = [True, False]
b_index = [True, False]
c_index = [True, False]
d_index = [True, False]


for _a in a_index:
    for _b in b_index:
        for _c in c_index:
            for _d in d_index:
                pos = 0

                if _a:
                    pos += a
                else:
                    pos -= a

                if _b:
                    pos += b
                else:
                    pos -= b

                if _c:
                    pos += c
                else:
                    pos -= c

                if _d:
                    pos += d
                else:
                    pos -= d

                if pos == 0:
                    print('Yes')
                    exit()

print('No') 
