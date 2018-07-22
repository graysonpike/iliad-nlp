from common import TEXTS
import json


# def main():

#     for text in TEXTS:
#         print("\nSummary for " + text)
        
#         averages = {
#             'sadness': 0,
#             'disgust': 0,
#             'joy': 0,
#             'anger': 0,
#             'fear': 0
#         }

#         results = json.load(open(text + '.results.json'))

#         for result in results:
#             for key in averages:
#                 averages[key] += result[key]

#         print("Averages: ")
#         for key in averages:
#             averages[key] = averages[key] / len(results)
#             print(key + ": " + str(averages[key]))


def main():
    for text in TEXTS:
        
        results = json.load(open(text + '.results.json'))
        average = 0
        for result in results:
            averages += result['anger']


main()