from stats import get_words_count, get_character_count


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_words_count(text)
    character_count = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(character_count)


main()
