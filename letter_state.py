class LetterState:
    """
    Represents the state of a letter in a word guessing game.
    Tracks whether a letter is in the target word and if it's in the correct position.
    """

    def __init__(self, character: str):
        """
        Initialize a new LetterState object.

        Args:
            character: A single letter to track the state for
        """
        self.character: str = character  # The letter this state represents
        self.is_in_word: bool = False    # Flag indicating if the letter appears anywhere in the target word
        self.is_in_position: bool = False  # Flag indicating if the letter is in the correct position

    def __repr__(self):
        """
        Provide a string representation of the LetterState object.

        Returns:
            A formatted string showing the letter and its current state
        """
        return f"[{self.character} is_in_word: {self.is_in_word} is_in_position: {self.is_in_position}]"
