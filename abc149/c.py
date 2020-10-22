x = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1

    return lower_divisors + upper_divisors[::-1]

for n in range(x, x ** 2):
    divisors = make_divisors(n)
    if len(divisors) == 2:
        print(n)
        exit()


