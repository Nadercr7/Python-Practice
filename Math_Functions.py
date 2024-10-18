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


def floor(x):
    if x == int(x):   return int(x)
    elif x > 0:       return int(x)
    else:             return int(x) - 1


def ceil(x):
    if x == int(x):  return int(x)
    elif x > 0:      return int(x) + 1
    else:            return int(x)

