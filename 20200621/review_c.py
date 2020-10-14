# -*- coding: utf-8 -*-

# 知らない文法

# UTFコードポイント
print(ord('a'));
print(ord('b'));
print(ord('c'));
print(ord('d'));

print(chr(97));
print(chr(98));
print(chr(99));
print(chr(100));


# 商を求める
N = 27
N //= 26
print(N)

# 文字列の切り出し
string = list("abcdefghij")
print(string[0:10:1])
print(string[::1])
print(string[::-1])
print(string[::2])
print(string[::-2])
print(string[1::2])
print(string[0:7:1])
print(string[0:7:3])
