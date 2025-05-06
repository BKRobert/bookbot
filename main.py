import sys
from stats import get_words_count, get_character_count, sort_dictionary


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    num_words = get_words_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    character_count = get_character_count(text)
    sorted_dictionary = sort_dictionary(character_count)
    print("--------- Character Count -------")
    for char, count in sorted_dictionary:
        print(f"{char}: {count}")
    print("============= END ===============")


main()
