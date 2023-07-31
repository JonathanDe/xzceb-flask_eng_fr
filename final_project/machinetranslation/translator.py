"""
Helper module to translate text
"""
from deep_translator import MyMemoryTranslator

# Function that translates english to french
def english_to_french(english_text):
    if isinstance(english_text, str) is False:
        raise ValueError('The value provided is not a string')
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

# Function that translates french to english
def french_to_english(french_text):
    if isinstance(french_text, str) is False:
        raise ValueError('The value provided is not a string')
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
