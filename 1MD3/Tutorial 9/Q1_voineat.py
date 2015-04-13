class ChangeRemainderError(Exception):
    pass

class ChangeParameterError(Exception):
    pass

def change(a, d):
    """ Computes the change of amount a given denominations d. Parameter
    a must be of type int, d must be of type list of int, and the
    elements of d must be in ascending order, otherwise
    ChangeParameterError is raised. The result is a list of the same
    length as d consisting of pairs with the number of coins / bills of
    each denomination. This is computed by first taking the maximal
    number of coins / bill of the highest denomination, then the next
    highest, etc. If no exact change is possible, ChangeRemainderError
    is raised."""
    if type(a) != type(2): raise ChangeParameterError
    if type(d) != type([]): raise ChangeParameterError
    for i in range(len(d)):
        if type(d[i]) != type(2): raise ChangeParameterError
        if d[i] < d[0]: raise ChangeParameterError

    if a % d[0] != 0: raise ChangeRemainderError
    i, r, c = len(d) - 1, a, []
    while i>= 0:
        c.append(r // d[i])
        r = r % d[i]
        if i == 0 and r % d[i] != 0:
            raise ChangeParameterError
        i = i - 1
    c = c[::-1]
    return c

def printChange(a, d):
    try:
        print(change(a, d))
    except ChangeParameterError:
        print('needs an integer amount and a non-empty list \
of denominations in ascending order')
    except ChangeRemainderError:
        print('no exact change possible')
    except:
        print('unexpected error')
