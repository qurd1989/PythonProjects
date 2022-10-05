# nested list

l = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g']

print(l[2][2][0])
l[0] = 'orange'
print(l)
l[-1] = 'nice'
print(l)

l.append('blue')
print(l)
l.insert(0,'elmar')
print(l)
l+=([[1,2,34,5]])
print(l)
x = l.pop(2)
print(l)
del l[-1]
print(l)
