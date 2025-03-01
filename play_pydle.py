from pydle import Pydle
from colorama import init, Fore
from typing import List
from pydle import LetterState
import random

init(autoreset=True)

def main():
  word_set = load_word_set("data/pydle_words.txt")
  secret = random.choice(list(word_set))
  pydle = Pydle(secret)

  while pydle.can_attempt:
    x = input("\nType your guess: ")

    if len(x) != pydle.WORD_LENGTH:
      print(Fore.RED + f"Word must be {pydle.WORD_LENGTH} characters long!")
      continue

    if not x.upper() in word_set:
      print(Fore.RED + f"{x} is not a valid word!")
      continue

    pydle.attempt(x)
    display_results(pydle)

  if pydle.is_solved:
    print("You've solved the puzzle")
  else:
    print("You have failed to solve the puzzle!")
    print(f"The secret word was: {pydle.secret}")


def display_results(pydle: Pydle):
  print("\nYour results so far...")
  print(f"\nYou have {pydle.remaining_attempts} attempts remaining. \n")

  lines = []

  for word in pydle.attempts:
    result = pydle.guess(word)
    coloured_result_str = convert_result_to_colour(result)
    lines.append(coloured_result_str)

  for _ in range(pydle.remaining_attempts):
    lines.append(" ".join(["_"] * pydle.WORD_LENGTH))
  draw_border_around(lines)


def convert_result_to_colour(result: List[LetterState]):
  result_with_colour = []
  for letter in result:
    if letter.is_in_position:
      colour = Fore.GREEN
    elif letter.is_in_word:
      colour = Fore.YELLOW
    else:
      colour = Fore.WHITE
    coloured_letter = colour + letter.character
    result_with_colour.append(coloured_letter)
  return " ".join(result_with_colour)


def draw_border_around(lines: List[str], size: int=9, padding: int=1):
  content_length = size + padding * 2
  top_border = "┌" + "─" * content_length + "┐"
  bottom_border = "└" + "─" * content_length + "┘"
  space = " " * padding
  print(top_border)
  for line in lines:
    print("│" + space + line + space + "│")

  print(bottom_border)


def load_word_set(path: str):
  word_set = set()
  with open(path, "r") as f:
    for line in f.readlines():
      word = line.strip().upper()
      word_set.add(word)
  return word_set

if __name__ == "__main__":
  main()
