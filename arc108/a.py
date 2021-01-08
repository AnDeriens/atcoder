s, p = list(map(int, input().split()))

n = s ** 2 - 4 * p

def is_square_root(n):
    m = int(n**.5)
    if abs(m*m - n) < 1e-6:
        return True
    else:
        return False

if is_square_root(n):
    print('Yes')
else:
    print('No')
