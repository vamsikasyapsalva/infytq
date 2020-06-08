a = input()
c = 0
for i in a:
    if i.isalpha() or i == ' ':
        c += 1
        
if c == len(a):
    print("True")
else:
    print("False")
