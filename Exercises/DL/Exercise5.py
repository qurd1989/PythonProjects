import copy

# type


abc = ["a", "b", "c",]
abc.insert(len(abc),"d")
print(abc)

#


def missing_char(str, n):
    front  = str[:n]
    back = str[n+1:]
    return front +  back
missing_char('kitten', 3)

# shaloow copy and deep copy

xs = [1,3, 4,5,6,7,8,9,]
xs.append('Elmar')
zs = copy.deepcopy(xs)
ys = list(xs)
xs[0] = 'New era'
xs.insert(4, 'Elmar')
print(xs)
print(zs)
print(ys)