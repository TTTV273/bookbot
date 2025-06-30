def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def count_word(text):
    words = text.split()
    num_words = len(words)
    return num_words


def main():
    file_path = "books/frankenstein.txt"
    file_content = get_book_text(file_path)
    num_words = count_word(file_content)
    print(f"{num_words} words found in the document")


main()
