t = int(input())

def execute():
    n = int(input())
    a = list(map(int, input().split()))

    turn = 0 # 0: 先手, 1: 後手
    
    # コインを皿に移す
    turn = n % 2

    cnt_1 = 0
    cnt_2 = 0
    for _a in a:
        if _a == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1

    # 皿からコインを取り除く
    if cnt_2 > 0:
        turn = (turn + cnt_2) % 2
    else:
        turn = ((turn + cnt_1) % 2) + 1
    
    if turn % 2 == 0:
        print("Second")
    else:
        print("First")

for i in range(t):
    execute()
