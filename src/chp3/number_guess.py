import random

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('>'))

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break # correct guess

if guess == secret_number:
    print('Good job! You got it right in ' + str(guesses_taken) + ' guesses!')
else:
    print('The number was ' + str(secret_number))