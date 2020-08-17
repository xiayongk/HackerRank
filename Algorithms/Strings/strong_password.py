def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    remain = 0
    if n < 6:
        remain = 6 - n
    
    number_condition = 1
    lower_condition = 1
    upper_condition = 1
    special_condition = 1
    for c in password:
        if c in numbers:
            number_condition = 0
        elif c in lower_case:
            lower_condition = 0
        elif c in upper_case:
            upper_condition = 0
        elif c in special_characters:
            special_condition = 0

    remain_condition = number_condition + lower_condition + upper_condition + special_condition
    
    if remain == 0:
        return remain_condition
    else:
        if remain > remain_condition:
            return remain
        else:
            return remain_condition


if __name__ == '__main__':
    n = 3
    password = 'Ab1'
    print(minimumNumber(n, password))