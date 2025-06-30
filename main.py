import sys

from stats import convert_to_sorted_list, count_characters, get_num_words


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    file_content = get_book_text(file_path)
    num_words = get_num_words(file_content)

    char_list = convert_to_sorted_list(count_characters(file_content))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_info in char_list:
        char = char_info["char"]
        count = char_info["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()
