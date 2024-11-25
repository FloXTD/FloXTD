def guess_number(low, high):
    print(f"Think of a number between {low} and {high}, and I'll try to guess it!")
    attempts = 0  # To count the number of guesses

    while low <= high:
        attempts += 1
        guess = (low + high) // 2  # Midpoint of the range
        response = input(f"Is your number {guess}? (yes/higher/lower): ").strip().lower()

        if response == "yes":
            print(f"I guessed it! Your number is {guess}. It took me {attempts} tries.")
            break
        elif response == "higher":
            low = guess + 1  # Narrow the range to higher numbers
        elif response == "lower":
            high = guess - 1  # Narrow the range to lower numbers
        else:
            print("Please respond with 'yes', 'higher', or 'lower'.")
    else:
        print("Hmm, something went wrong. Are you sure your responses were consistent?")

# Run the game
guess_number(1, 100)
