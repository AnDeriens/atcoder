n = int(input())
s = input()

if n % 2 == 1:
    print('No')
    exit()

for i in range(int(n / 2)):
    if s[i] != s[i + int(n / 2)]:
        print('No')
        exit()

print('Yes')
