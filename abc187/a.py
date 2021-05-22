a, b = list(map(int, input().split()))

a_1 = a // 100
a_2 = (a - a_1 * 100) // 10
a_3 = a - a_1 * 100 - a_2 * 10

b_1 = b // 100
b_2 = (b - b_1 * 100) // 10
b_3 = b - b_1 * 100 - b_2 * 10

print(max(a_1 + a_2 + a_3, b_1 + b_2 + b_3))
