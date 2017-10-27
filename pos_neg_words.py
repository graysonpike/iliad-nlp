import bisect

# This program is to analyze the frequency of positive and negative words in
# different translations of the Iliad

'''
TEXTS = [
    "alexander_pope",
    "edward_earl_of_derby",
    "george_chapman",
    "lang_leaf_myers",
    "samuel_butler",
    "theodore_buckley",
    "william_cowper"
]
'''
TEXTS = ["alexander_pope_b1"]


def loadWords():
    # Parsing function for the subjectivity dictionary
    # NOTE: In the future, incorporate strong/weak feature of dicitonary?
    # Return tuple of lists of strings:
    # e.g. (["good", "nice"]["bad", "ugly"])
    # Where the first element of the tuple contains positive words, and the
    # second contains negative words
    positive = []
    negative = []
    file = open("dictionaries/subjectivity_dict.tff", 'r')
    for line in file:
        # Remove the newline from this line
        line = line.rstrip()
        parts = line.split(' ')
        # format is priorpolarity=<positive/negative>, so we only want the
        # part following the equals sign
        # Make sure that the line is valid before parsing (len(parts) == 6)
        if(len(parts) == 6 and parts[5].split('=')[1] == "positive"):
            positive.append(parts[2].split('=')[1])
        else:
            negative.append(parts[2].split('=')[1])

    file.close()
    positive.sort()
    negative.sort()
    return (positive, negative)


def readFile(filename):
    # Parsing function for plaintext texts.
    # Return a list of strings, each word in the dictionary
    file = open(filename)
    words = []
    for line in file:
        line = line.rstrip()
        words += line.split(' ')

    # Make all words lowecase and remove punctuation
    for word in words:
        word = word.lower().strip(" ,.")

    # Remove empty lines
    words = list(filter(("").__ne__, words))
    return words


def determineFrequency(text, dictionary):
    # Return the frequency of words defined by the dictionary in the given text
    occurences = 0
    for word in text:
        # Determine if the word exists in the dictionary
        index = bisect.bisect_left(dictionary, word)
        if(index < len(dictionary)):
            if(dictionary[index] == word):
                # print word
                occurences += 1
    return occurences/(float)(len(text))


def main():

    results = {}

    print("Parsing dictionary: ", end='')
    # Populate list of pos/neg words
    (positive, negative) = loadWords()
    print("[OK]")

    print("Parsing plaintexts: ", end='')
    # Read files for all texts
    texts = {}
    for text in TEXTS:
        texts[text] = readFile("translations/books/1/" + text + ".txt")
    print("[OK]")

    print("Evaluating texts: ", end='')
    # Process each text
    for text in texts:
        results[text] = determineFrequency(texts[text], positive)
    print("[OK]")
    
    print("Results:")
    for result in results:
        print(result + ": " + (str)(results[result]))

main()
