def min(x,y) :
    if x != y : return x if x < y else y
    

def max(x,y) :
    if x != y : return x if x > y else y


def abs(x):
    if x < 0:
        return -x
    else:
        return x

def abs_max(x,y) :
        x = abs(x)
        y = abs(y)
        if x != y : return x if x > y else y
