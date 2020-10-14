# -*- coding: utf-8 -*-

import re

s = input()

pattern = r'[a-z]'

if re.match(pattern, s):
    print('a')
else:
    print('A')

