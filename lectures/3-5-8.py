def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if aStr == '':
        return False

    mid = len(aStr)/2

    if aStr[mid] == char:
        return True
    elif aStr[mid] < char:
        return isIn(char, aStr[mid + 1:])
    elif aStr[mid] > char:
        return isIn(char, aStr[:mid])


print isIn('a', 'abcdefghij')
print isIn('m', 'mmmmmmmmm')
print isIn('k', 'abcdefghijk')
print isIn('n', 'abcdefghijklmnnnnn')
print isIn('x', 'abcdefg')
print isIn('n', 'abcdefg')
print isIn('y', 'abcdefgw')
print isIn('z', 'abcdefgxy')

