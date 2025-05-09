from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    args = sys.argv
    if (len(args) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = args[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_counts = get_sorted_dicts(get_num_chars(text))
    output = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
"""
    for char in char_counts:
        if (char["char"].isalpha()):
            output += f"{char["char"]}: {char["num"]}\n"
    output += "============= END ==============="
    print(output)
main()