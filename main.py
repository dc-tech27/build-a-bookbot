import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    report = print_report(book_path, num_words, chars_sorted_list)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in chars_sorted_list:
        if char_count[0].isalpha():
            print(f"{char_count[0]}: {char_count[1]}")
    print("============= END ===============")

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

main()