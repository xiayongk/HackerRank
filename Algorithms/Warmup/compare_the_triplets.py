def compareTriplets(a, b):
    a_points = 0
    b_points = 0

    for (a_s, b_s) in zip(a, b):
        if a_s > b_s:
            a_points += 1
        elif b_s > a_s:
            b_points += 1
    
    return [a_points, b_points]


if __name__ == '__main__':
    a = [17, 28, 30]
    b = [99, 16, 8]

    print(compareTriplets(a, b))