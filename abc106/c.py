s = input()
k = int(input())

first_not_1 = k + 1
for i in range(len(s)):
    if s[i] != '1':
        first_not_1 = i + 1
        break

if first_not_1 > k:
    print(1)
else:
    print(s[first_not_1 - 1])
