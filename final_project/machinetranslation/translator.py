from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    if type(englishText) != str:
        raise ValueError('The value provided is not a string')
    frenchText = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(englishText)
    return frenchText


def frenchToEnglish(frenchText):
    if type(frenchText) != str:
        raise ValueError('The value provided is not a string')
    englishText = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchText)
    return englishText
