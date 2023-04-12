'''
크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z='''

cAl = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']

s = input()

for i in cAl:
    s=s.replace(i,'*')

print(len(s))
    







