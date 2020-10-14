# -*- coding: utf-8 -*-

n = int(input())

c_ac = 0
c_wa = 0
c_tle = 0
c_re = 0

for i in range(n):
    x = input()
    if x == 'AC':
        c_ac += 1
    elif x == 'WA':
        c_wa += 1
    elif x == 'TLE':
        c_tle += 1
    else:
        c_re += 1

print('AC x ' + str(c_ac))
print('WA x ' + str(c_wa))
print('TLE x ' + str(c_tle))
print('RE x ' + str(c_re))

