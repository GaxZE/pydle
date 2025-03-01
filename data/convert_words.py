def main():
    # Define input and output file paths
    input_file_path = "data/words.txt"
    output_file_path = "data/pydle_words.txt"
    # Initialize empty list to store filtered words
    five_letter_words = []

    # Open the input file and read all words
    with open(input_file_path, "r") as f:
        for line in f.readlines():
            # Remove whitespace and newline characters
            word = line.strip()
            # Filter for words that are exactly 5 letters long
            if len(word) == 5:
                five_letter_words.append(word)

    # Write the filtered words to the output file
    with open(output_file_path, "w") as f:
        for word in five_letter_words:
            # Add each word with a newline character
            f.write(word + "\n")

    # Print summary of the operation
    print(f"Found {len(five_letter_words)} five-letter words")

# Standard Python idiom to run main() when script is executed directly
if __name__ == "__main__":
    main()
