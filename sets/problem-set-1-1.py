s = 'azcbobobegghakl'

def count_vowels(check_string):
    vowels = 'aeiouAEIOU'

    count = 0

    for char in check_string:
        if char in vowels:
            count += 1

    return count

vowel_count = count_vowels(s)

print('Number of vowels: ' + str(vowel_count))
