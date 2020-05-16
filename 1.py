a = 'Abhishek:34848,Mayur:4739,Friends:2949,Yeah:9889'
b = a.split(',')
res = ''
for i in b:
    i = i.split(':')
    w = i[0]
    d = i[1]
    l = len(w)
    m = 0
    for j in d:
        if int(j) <= l:
            if m < int(j):
                m = int(j)
    if m == 0:
        res += 'X'
    else:
        res += w[m-1]
print(res)
        
