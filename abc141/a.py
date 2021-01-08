weathers = [ 'Sunny', 'Cloudy', 'Rainy' ]

s = input()

for i in range(len(weathers)):
    if weathers[i] == s:
        print(weathers[(i + 1) % len(weathers)])
        exit()
