None
def program1(x):
    total = 0
    for i in range(1000):
        print(i)
        total += i

    while x > 0:
        x -= 1
        print(x)
        total += x
        print(x)

    return total
print(program1(1000))