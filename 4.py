a = ['a', '1', 'b', '2', 'c', '3']
b = []
c = []
for i in a:
    if i in '123':
        b.append(i)
    else:
        c.append(i)
del a
print(b)
print(c)