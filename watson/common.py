TEXTS = [
    "george_chapman",
    "alexander_pope",
    "william_cowper",
    "edward_earl_of_derby",
    "theodore_buckley",
    "lang_leaf_myers",
    "samuel_butler",
    "robert_fagels",
]


def read_file_raw(filename):
    # Return a string of the text in a plaintext file
    file = open(filename)
    return file.read()
