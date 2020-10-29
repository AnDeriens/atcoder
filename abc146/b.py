n = int(input())
s = input()

ans = ''

for i in list(s):
    ord_s = ord(i)
    num = ord_s + n
    if num > 90:
        num -= 26

    ans += chr(num)

print(ans)

