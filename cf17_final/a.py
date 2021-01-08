import re

s = input()

pattern = re.compile(r'\AA?KIHA?BA?RA?\Z')

if pattern.match(s):
    print('YES')
else:
    print('NO')
