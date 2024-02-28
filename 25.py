#100000000
#10o0639
#10o06039
for a in range(10):
    for b in range(10):
        x = 1000639 + a * 100000 + b * 1000
        if x % 131 == 0:
            print(x, x // 131)
for a in range(10):
    for b in range(10):
        for c in range(10):
            x = 10006039 + a * 1000000 + b * 10000 + c * 100
            if x % 131 == 0:
                print(x, x // 131)

