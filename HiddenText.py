def check_hidden_text(string, template):
    for j in range(len(string) - len(template)):
        for i in range(1, len(string) - j):
            if template in string[j:: i]:
                return 'YES'
    return 'NO'


def main():
    s1 = input()
    s2 = input()
    print(check_hidden_text(s1, s2))


if __name__ == '__main__':
    main()