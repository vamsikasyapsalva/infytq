a = input()
b = []
for i in a:
    if a.count(i) % 2 != 0:
        b.append(i)
print(b)
