def get_words_count(text):
    num_words = text.split()
    return len(num_words)


def get_character_count(text):
    text = text.lower()
    character_dictionaries = {}
    for character in text:
        if character in character_dictionaries:
            character_dictionaries[character] += 1
        else:
            character_dictionaries[character] = 1
    return character_dictionaries
