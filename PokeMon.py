from collections import defaultdict

players = defaultdict(set)
decks = defaultdict(set)

while (buff := input()):
    buff = [e.strip() for e in buff.split('/')]
    if buff[0].isdigit():
        decks[int(buff[0])].add(buff[-1])
    else:
        players[buff[0]].add(int(buff[-1]))

player_cards = defaultdict(set)
for player, deck in players.items():
    for i in deck:
        player_cards[player] = player_cards[player].union(decks[i])

a = sorted([(len(deck), player) for player, deck in player_cards.items()], key=lambda x: (-x[0], x[1]))
print(
    *[player[1] for player in a if player[0] == a[0][0] != 0],
    sep='\n'
)
