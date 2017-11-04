# Program to determine the frequency of certain
# names in translations of the Iliad

import common
import sys


# keywords = [
#     "zeus",
#     "juno",
#     "jupiter",
#     "jove",
# ]

# keywords = [
#     "paris",
#     "alexander",
#     "alexandrus",
#     "alexandros",
# ]

# keywords = [
#     "diomedes",
#     "tydides",
#     "diomede",
#     "diomed",
# ]

keywords = [
    "agamemnon",
    "atrides"
]


def getOccurences(text, keywords):
    # Return a dictionary of keyword occurences in the given text
    occurences = {}
    for keyword in keywords:
        occurences[keyword] = 0
    for word in text:
        if(word in keywords):
            occurences[word] += 1
    return occurences


def main():

    # Read files for all texts
    print("Parsing plaintexts: ", end='')
    sys.stdout.flush()
    texts = {}
    for text in common.TEXTS:
        texts[text] = common.readFile("translations/cleaned/" + text + ".txt")
    print("[OK]")

    results = {}

    # Check # of occurences for each keyword in each text
    print("Evaluating texts:   ", end="")
    sys.stdout.flush()
    for text in texts:
        results[text] = getOccurences(texts[text], keywords)
    print("[OK]")

    # Add resulting data to a 2d array so that it can be sorted
    # by publication date
    table_data = []
    for text in results:
        line = "{0:30}".format(text)
        for keyword in keywords:
            line += "{0:15}".format("%3d" % results[text][keyword])
        table_data.append((line, common.PUB_DATES[text]))
    table_data = sorted(table_data, key=lambda x: x[1])

    # Print data in formatted table
    header = ("{0:30}".format("Translator"))
    for keyword in keywords:
        header += ("{0:15}".format(keyword))
    print(header)
    for item in table_data:
        print(item[0])

main()
