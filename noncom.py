a = 'GeeksforGeeks'
b = 'Codefreaks'
c = ''
r = ''
k = ''
c  = set.intersection(set(a),set(b))
d = list(sorted(c))
n = a+b
for i in n:
    if i not in str(d):
        k += i
print(''.join(list(sorted(set(k)))))
        
