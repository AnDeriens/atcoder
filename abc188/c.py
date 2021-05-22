# 未解決

n = int(input())
a = [0] + list(map(int, input().split()))

rest_players = [_ for _ in range(1, 2 ** n + 1)]

for i in range(1, n + 1):
    lose_players = []
    for j in range(1, i + 1):
        print(2 * j - 1, rest_players)
        small_index = rest_players[2 * j - 1]
        big_index = rest_players[2 * j]

        if a[small_index] < a[big_index]:
            lose_players.append(small_index)
        else:
            lose_players.append(big_index)

    for loser in lose_players:
        rest_players.remove(loser)

print(rest_players)
