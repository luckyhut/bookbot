def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print_word_count(words)
        print_letters_count(words)

def print_word_count(words):
    word_count = 0
    for word in words:
        word_count += 1
    print("There are", word_count, "words.")

def print_letters_count(words):
    letters_dict = {}
    for word in words:
        lowercase = word.lower()
        for letter in lowercase:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1

    sorted_letters = []
    for letter in letters_dict:
        sorted_letters.append({"letter": letter, "count": letters_dict[letter]})

    sorted_letters.sort(reverse=True, key=sort_helper)
    
    for i in range(0, len(sorted_letters)):
        if sorted_letters[i]["letter"].isalpha:
            letter = sorted_letters[i]["letter"]
            count = sorted_letters[i]["count"]
            print(f"The letter \'{ letter }\' was found a total of", count, "times.")
            
def sort_helper(dict):
    return dict["count"]
    
main()
