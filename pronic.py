import math 
a = '93012630'
a = list(a)
a = list(map(int,a))
b = []
f = []
def powerset(s):
    n = len(s)
    masks = [1<<j for j in range(n)]
    for i in range(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]

for i in powerset(a):
    i = list(map(str,i))
    i = ''.join(i)
    b.append(i)
b = b[1:]
b = list(map(int,b))
#print(b)
def pron(n) : 
	x = (int)(math.sqrt(n)) 

	# Checking Pronic Number by multiplying 
	# consecutive numbers 
	if (x*(x + 1)== n): 
		return n
	else:
	    return 0
	
k = list(map(pron,b))
for i in k:
    if i != 0:
        f.append(i)
print(list(sorted(set(f))))
