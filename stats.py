def count_words_in_string(filepath):
    wordCount = 0
    with open(filepath) as file:
        contents = file.read()
        wordCount = len(contents.split())
    print('Found', wordCount, 'total words')

def character_frequency(filepath: str, searchText: str) -> dict:
    freq_dict = {char: 0 for char in searchText.lower()}
    with open(filepath) as file:
        contents = file.read()
        for bookChar in contents.lower():
            if bookChar in freq_dict:
                freq_dict[bookChar] += 1
    return freq_dict

def bullshit(charCountDict: dict) -> dict:
    sortedDict = dict(sorted(charCountDict.items(), key=lambda item: item, reverse=True))
    return sortedDict