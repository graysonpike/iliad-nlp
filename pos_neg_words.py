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
    # Return tuple of lists of strings:
    # e.g. (["good", "nice"]["bad", "ugly"])
    # Where the first element of the tuple contains positive words, and the
    # second contains negative words
    positive = []
    negative = []
    file = open("dictionaries/subjectivity_dict.tff", 'r')
    for line in file:
        line = line.rstrip()
        parts = line.split(' ')
        # format is priorpolarity=<positive/negative>, so we only want the
        # part following the equals sign
        if(len(parts) == 6 and parts[5].split('=')[1] == "positive"):
            positive.append(parts[2].split('=')[1])
        else:
            negative.append(parts[2].split('=')[1])

    return (positive, negative)


def readFile(filename):
    # Return string of the entire text in the file
    return


def determineFrequency(text, dict):
    # Return the frequency of words defined by dict
    return


def main():

    print("Loading dictionary:")
    # Populate list of pos/neg words
    (positive, negative) = loadWords()

    # Read files for all texts
    texts = {}
    for text in TEXTS:
        texts[text] = readFile("translations/books/" + text + "_b1.txt")

    # Process each text
    for text in texts:
        determineFrequency(texts[text], positive)

main()
