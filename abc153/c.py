n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

h.sort()

attack = 0

for i in range(n - k):
    attack += h[i] 

print(attack)
