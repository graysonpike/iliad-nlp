# iliad-nlp
Comparing different translations of the Iliad with NLP


### Project Information

Directory Structure

- `translations/`
    - `raw/` - UTF-8 Text as Provided by Project Gutenberg
    - `cleaned/` - Text suitable for analysis. Removed tags, footnotes, and illustration regerences
- `dictionaries/`
    - `subjectivity_dict.tff` - Formatted list of subjective english words. Tagged with strength, part-of-speech, word stem, and polarity.

Types of Analysis:

#### Positive/Negative Word Frequency
Each word in the text is categorized as positive, negative, or neutral. The ratio of positive to words to all words and the ratio of negative words to all words is reported for each translation.