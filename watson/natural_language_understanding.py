# Script to upload large sections of text to IBM Watson Natural Language Understanding

import json
import sys
from common import read_file_raw, TEXTS

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions


def is_chunk_too_large(chunk):
    # Takes a list of strings representing a chunk
    # If the chunk has more than 10,000 characters, it is too large
    total_chars = 0
    for line in chunk:
        total_chars += len(line)
    return total_chars > 10000


def create_chunks(filename):
    # Read file as list of lines (strings)
    lines = read_file_raw(filename).split('\n')
    for line in lines:
        line += ' '

    # Chunks are sequential sections of the total text that fit within
    # the max char limit of the Watson API
    chunks = []
    current_chunk = 0
    chunks.append([])
    while len(lines) > 0:
        # Add line to chunk from queue
        chunks[current_chunk].append(lines[0])
        # If the chunk is too large, remove the added line and create new chunk
        if(is_chunk_too_large(chunks[current_chunk])):
            # Delete line just added to current chunk
            del chunks[current_chunk][-1]
            chunks.append([])
            current_chunk += 1
        # Otherwise, delete the line from the queue and repeat
        else:
            del lines[0]
    return chunks


def get_chunk_as_string(chunk):
    # Return the chunk (list of strings) as one string
    result = ""
    for line in chunk:
        result += line
    return result


def analyze(instance, chunk):
    response = instance.analyze(
        text=get_chunk_as_string(chunk),
        features=Features(
            emotion=EmotionOptions()))
    return response['emotion']['document']['emotion']


def process_text(text):

    credentials = json.load(open('ibm_cloud_credentials.json'))['natural-language-understanding']

    instance = NaturalLanguageUnderstandingV1(
        username=credentials['username'],
        password=credentials['password'],
        version='2018-03-16')

    chunks = create_chunks('../translations/cleaned/' + text + '.txt')
    results = []
    for chunk in chunks:
        results.append(analyze(instance, chunk))

    outfile = open(text + '.results.json', 'w')
    json.dump(results, outfile)

    # averages = {
    #     'sadness': 0,
    #     'disgust': 0,
    #     'joy': 0,
    #     'anger': 0,
    #     'fear': 0
    # }

    # print("Chunk Values: ")
    # for key in averages:
    #     print(key)
    #     for result in results:
    #         print(result[key])

    # for result in results:
    #     for key in averages:
    #         averages[key] += result[key]

    # print("Averages: ")
    # for key in averages:
    #     averages[key] = averages[key] / len(chunks)
    #     print(key + ": " + str(averages[key]))


def main():

    for text in TEXTS:
        print("Processing " + text + "... ", end='')
        sys.stdout.flush()
        process_text(text)
        print("DONE")


main()