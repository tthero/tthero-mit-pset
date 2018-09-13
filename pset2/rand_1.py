print("Please think of a number between 0 and 100")
low, high = 0, 100
guess = ''
while (guess != 'c'):
    avg = (low + high) // 2

    print("Is your secret number {}?".format(avg))
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if guess == 'c':
        print("Game over. Your secret number was:", avg)
    elif guess == 'l':
        low = avg
    elif guess == 'h':
        high = avg
    else:
        print("Sorry, I did not understand your input.")
