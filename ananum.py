s1 = input()
s2 = input()
a = []
b = []
d = []
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        a.append(s1[i:j])
#print(a)
for i in a:
    if len(i) == len(s2) and i[0] in s2 and i[len(i)-1] in s2:
        c = 0
        for j in i[1:len(i)-1]:
            if j in s2:
                c += 1
        if c == len(s2)-2:
            b.append(i)
#print(b)
print('no of anagrams:',len(b))
for i in b:
    d.append(s1.find(i))
print(d)
