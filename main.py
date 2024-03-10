import os
import string


PATH_TO_BOOKS = "books/"

def count_words(contents):
    return len(contents.split())

def count_letters(contents):
    lower_contents = contents.lower()
    letters = string.ascii_lowercase
    results = {}
    for letter in letters:
        results[letter] = lower_contents.count(letter)
    return results

def report_character_count(character_counts):
    sorted_counts = [{"character":key, "count":value} for key, value in character_counts.items()]
    sorted_counts.sort(reverse=True, key=lambda x: x.get("count"))
    for char_count in sorted_counts:
        print(f"The '{char_count.get('character')}' character was found {char_count.get('count')} times")

def main():
    books = [f"{PATH_TO_BOOKS}{book}" for book in os.listdir(PATH_TO_BOOKS)]
    for book in books:
        with open(book,'r') as bfile:
            contents = bfile.read()
            print(contents)
            print(f"There are {count_words(contents)} words in {book.split('/')[-1]}")
            character_counts = count_letters(contents)
            report_character_count((character_counts))


if __name__ == "__main__":
    main()
