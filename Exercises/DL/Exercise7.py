import  operator
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(sorted(xs.items(), key=lambda x: x[1]))


a = [1,2,3]
b =a
print(a==b)
print(b is a)
c = list(a)
print(a == c)

print(a is c)

#
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}
def greeting (userid):
    return "Hi %s! " % name_for_userid.get(userid, "there")

print(greeting(382))

print(greeting(3333))


def myfunc(a, b):
    return a + b
funcs = [myfunc]
print(funcs[0](3,4))
