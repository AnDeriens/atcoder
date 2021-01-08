s = input()

exist_n = 0
exist_w = 0
exist_s = 0
exist_e = 0

for _s in list(s):
    if _s == 'N':
        exist_n = 1
    elif _s == 'W':
        exist_w = 1
    elif _s == 'S':
        exist_s = 1
    elif _s == 'E':
        exist_e = 1

if (exist_n ^ exist_s) == 1 or (exist_w ^ exist_e) == 1:
    print('No')
else:
    print('Yes')

