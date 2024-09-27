
def main():    
    path_to_file = './books/frankenstein.txt'
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")


    char_dict = get_char_dict(text)
    sorted_chars = sort_on(char_dict)
    
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print(char_dict)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    chars = {}
    
    for i in text:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1  # Increment the count if the character already exists as a key
        else:
            chars[lowered] = 1  # Add new character to dictionary with a count of 1
    
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(char_dict):
    sorted_chars = sorted(char_dict.items(), key = lambda item: item[1], reverse=True)
    return sorted_chars

main()

