def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars