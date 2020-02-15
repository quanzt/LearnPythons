import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print(f'Good job. You are correct. The secret number is {str(secretNumber)}')
else:
    print('Sorry, your guess is wrong. The secret number is {}'.format(secretNumber))

#
# for i in range(20):
#     x = random.randint(1, 3)
#     print(x)