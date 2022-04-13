import random

# print(random.randint(1,10))
random_number = random.randint(1,100)

guess_count = 0

while True:
    user_guess_number = int(input("Guess a number between 1 to 100 ="))

    if user_guess_number == random_number:
        print(f"you have guessed the number in {guess_count} guesses")
        break
    elif user_guess_number<random_number:
        print("Your number is low")
    elif user_guess_number > random_number:
        print("Your number is high")

    guess_count +=1