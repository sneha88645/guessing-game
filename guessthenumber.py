import random

print("Welcome to 'Guess the Number' Gameeeeee!")

choice = input("Do you want to set your own range? (Y/N): ").strip().lower()

if choice == 'y':
    print("Great! Let's set your custom range.")
    min_val = int(input("Enter the minimum number of the range: "))
    max_val = int(input("Enter the maximum number of the range: "))
elif choice == 'n':
    min_val = 1
    max_val = 100
    print("No problem! We'll use the default range of 1 to 100.")
else:
    print("Invalid choice! Using default range of 1 to 100.")
    min_val = 1
    max_val = 100

print("-----------------------------------------------------")

target = random.randint(min_val, max_val)

attempts = 10

while True:
    
    while attempts > 0:
        userguess = input("Guess the target number or quit the game Q:\n ").strip()
        
        if userguess.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            break
        
        guess = int(userguess)
        attempts -= 1
        
        if guess < target:
            print("Your guess number is too small! Think bigger.\n")
        
        elif guess > target:
            print("Your guess number is too high! Think smaller.\n")
        
        else:
            print("Congratulations! You've guessed the number!\n\n")
            break
        
        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The number was {target}\n\n")
        else:
            print(f"You have {attempts} attempts left.\n")

    repeat = input("Do you want to continue the game? (y/n): ").strip().lower()
    if repeat == 'n':
        print("Thanks for playing! Goodbye.")
        break
    else:
        # Resetting the game
        choice = input("Do you want to set your own range? (Y/N): ").strip().lower()
        target = random.randint(min_val, max_val)
        attempts = 10

print("Game Over.\n")