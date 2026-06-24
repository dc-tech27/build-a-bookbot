def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = text.split()
    print(f"Found {len(num_words)} total words")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

main()