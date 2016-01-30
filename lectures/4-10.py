def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowels = 'aeiouAEIOU'
    counter = 0
    vowel_count = len(vowels)
    while counter < vowel_count:
        check_char = vowels[counter:counter+1]
        counter += 1
        if check_char == char:
            return True

    return False

print isVowel('x')
print isVowel('A')
print isVowel('a')
print isVowel('i')
print isVowel('e')
print isVowel('U')
print isVowel('m')
print isVowel('B')

