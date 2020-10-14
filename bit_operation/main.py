# -*- coding: utf-8 -*-

"""
print(0b101) # 5
print(bin(5)) # 0b101

## 左シフト
print(bin(5<<0)) # 0b101
print(bin(5<<1)) # 0b1010
print(bin(5<<2)) # 0b10100
print(bin(5<<3)) # 0b101000
print(bin(5<<4)) # 0b1010000

print(0b101) # 5
print(0b1010) # 10
print(0b10100) # 20
print(0b101000) # 40
print(0b1010000) # 80

## 右シフト
print(bin(5>>0)) # 0b101
print(bin(5>>1)) # 0b10
print(bin(5>>2)) # 0b1
print(bin(5>>3)) # 0b0
print(bin(5>>4)) # 0b0

print(0b101) # 5
print(0b10) # 2
print(0b1) # 1
print(0b0) # 0
print(0b0) # 0
"""

## 演算
"""
a = 0b10010011 # 146
b = 0b10110001 # 49
print(a)
print(b)

## 論理積
print(bin(a & b))
print(a & b)
## 論理和
print(bin(a | b))
print(a | b)
## 排他的論理和
print(bin(a ^ b))
print(a ^ b)
## 反転
print(bin(~a))
print(~a)
print(bin(~b))
print(~b)
"""

## ビットマスク
p = 0b10010011
q = 0b00000111

print(bin(p))
print(bin(q))

print(bin(p & q))
print(bin((p >> 2) & q))

print(p)
print(~p)
print(~1 & p)
print(bin(~1 & p))
print(bin(p & ~q))

