print('Please think of a number between 0 and 100!')

high = 100
low = 0
guess = int((low + high)/2.0)

while True:

    print('Is your secret number ' + str(guess) + '?')
    user_input = raw_input("Enter 'h' to indicate the guess is too high. "
                            + "Enter 'l' to indicate the guess is too low. "
                            + "Enter 'c' to indicate I guessed correctly. ")

    if user_input == 'h':
        high = guess
        guess = (low + high)/2
    elif user_input == 'l':
        low = guess
        guess = (low + high)/2
    elif user_input == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")


print("Game over. Your secret number was: " + str(guess))
