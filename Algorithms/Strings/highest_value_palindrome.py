def highestValuePalindrome(s, n, k):
    s = list(s)
    start = 0
    end = n - 1
    mid = end // 2
    diff_index_list = []
    diff_cnt = 0
    for i in range(start, mid+1):
        if s[i] != s[end-i]:
            diff_index_list.append(i)
            diff_index_list.append(end-i)
            if int(s[i]) > int(s[end-i]):
                s[end-i] = s[i]
            else:
                s[i] = s[end-i]
            k -= 1
            if k < 0:
                return '-1'
    
    if k > 0:
        for i in range(0, mid+1):
                if k <= 0:
                    break
                if s[i] == '9':
                    continue
                else:
                    if i in diff_index_list:
                        s[i] = s[end-i] = '9'
                        k -= 1
                    else:
                        if k < 2:
                            s[mid] = '9'
                            k -= 1
                        else:
                            s[i] = s[end-i] = '9'
                            k -= 2
        
    return ''.join(s)
            

if __name__ == '__main__':
    s = '12321'
    n = 5
    k = 1
    print(highestValuePalindrome(s, n, k))