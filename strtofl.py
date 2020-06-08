import textwrap
a = '45.6778.4524.45'
b = textwrap.wrap(a,5)
b = list(map(float,b))
print(b)
