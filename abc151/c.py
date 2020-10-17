n, m = list(map(int, input().split()))

problems = [0] * (n + 1)
penalty = 0
correct = 0

for i in range(m):
    p, s = input().split()
    p = int(p)

    if problems[p] == -1:
        continue

    if s == 'WA':
        problems[p] += 1

    if s == 'AC':
        penalty += problems[p]
        correct += 1
        problems[p] = -1

print(correct, penalty)
