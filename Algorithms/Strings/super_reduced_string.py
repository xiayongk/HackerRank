def superReducedString(s):
    result = []
    for c in s:
        if len(result) == 0:
            result.append(c)
        else:
            if c == result[-1]:
                result.pop()
            else:
                result.append(c)
    
    if len(result) == 0:
        return 'Empty String'
    
    return ''.join(result)


if __name__ == '__main__':
    s = 'aaabccddd'
    print(superReducedString(s))