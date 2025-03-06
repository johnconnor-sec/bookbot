def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words


def count_characters(file_contents):
    characters = {}
    num_characters = file_contents.lower()
    for char in num_characters:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_on(characters):
    sort = []  # an empty list
    for char, count in characters.items():  # looping through the dictionary
        if char.isalpha():  # filtering for alphabetical characters
            sort.append(
                {"char": char, "count": count}
            )  # add a dictionary to the list for each character
    sort.sort(
        key=lambda x: x["count"], reverse=True
    )  # sorting grouped characters, greatest to least
    return sort
