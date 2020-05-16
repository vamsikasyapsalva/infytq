a = input()
s = []
c = 0
for i in a:
    if i == '[' or i == '{' or i == '(':
        s.append(i)
        c += 1
        continue
    if len(s) == 0:
        print(c+1)
    x = s.pop()
    if i == ']' and x == '[':
        c += 1
    elif i == '}' and x == '{':
        c += 1
    elif i == ')' and x == '(':
        c += 1
    else:
        print(c+1)
if len(s)!= 0:
    print(c+1)
else:
    print("Balanced")
