import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("Choose a difficulty level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")
    
    difficulty = input("Enter the difficulty level (1/2/3): ")
    
    tries_dict = {'1': 10, '2': 7, '3': 5}
    max_attempts = tries_dict.get(difficulty, 7)  # Default to Medium if invalid input
    
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = int(input(f"Guess the number (1-100). You have {max_attempts - attempts} attempts left: "))
        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} tries.")
            return
        elif guess < number_to_guess:
            print("Too Low!")
        else:
            print("Too High!")
        
        if attempts == 3:
            hint = "Hint: The number is divisible by " + str(random.choice([i for i in range(2, 10) if number_to_guess % i == 0]))
            print(hint)

    print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

guess_the_number()