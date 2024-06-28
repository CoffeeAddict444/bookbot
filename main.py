def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    words = count_words(text)
    characters = count_characters(text)
    sort = sorting(characters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    for line in sort:
        print(line)
    print("--- End Report ---")


def book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letters_dict = {}
    alphabet = ["a","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
    lower_text = text.lower()
    for i in lower_text:
        if i in alphabet:
            if i in letters_dict:
                letters_dict[i] += 1
            else:
                letters_dict[i] = 1
    return letters_dict

def sorting(characters):
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    sorting_itteration = []
    for character, frequency in sorted_characters:
        sorting_itteration.append(f"The '{character}' character was found {frequency} times")
    return sorting_itteration


main()