from collections import defaultdict

players = defaultdict(set)
decks = defaultdict(set)

while (buff := input()):
    buff = [e.strip() for e in buff.split('/')]
    if buff[0].isdigit():
        decks[int(buff[0])].add(buff[-1])
    else:
        players[buff[0]].add(int(buff[-1]))



player_cards = defaultdict(int)
for player, deck in players.items():
    tmp = set()
    for i in deck:
        tmp |= decks[i]
    player_cards[player] = len(tmp)
        # player_cards[player] = player_cards[player].union(decks[i])
        # player_cards[player] |= decks[i]



a = sorted([(deck, player) for player, deck in player_cards.items()], key=lambda x: (-x[0], x[1]))
print(
    *[player[1] for player in a if player[0] == a[0][0] != 0],
    sep='\n'
)
