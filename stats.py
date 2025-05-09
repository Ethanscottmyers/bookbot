def get_num_words(book):
    return len(book.split())

def get_num_chars(book):
    chars = {}
    for char in book:
        char = char.lower()
        if (char in chars):
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_by_num(dict):
    return dict["num"]

def get_sorted_dicts(dict_chars):
    dicts = []
    for c, num in dict_chars.items():
        dicts.append({"char": c, "num": num})
    dicts.sort(reverse=True, key=sort_by_num)
    return dicts