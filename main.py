from stats import get_book_text, count_words, count_characters, sort_on
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_file>")
        sys.exit(1)

    arg1 = sys.argv[1]

    file_contents = get_book_text(arg1)
    num_words = count_words(file_contents)
    num_chars = count_characters(file_contents)
    sorted_chars = sort_on(num_chars)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {arg1}")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character count ----------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['count']}")


main()
