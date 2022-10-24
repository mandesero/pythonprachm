def turtle(coord, direction):
    x, y = coord

    cur_dir = {
        0: (1, 0),     # восток
        1: (0, 1),     # север
        2: (-1, 0),    # запад
        3: (0, -1),    # юг
    }

    command = yield x, y

    while True:

        if command == "f":
            x += cur_dir[direction][0]
            y += cur_dir[direction][1]

        if command == "l":
            direction = (direction + 1) % 4

        if command == "r":
            direction = (direction - 1) % 4

        command = yield x, y
