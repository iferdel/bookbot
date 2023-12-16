def main():
    book_path = 'books/frankestein.txt'
    book_text = read_book(path=book_path)
    number_of_words = count_words(text=book_text)
    chars_dict = count_characters(text=book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"Number of characters in document: {number_of_words}")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report of {book_path} ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_characters(text):
    dict = {}
    text_lowercased = text.lower()
    for char in text_lowercased:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def count_words(text):
    words = text.split()
    return len(words)

def read_book(path):
    with open(path) as f:
        return f.read()

main()
