n = int(input())

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

for i in make_divisors(n):
    print(i)
