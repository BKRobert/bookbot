def get_words_count(text):
    num_words = text.split()
    return len(num_words)


def get_character_count(text):
    text = text.lower()
    character_dictionary = {}
    for character in text:
        if character.isalpha():
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1
    return character_dictionary


def sort_dictionary(character_dictionary):
    return sorted(character_dictionary.items(), key=lambda item: item[1], reverse=True)
