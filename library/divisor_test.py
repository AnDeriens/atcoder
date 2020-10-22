import divisor

inputs = [1, 3, 4, 6, 11]
outputs = []
outputs.append([1]) # 1
outputs.append([1, 3]) # 3
outputs.append([1, 2, 4]) # 4
outputs.append([1, 2, 3, 6]) # 6
outputs.append([1, 11]) # 11 

errors = []

for i in range(len(inputs)):
    output = divisor.giveDivisors(inputs[i])
    if outputs[i] == output:
        print('.')
    else:
        print('[failure] No. ' + str(i))
        print('*input: ', inputs[i])
        print('*expected: ', outputs[i])
        print('*acctual: ', output)

