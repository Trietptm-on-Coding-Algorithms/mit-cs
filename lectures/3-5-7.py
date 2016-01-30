def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[:-1])


print lenRecur('')
print lenRecur('1')
print lenRecur('food')
print lenRecur('foodie')
print lenRecur('espresso')
print lenRecur('oih829b298y9h')
