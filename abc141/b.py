s = input()

humiyasui = True

for i in range(len(s)):
    char = s[i]
    if i % 2 == 0 and char == 'L':
        humiyasui = False

    if i % 2 == 1 and char == 'R':
        humiyasui = False

if humiyasui:
    print('Yes')
else:
    print('No')

