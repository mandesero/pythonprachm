def check_hidden_text(string, template):
    if any([letter not in string for letter in template]):
        return 'NO'
    start = string.index(template[0])
    for step in range(1, len(string)):
        if template in string[start::step]:
            return "YES"
    return "NO"


def main():
    s1 = input()
    s2 = input()
    print(check_hidden_text(s1, s2))


if __name__ == '__main__':
    main()
