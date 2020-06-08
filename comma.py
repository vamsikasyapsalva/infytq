a = input()
b = ''
for i in a:
    if i ==',':
        continue
    else:
        b += i
b = b.split()
print(b)
