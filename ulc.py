a = 'GFG is For GeeKs'
u = 0
l = 0
for i in a:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
print(u)
print(l)
