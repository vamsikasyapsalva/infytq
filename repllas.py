a = 'GFG is good'
b = 'best'
a = a.split()
a.remove(a[-1])
a.append(b)
print(' '.join(a))
