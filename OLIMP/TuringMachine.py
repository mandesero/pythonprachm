class Turing:
    def __init__(self, table, prog):
        table = [line.split() for line in table]
        vars = table[0]
        table.pop(0)

        for i in range(len(table)):
            rules = {vars[j]: table[i][j + 1].split(',') for j in range(len(vars))}
            table[i] = rules.copy()

        self.table = table
        self.field = ["_"] * len(prog) + list(prog) + ["_"] * len(prog)
        self.start = len(prog)
        self.run()

    def run(self):
        moves = {
            "L": -1,
            "R": +1,
            "N": 0,
            "": 0,
        }
        it = 0
        current_state = 0
        while it != 100000:
            it += 1
            action = self.table[current_state][self.field[self.start]]
            # print(action)
            if action[0]:
                self.field[self.start] = action[0]
            if action[2]:
                if action[2] == "!":
                    break
                current_state = int(action[2])
            self.start += moves[action[1]]

            if self.start >= len(self.field):
                self.field.append("_")
            elif self.start < 0:
                self.field.insert(0, '_')
                self.start += 1
        if it == 100000:
            return
        print("".join([i for i in self.field if i != '_']))


if __name__ == '__main__':
    t = []
    while True:
        s = input()
        t.append(s)
        if " " not in s:
            break
    Turing(t[:-1], t[-1])
