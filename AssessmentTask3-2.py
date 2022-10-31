import random

answer = random.randint(1, 100)
guess = 0
guesses = [0, 0]

print("WELCOME TO THE GUESSING GAME!!.")
print("I HAVE A NUMBER BETWEEN 1 AND 100.")
print("IF YOUR FIRST GUESS IS WITHIN 10 OF THE NUMBER I PICKED,I WILL SAY WARM.")
print("IF YOUR FIRST GUESS IS NOT WITHIN 10 OF THE NUMBER I PICKED, I WILL SAY COLD.")
print("I WILL SAY YOU ARE  WARMER IF YOUR GUESS IS CLOSER THAN YOUR MOST RECENT GUESS.")
print("I WILL SAY YOU ARE COLDER IF YOUR GUESS IS FURTHER THAN YOUR MOST RECENT GUESS.")

while guess != answer:
    print("GUESS BETWEEN 1 AND 100, WHAT'S YOUR GUESS?")
    guess = int(input())
    guesses.append(guess)
    lastGuess = abs(guesses[-2] - answer)
    currentGuess = abs(guesses[-1] - answer)

    if guess == answer:
        print("CONGRATULATIONS YOU WON! THE CORRECT ANSWER IS: ", answer)
        print("IT TOOK YOU", len(guesses) - 2, "GUESSES TO GET THE CORRECT ANSWER")
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        print("PLEASE TRY AGAIN!")
    if guesses[-2]:
        if currentGuess < lastGuess:
            print("Warmer")
        elif currentGuess > lastGuess:
            print("Colder")
    else:
        if abs(answer - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
