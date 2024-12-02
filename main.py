print("hello world")

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{num_words} words found in the document")
    for c in chars_dict:
        print(f'The \'{c}\' character was found 46043 times')
    print('--- End report ---')

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()