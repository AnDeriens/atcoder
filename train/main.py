# -*- coding: utf-8 -*-

s = input()
nums = list(map(int, list(s)))
operators = ['+', '+', '+']

def exec(nums, operators):
    num = 0
    num += nums[0]        
    i = 1
    for op in operators:
        if op == '+':
            num += nums[i]
        elif op == '-':
            num -= nums[i]

        i += 1

    return num

def output(nums, operators):
    string = ''
    i = 0
    for n in nums:
        string += str(n)
        if i < len(operators):
            string += operators[i]

        i += 1

    string += '=7'
    print(string)


length = len(operators)

for i in range(2 ** length):
    _operators = operators
    for j in range(length):
        if ((i >> j) & 1):
            _operators[length - 1 - j] = '+'
        else: 
            _operators[length - 1 - j] = '-'

    if exec(nums, _operators) == 7:
        output(nums, _operators)
        break



