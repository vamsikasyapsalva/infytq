import re

a = 'my name is vamsi kasyap Name'

b = re.search('^my.*kasyap$',a)

#b = re.findall('name|Name',a)

#b = re.split('\s',a)

#b = re.split('\s',a,1)

#b = re.sub('\s','$',a)

#b = re.search(r'\bs\w',a)

print(b.string)
