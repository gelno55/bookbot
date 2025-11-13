def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    num_chars = {}
    chars = text.lower()
    for char in chars:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sorted_chars(chars):
    char_list = [
        {"char": char, "num": count}
        for char, count in chars.items()
    ]

    def sort_on(item):
        return item["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list