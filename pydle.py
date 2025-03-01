from letter_state import LetterState

class Pydle:
  """
  Main game class for Pydle, a word-guessing game similar to Wordle.
  Manages game state, processes guesses, and determines win conditions.
  """

  MAX_ATTEMPTS = 6  # Maximum number of guesses allowed
  WORD_LENGTH = 5   # Length of the target word

  def __init__(self, secret: str):
    """
    Initialize a new Pydle game.

    Args:
        secret: The target word that the player needs to guess
    """
    self.secret: str = secret.upper()  # Store the secret word in uppercase for consistency
    self.attempts = []  # List to track all word attempts made by the player

  def attempt(self, word: str):
    """
    Record a word attempt without processing the guess.

    Args:
        word: The word that the player guessed
    """
    word = word.upper()  # Convert to uppercase for consistency
    self.attempts.append(word)  # Add the attempt to the history

  def guess(self, word: str):
    """
    Process a guess and determine the state of each letter.

    Args:
        word: The word that the player guessed

    Returns:
        List of LetterState objects representing the state of each letter in the guess
    """
    word = word.upper()  # Convert to uppercase for consistency
    result = []  # List to store the state of each letter

    # Check each letter in the guessed word
    for i in range(self.WORD_LENGTH):
      character = word[i]
      letter = LetterState(character)  # Create a new LetterState for this character
      letter.is_in_word = character in self.secret  # Check if the letter appears anywhere in the secret word
      letter.is_in_position = character == self.secret[i]  # Check if the letter is in the correct position
      result.append(letter)

    return result

  @property
  def is_solved(self):
    """
    Check if the game has been solved.

    Returns:
        Boolean indicating whether the player has correctly guessed the word
    """
    return len(self.attempts) > 0 and self.attempts[-1] == self.secret

  @property
  def remaining_attempts(self) -> int:
    """
    Calculate how many attempts the player has left.

    Returns:
        Number of remaining attempts
    """
    return self.MAX_ATTEMPTS - len(self.attempts)

  @property
  def can_attempt(self):
    """
    Determine if the player can make another attempt.

    Returns:
        Boolean indicating whether the player can make another guess
    """
    return self.remaining_attempts > 0 and not self.is_solved
