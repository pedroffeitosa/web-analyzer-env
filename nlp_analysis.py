from textblob import TextBlob
from textstat import textstat

def analyze_text(text):
    """
    Analyze the text for readability and sentiment.
    :param text: String text content.
    :return: Readability score and sentiment polarity.
    """
    readability = textstat.flesch_reading_ease(text)
    sentiment = TextBlob(text).sentiment.polarity  # -1 (negative) to 1 (positive)
    
    return readability, sentiment
