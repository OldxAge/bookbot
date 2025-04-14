from stats import count_words_in_string, character_frequency, bullshit
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("This only has", len(sys.argv), "arguments. It needs 2")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book: str = sys.argv[1]
    print("================ BOOKBOT =============")
    print("Analyzing book found at", book)
    print("------------ Word Count -------------")
    count_words_in_string(book)
    print("--------- Character Count -----------")
    charCount = character_frequency(book, 'et')
    for key, value in bullshit(charCount).items():
        print(f"{key}: {value}")
    print("--------- End -----------")

main()
