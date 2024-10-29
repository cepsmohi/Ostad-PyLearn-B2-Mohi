import random

random_number = random.randint(1, 100)
attempts = 0

print("\n"+"Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100."+"\n")

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))

        if guess < 1 or guess > 100:
            raise ValueError("Please enter a number between 1 and 100.")

        attempts += 1

        if guess == random_number:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        elif guess < random_number:
            print("Too low!"+"\n")
        else:
            print("Too high!"+"\n")
    except Exception as e:
        print(f"Error: {e}")