
PATH = "books/frankenstein.txt"

def main():
    with open(PATH) as f:
        #print(count_words(f.read()))
        #print(count_total_characters(f.read()))
        text = f.read()
        print_report(PATH, text, count_total_characters(text))

def count_words(text):
    return len(text.split())

def count_total_characters(text):
    frequencies = { }

    for c in text:
        c = c.lower()
        if(c in frequencies):
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    
    return frequencies

def sort_on(dict):
    return dict["num"]

def print_report(file, text, freq):
    freq_splits = []

    for entry in freq:
        entry_dict = { }
        entry_dict["name"] = entry
        entry_dict["num"] = freq[entry]
        freq_splits.append(entry_dict)

    freq_splits.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {file} ---")
    print(f"{count_words(text)} words found in the document\n")

    for entry in freq_splits:
        name = entry["name"]
        num = entry["num"]
        
        if(name.isalpha()):
            print(f"The '{name}' character was found {num} times")

    print("--- End report ---")

if(__name__ == "__main__"):
    main()