from stats import get_num_words


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    file_path = "books/frankenstein.txt"
    file_content = get_book_text(file_path)
    num_words = get_num_words(file_content)
    print(f"{num_words} words found in the document")


main()
