for a in range(1, 1000):
    l = 1
    for x in range(1, 1000):
        if ((x % 13 != 0) or not(40 <= x <= 60) or (a < x + 20)) == 0:
            l = 0
    if l == 1:
        print(a)
        