import random
from letter_state import LetterState
from colorama import Fore, Back, Style

# Constants for game configuration
WORD_LENGTH = 5  # Length of the target word
MAX_ATTEMPTS = 6  # Maximum number of guesses allowed

# Load the word list from file
def load_word_list(file_path):
    """
    Load words from a file into a list.

    Args:
        file_path: Path to the file containing words

    Returns:
        List of words loaded from the file
    """
    word_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()  # Convert to uppercase for consistency
            word_list.append(word)
    return word_list

# Process the player's guess and determine letter states
def process_guess(guess, secret):
    """
    Compare the player's guess with the secret word and determine the state of each letter.

    Args:
        guess: The player's guessed word
        secret: The target word to guess

    Returns:
        List of LetterState objects representing the state of each letter in the guess
    """
    # Initialize letter states for each character in the guess
    result = []
    for i in range(WORD_LENGTH):
        result.append(LetterState(guess[i]))

    # First pass: Check for correct positions (green letters)
    for i in range(WORD_LENGTH):
        if guess[i] == secret[i]:
            result[i].is_in_position = True
            result[i].is_in_word = True

    # Second pass: Check for letters in word but wrong position (yellow letters)
    for i in range(WORD_LENGTH):
        if result[i].is_in_position:
            continue  # Skip letters already marked as correct position

        # Check if the letter exists in the secret word
        # and hasn't been accounted for by another guess letter
        for j in range(WORD_LENGTH):
            if guess[i] == secret[j] and not any(r.character == guess[i] and r.is_in_word for r in result[:i]):
                result[i].is_in_word = True
                break

    return result

# Display the game board with colored feedback
def display_results(guess_results):
    """
    Display the results of all guesses with color coding.

    Args:
        guess_results: List of lists containing LetterState objects for each guess
    """
    for guess in guess_results:
        # Display each letter with appropriate color based on its state
        for letter in guess:
            if letter.is_in_position:
                # Green background for correct position
                print(Back.GREEN + Fore.WHITE + letter.character + Style.RESET_ALL, end="")
            elif letter.is_in_word:
                # Yellow background for correct letter, wrong position
                print(Back.YELLOW + Fore.WHITE + letter.character + Style.RESET_ALL, end="")
            else:
                # Gray background for incorrect letter
                print(Back.LIGHTBLACK_EX + Fore.WHITE + letter.character + Style.RESET_ALL, end="")
        print()  # New line after each guess

# Main game function
def main():
    """
    Main game loop for Pydle.
    """
    # Load the word list and select a random target word
    word_list = load_word_list("data/pydle_words.txt")
    secret = random.choice(word_list)

    # Initialize game state
    attempts = 0
    has_won = False
    guess_results = []

    # Print welcome message and instructions
    print("Welcome to Pydle!")
    print(f"You have {MAX_ATTEMPTS} attempts to guess the {WORD_LENGTH}-letter word.")

    # Main game loop
    while attempts < MAX_ATTEMPTS and not has_won:
        # Get player's guess
        guess = input(f"\nAttempt {attempts + 1}/{MAX_ATTEMPTS}. Enter your guess: ").upper()

        # Validate the guess
        if len(guess) != WORD_LENGTH:
            print(f"Your guess must be {WORD_LENGTH} letters long. Try again.")
            continue

        if guess not in word_list:
            print("That's not in the word list. Try again.")
            continue

        # Process the guess and update game state
        result = process_guess(guess, secret)
        guess_results.append(result)
        attempts += 1

        # Display the current state of the game
        display_results(guess_results)

        # Check if the player has won
        if all(letter.is_in_position for letter in result):
            has_won = True
            print(f"\nCongratulations! You've guessed the word in {attempts} attempts.")

    # Game over - show the secret word if player didn't win
    if not has_won:
        print(f"\nGame over! The word was {secret}.")

# Run the game when the script is executed
if __name__ == "__main__":
    main()
