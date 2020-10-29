days = ['SUN','MON','TUE','WED','THU','FRI','SAT']

s = input()
i = 0

if s == 'SUN':
    print(7)
    exit()

while (i <= 8):
    if s == days[i]:
        print((7 - i) % 7)
        exit()
    i += 1
