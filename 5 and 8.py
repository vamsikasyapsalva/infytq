a = input()
a = a.split(',')
n1 = 0
n2 = ''
s = 0
if a.index('5') < a.index('8'):
    for i in range(len(a)):
        if i not in range(a.index('5'),a.index('8')+1):
           n1 += int(a[i])
        else:
            n2 += a[i]
print(n1+int(n2))
