def search_max_sub_seq():
    max_len, cur_len = 1, 1
    prev = int(input())
    while (cur := int(input())) != 0:
        if cur >= prev:
            cur_len += 1
        else:
            max_len = max(cur_len, max_len)
            cur_len = 1
        prev = cur
    return max(cur_len, max_len)


def main():
    print(search_max_sub_seq())


if __name__ == '__main__':
    main()

