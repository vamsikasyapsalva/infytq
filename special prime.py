a = int(input())
b =[]
c = []
co = 0
for i in range(a+1):
    b.append(i)
print(b)
for i in b:
    for j in b[i:]:
        c.append(i+j)
print(c)

def prime(n):
    co = 0
    if n == 2:
        return n
    elif n > 1:
        for i in range(2,n):
            if n % i == 0:
                co += 1
        if co == 0:
            return n
        else:
            return False
    else:
        return False
                
               
        
s = list(map(prime,c))

print(s)

for i in s:
    if i != False:
        co += 1
print(co)
