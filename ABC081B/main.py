# -*- coding: utf-8 -*-

def is_all_even(nums):
    return len(list(filter(lambda x: x % 2 == 0, nums))) == len(nums)

def to_half(nums):
    return [int(i / 2) for i in nums]

def exec(nums, i):
    if is_all_even(nums):
        i+=1
        nums = to_half(nums)
        return exec(nums, i)
    else:
        return i

n = input()
nums = [int(i) for i in input().split()]
print(exec(nums, 0))
