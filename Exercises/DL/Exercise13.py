# using dict as switch case statments

def dispatch_if(operator, x,y):
    if operator == 'add':
        return  x +y
    elif operator == 'sub':
        return  x-y
    elif operator == 'mal':
        return x * y
    elif operator  == 'div':
        return  x / y
    else:
        return None

def dispatch_dict(operator, x, y):
    return {
        'add' : lambda: x +y,
        'sub' : lambda: x - y,
        'mal': lambda : x *y,
        'dic': lambda: x /y
    }.get(operator,lambda : None) ()
print(dispatch_dict('mal' , 2, 8))
print(dispatch_if('mal' , 2, 8))