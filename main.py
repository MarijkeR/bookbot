def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    wordcount = count_words(file_contents)
    characters = count_distinct_characters(file_contents)
        
    characters_list = []
    for entry in characters:
        characters_list.append({"char": entry, "num": characters[entry]})

    characters_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document")
    print()

    for item in characters_list:
        character = item["char"]
        count = item["num"]
        print(f"The '{character}' character was found {count} times")
        
    print("--- End report ---")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_distinct_characters(file_contents):
    file_contents = file_contents.lower()
    characters = {}
    for char in file_contents:
        if char.isalpha() == True:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

main()
