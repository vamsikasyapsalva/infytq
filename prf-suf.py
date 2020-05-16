a = input()
h = len(a)//2

for i in range(h,0,-1):
    p = a[0:i]
    #print(p)
    s = a[len(a)-i:len(a)]
    print(s)
    if p == s:
        print(len(p))
        break
