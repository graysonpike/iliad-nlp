# Program to determine the frequency of certain
# names in translations of the Iliad

import common

'''
keywords = [
    "achilles",
    "helen",
    "priam",
    "paris",
    "agamemnon",
    "hector",
    "atrides"
]
'''

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
    results = []
    for keyword in occurences:
        results.append([keyword, occurences[keyword]])
    return sorted(results, key=lambda x: x[1], reverse=True)


def main():

    print("Parsing plaintexts: ", end='')
    # Read files for all texts
    texts = {}
    for text in common.TEXTS:
        texts[text] = common.readFile("translations/cleaned/" + text + ".txt")
    print("[OK]")

    results = {}

    for text in texts:
        results[text] = getOccurences(texts[text], keywords)

    for text in results:
        print("{0:18}".format(text))
        for result in results[text]:
            print("\t{0:12}".format(result[0]) + str(result[1]))

main()
