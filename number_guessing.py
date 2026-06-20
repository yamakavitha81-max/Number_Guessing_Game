import random

best_score = None

print("=========== WELCOME TO NUMBER GUESSING GAME ===========")

while True:

    print("\nChoose Difficulty")
    print("1. Easy (1-50) - 10 Attempts")
    print("2. Medium (1-100) - 7 Attempts")
    print("3. Hard (1-200) - 5 Attempts")

    choice = input("Enter Your Choice (1/2/3): ")

    if choice == "1":
        max_number = 50
        max_attempts = 10
    elif choice == "2":
        max_number = 100
        max_attempts = 7
    elif choice == "3":
        max_number = 200
        max_attempts = 5
    else:
        print("Invalid choice! Medium mode selected.")
        max_number = 100
        max_attempts = 7

    secret_number = random.randint(1, max_number)
    attempts = 0
    guessed = False

    print(f"\nGuess a number between 1 and {max_number}")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter numbers only!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("\n Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            guessed = True

            if best_score is None or attempts < best_score:
                best_score = attempts
                print(" New Best Score!")

            break

        print(f"Attempts Left: {max_attempts - attempts}")

    if not guessed:
        print("\n Game Over!")
        print(f"The Correct Number was {secret_number}")

    if best_score is not None:
        print(f"Best Score: {best_score} attempts")

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again not in ["y", "yes"]:
        print("\nThank you for playing!")
        break