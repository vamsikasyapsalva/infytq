from collections import Counter
a = '5,5,5,1,2,3,8,8,8,8'
a = a.split(',')
a = list(map(int,a))
print(a)
n = 6
c = Counter(a)
k = sorted(a, key=c.get)
print(k)
for i in k:
    if  n == 0:
        break
    elif a.count(i) >= 1 and n != 0:
        a.remove(i)
        n -= 1
print(len(set(a)))
        
