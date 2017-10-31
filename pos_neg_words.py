import bisect
import common

# This program is to analyze the frequency of positive and negative words in
# different translations of the Iliad


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
    for text in common.TEXTS:
        texts[text] = common.readFile("translations/cleaned/" + text + ".txt")
    print("[OK]")

    print("Evaluating texts: ", end='')
    # Process each text
    for text in texts:
        results[text] = (determineFrequency(texts[text], positive),
                         determineFrequency(texts[text], negative))
    print("  [OK]")

    print("Results:\n")
    print("Word count:")
    for text in texts:
        print("{0:22}".format(text) + "Word Count: " + (str)(len(texts[text])))
    print("\nSubjectivity:")
    table_data = []
    for text in texts:
        table_data.append((text, results[text][0] * 100, results[text][1] * 100, common.PUB_DATES[text]))
    table_data = sorted(table_data, key=lambda x: x[3])
    for item in table_data:
        print("{0:22}".format(item[0]) + "Pos: " + "%.4f" % (item[1]) +
              "\tNeg: " + "%.4f" % (item[2]))

main()
