import sys
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    sorted_chars = get_sorted_chars(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_chars:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
    
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()