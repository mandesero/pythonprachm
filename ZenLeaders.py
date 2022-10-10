players = []
while (buf := input()):
    fname, sname, *team, time = buf.split()
    players.append([fname, sname, ' '.join(team), time])

players = sorted(players, key=lambda x: list(map(int, x[-1].split(':'))) + x[1:2] + x[0:1] + x[2:3])
maxf = max(map(len, [x[0] for x in players]))
maxs = max(map(len, [x[1] for x in players]))
maxt = max(map(len, [x[2] for x in players]))
i, prev_time = 0, 0
for player in players:
    if player[-1] != prev_time:
        i += 1
        if i > 3:
            break

    print(player[0].ljust(maxf), player[1].ljust(maxs), player[2].ljust(maxt), player[3].ljust(8))

    prev_time = player[-1]
