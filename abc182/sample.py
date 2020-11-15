
def present(l):
    for i in range(len(l)):
        print(l[i])

    print('')

x = [['.'] * 3 for i in range(3)]

present(x)

x[1][1] = 'B'

present(x)
