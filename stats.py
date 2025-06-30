def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def sort_on(items):
    return items["num"]


def convert_to_sorted_list(char_dict):
    char_list = []

    for char in char_dict:
        char_info = {"char": char, "num": char_dict[char]}
        char_list.append(char_info)

    char_list.sort(reverse=True, key=sort_on)

    return char_list
