joe = "salad water hamburger salad hamburger"
joe = "hamburger water hamburger"

def item_order(order):

    salads = 0
    hamburgers = 0
    water = 0

    word = ''
    char_num = 0
    end = len(order)

    for char in order:
        char_num += 1

        if char_num == end:
            word += char

        if char == ' ' or char_num == end:
            if word == 'salad':
                salads += 1
            elif word == 'hamburger':
                hamburgers += 1
            elif word == 'water':
                water += 1
            word = ''
        else:
            word += char

    return "salad:" + str(salads) \
           + " hamburger:" + str(hamburgers) \
           + " water:" + str(water)


print item_order(joe)
