# Program to determine frequencies of parts of speech in different translations of the Iliad

from nltk import word_tokenize, pos_tag, Text
import common
import sys


def get_tokens(filename):
    file = open(filename)
    raw = file.read()
    return word_tokenize(raw)


def main():

    print("Tokenizing texts...       ", end="")
    sys.stdout.flush()
    tokens = {}
    for text in common.TEXTS:
        tokens[text] = get_tokens("translations/cleaned/" + text + ".txt")
        # tokens[text] = get_tokens("novels/" + text + ".txt")
    print("[OK]")

    print("Tagging tokens for POS... ", end="")
    sys.stdout.flush()
    tags = {}
    for text in common.TEXTS:
        tags[text] = pos_tag(tokens[text])
    print("[OK]")

    print("Counting Words...         ", end="")
    sys.stdout.flush()
    not_words = "''(),--.:``$CD"
    total_words = {}
    for text in common.TEXTS:
        total_words[text] = 0
        for tag in tags[text]:
            if not (tag[1] in not_words):
                total_words[text] += 1
    print("[OK]")

    print("Counting POS...           ", end="")
    sys.stdout.flush()
    results = {}
    for text in common.TEXTS:
        nouns = 0
        adjectives = 0
        verbs = 0
        for tag in tags[text]:
            if(tag[1] == 'NN' or tag[1] == 'NNS' or tag[1] == 'NNP'):
                nouns += 1
            elif(tag[1] == 'JJ'):
                adjectives += 1
            elif(tag[1] == 'VB'):
                verbs += 1
        results[text] = [nouns / total_words[text], adjectives / total_words[text], verbs / total_words[text]]
    print("[OK]")

    for text in common.TEXTS:
        print(Text(tokens[text]).similar("achilles", 10))

    print("\nResults:")
    print("{0:25}".format("Translation") + "{:>15}".format("Nouns") + "{:>15}".format("Adjectives") + "{:>15}".format("Verbs"))
    for text in common.TEXTS:
        print("{0:25}".format(text), end="")
        for i in range(3):
            print("{:>15}".format("%.5f" % results[text][i]), end="")
        print("")


main()
