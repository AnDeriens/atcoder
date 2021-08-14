ss = input()
n = 10 ** 9 + 7

x = {'c': 0, 'h': 0, 'o': 0, 'k': 0, 'u': 0, 'd': 0, 'a': 0, 'i': 0}

for s in ss:
    if s == 'c':
        x['c'] += 1

    if s == 'h':
        x['h'] += x['c'] % n

    if s == 'o':
        x['o'] += x['h'] % n

    if s == 'k':
        x['k'] += x['o'] % n

    if s == 'u':
        x['u'] += x['k'] % n

    if s == 'd':
        x['d'] += x['u'] % n

    if s == 'a':
        x['a'] += x['d'] % n

    if s == 'i':
        x['i'] += x['a'] % n

print(x['i'] % n)
