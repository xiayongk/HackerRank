def camelcase(s):
    queue = []
    cnt = 1
    for (i, c) in enumerate(s):
        if c == c.upper():
            cnt += 1

    return cnt


if __name__ == '__main__':
    s = 'saveChangesInTheEditor'
    s = 'hiMyNameIsHayoungKim'
    print(camelcase(s))