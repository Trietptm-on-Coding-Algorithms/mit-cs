s = 'azcbobobegghaklbob'


def count_bobs(check_string):
    target = 'bob'

    count = 0

    max_index = len(check_string) - len(target)

    for index in range(0, max_index + 1):
        if check_string[index:index+3] == target:
            count += 1

    return count

bob_count = count_bobs(s)

print('Number of times bob occurs is: ' + str(bob_count))
