s_1 = input()
s_2 = input()
s_3 = input()
s_4 = input()

arr = [s_1, s_2, s_3, s_4]
c = ['H' , '2B' , '3B' , 'HR']

cnt = 0
for x in arr:
    if x in c:
        c.remove(x)

if len(c) == 0:
    print('Yes')
else:
    print('No')
    
