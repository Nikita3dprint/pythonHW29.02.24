a = [int(x) for x in open('17_7819.txt')]
k = 0
mxdvz = 0
mxsum = 0
for i in range(len(a)):
    if 9 < abs(a[i]) < 100 and a[i] > mxdvz:
        mxdvz = a[i]
for i in range(len(a)-1):
    if (99 < a[i] < 1000) or (99 < a[i+1] < 1000) and (a[i] + a[i+1] % mxdvz == 0):
        k += 1
        if a[i] + a[i+1] > mxsum:
            mxsum = a[i] + a[i+1]
print(k, mxsum)
