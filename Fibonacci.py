n = int(input('Sequence Number: '))
d = [0, 1]
g = []
a = 0
b = 1
for iii in range(n):
    c = a + b
    d.append(c)
    a = b
    b = c
    if iii == n-1:
        f = a/b
print(d)
print('Golden Number is : ', f)
    