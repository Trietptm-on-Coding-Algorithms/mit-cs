def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    copy = ()
    i = 0

    while i < len(aTup):
        copy += (aTup[i],)
        i += 2

    return copy


foo = ('I', 'am', 'a', 'test', 'tuple')

print oddTuples(foo)
