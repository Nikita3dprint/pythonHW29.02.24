for n in range(6, 200):
    s = '2' + n * '4'
    while '14' in s or '244' in s or '444' in s:
        if '14' in s:
            s = s.replace('14', '2', 1)
        if '244' in s:
            s = s.replace('244', '14', 1)
        if '444' in s:
            s = s.replace('444', '21', 1)
    sum = s.count('1') + 2 * s.count('2') + 4 * s.count('4')
    if sum > 20:
        print(n)
        