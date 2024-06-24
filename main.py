
def count_characters(string):
    letters_count = {}
    for c in string:
        if c in letters_count:
            letters_count[c] += 1
        else:
            letters_count[c] = 1
    return letters_count

if __name__ == '__main__':
    book = "books/frankenstein.txt"

    with open(book) as f:
        file_contents = f.read()
        
        words = file_contents.split()
        word_count = len(words)

        character_counts = count_characters(file_contents.lower())
        filtered_characters = {k: v for k, v in character_counts.items() if k.isalpha()}
        sorted_characters = {k: v for k, v in sorted(filtered_characters.items(), key=lambda item: item[1], reverse=True)}

        print(f"--- Begin report of {book} ---")
        print(f"{word_count} words found in the document\n")

        for c in sorted_characters:
            print(f"The '{c}' character was found {sorted_characters[c]} times")
        print("--- End report ---")