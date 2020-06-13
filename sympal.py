a = 'amaama'
a1 = a[:len(a)//2]
a2 = a[len(a)//2:]
if a1 == a2:
    print('symmetric')
if a == a[::-1]:
    print('palindrome')
