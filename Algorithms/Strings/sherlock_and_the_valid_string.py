def isValid(s):
    cnt_dict = {}
    for c in s:
        if c in cnt_dict:
            cnt_dict[c] += 1
        else:
            cnt_dict[c] = 1

    cnt_list = cnt_dict.values()
    cnt_set = set()
    for cnt in cnt_list:
        cnt_set.add(cnt)
    
    cnt_set = list(cnt_set)
    if len(cnt_set) == 1: # 모든 알파벳의 빈도 수가 동일한 경우
        return 'YES'
    elif len(cnt_set) == 2: # 알파벳 빈도 수 종류가 2개인 경우
        first_cnt_list = list(filter(lambda x: x == cnt_set[0], cnt_list))
        second_cnt_list = list(filter(lambda x: x == cnt_set[1], cnt_list))
        if len(first_cnt_list) == 1: 
            if cnt_set[0] == 1 or (cnt_set[0] - cnt_set[1]) == 1:
                return 'YES'
            else:
                return 'NO'
        elif len(second_cnt_list) == 1:
            if cnt_set[1] == 1 or (cnt_set[1] - cnt_set[0]) == 1:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
    else:
        return 'NO'
    

if __name__ == '__main__':
    s = 'abcdefghhgfedecba' # YES
    s = 'aabbbcccddd' # NO
    print(isValid(s))