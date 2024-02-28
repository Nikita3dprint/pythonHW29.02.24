for n in range(1, 200):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[:2]
    else:
        b = b + bin(n % 3)[2:]
    r = int(b, 2)
    if r < 105:
        print(n, r)
