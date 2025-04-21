i=['a','b','c']
j=('a','b','c')
k={'a','b','c'}
l={'a':'aadii', 'b':'bok'}
print(i[1])
print(j[1])
# print(k[1])
# print(l[1])
# print(dir(set))
methods = [method for method in dir(set) if not method.startswith('__')]
print(methods)
