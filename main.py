from stats import get_num_words, get_num_char, sorted_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted = sorted_chars(num_chars)
    for sorted_char in sorted:
        if sorted_char["char"].isalpha():
            c = sorted_char["char"]
            n = sorted_char["num"]
            print(f"{c}: {n}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
