a = '4365188'
b = ''
for i in range(len(a)):
    if i % 2 != 0:
        s = int(a[i])*int(a[i])
        b += str(s)
print(b[:4])
