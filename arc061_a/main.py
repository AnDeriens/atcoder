# -*- coding: utf-8 -*-

s = input()

s_list = list(s)
operator_box = list(range(len(s_list) - 1))
operators = dict(zip(operator_box, list(map(lambda x: False, operator_box))))

result = 0

# あるオペレータの組み合わせにおける数の和を出す
def calc(nums, operators):
    sums = 0
    _index = 0
    for index, operator in operators.items():
        if operator:
            if _index == index:
                chars = [nums[_index]]
            else:
                chars = nums[_index: int(index) + 1]

            _index = int(index) + 1
            number = ''.join(chars)
            sums += int(number)

    chars = nums[_index:]
    sums += int(''.join(chars))
    return sums

length = len(operators)

for i in range(2 ** length):
    _operators = operators
    for j in range(length):
        if ((i >> j) & 1):
            _operators[length - 1 - j] = True
        else: 
            _operators[length - 1 - j] = False

    result += calc(s_list, _operators)

print(result)

