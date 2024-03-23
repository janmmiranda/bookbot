def main():
    bookPath = "books/frankensteint.txt"
    text = getBookText(bookPath)
    wordCount = getWordsCount(text)
    charsDict = getLettersCount(text)
    sorted = sortDict(charsDict)
    createReport(bookPath, wordCount, sorted)
    # print(text)
    # print("Book has {} words!".format(wordCount))
    # print(charsDict)
    

def getBookText(path):
    with open(path) as f:
        return f.read()
    
def getWordsCount(text):
    words = text.split()
    return len(words)

def getLettersCount(text):
    chars = {}
    for i in text:
        lowered = i.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sortOn(dict):
    return dict["count"]

def sortDict(dict):
    res = []
    for key in dict:
        temp = {}
        temp["char"] = key
        temp["count"] = dict[key]
        res.append(temp)
    
    res.sort(reverse=True, key=sortOn)

    return res

def createReport(path, count, list):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    for line in list:
        letter = line["char"]
        letterCount = line["count"]
        print(f"The '{letter}' character was found {letterCount} times")
    print("--- End report ---")

main()