a = 'gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb'
b = ['gfg', 'is', 'best']
c = []
d = []
e = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        c.append(a[i:j])
        
for i in c:
    if i in b:
        d.append(i)
for i in d:
    e.append(a.count(i))
s = e.index(max(e))
print(d[s])
    
