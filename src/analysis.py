from textblob import TextBlob
import re
import pandas as pd

# Emoji possibilities organized by subjectivity
first_subjectivity_layer = ["☹️", "🙁", "😑", "😐", "😏", "🙂"]
second_subjectivity_layer = ["😭", "😢", "😓", "😊", "😀", "😁"]
third_subjectivity_layer = ["🤬", "😡", "😠", "😄", "😅", "🤩"]

delim = '[.!;?\n\-,]'

class Analyzer:
    def __init__(self):
        self.sentiment_data = []

    def get_sentiment_data(self):
        return self.sentiment_data

    # Returns Emoji-ed version of the given text
    def get_output_text(self, input_text):
        split_text = re.split(delim, input_text)
        output_text = ""
        self.sentiment_data = []

        # Analyze each tokenized section in input text
        for section in split_text:
            if len(section.strip()) > 0:
                sentiment, new_text, emoji = self.analyze(section)
                output_text += new_text
                self.sentiment_data.append([section, emoji, sentiment.polarity, sentiment.subjectivity])

        return output_text

    # Analyzes a single section of input text
    def analyze(self, section_text):
        tb = TextBlob(section_text)

        subjectivity = tb.sentiment.subjectivity
        polarity = tb.sentiment.polarity

        layer = None
        emoji = None

        # Pick emoji to use for this sentence
        if subjectivity <= 1 / 3:
            layer = first_subjectivity_layer
        elif subjectivity <= 2 / 3:
            layer = second_subjectivity_layer
        else:
            layer = third_subjectivity_layer

        if polarity <= -2 / 3:
            emoji = layer[0]
        elif polarity <= -1 / 3:
            emoji = layer[1]
        elif polarity < 0:
            emoji = layer[2]
        elif polarity <= .33:
            emoji = layer[3]
        elif polarity <= .66:
            emoji = layer[4]
        else:
            emoji = layer[5]

        return (tb.sentiment, section_text + emoji, emoji)
