import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        english_text = 'Hello'
        expected_translation = 'Bonjour'
        translation = englishToFrench(english_text)
        self.assertEqual(translation, expected_translation)
    
    def test_english_to_french_wrong_value(self):
        wrong_value = 2
        with self.assertRaises(ValueError) as exception_context:
            englishToFrench(wrong_value)
        self.assertEqual(
            str(exception_context.exception),
            'The value provided is not a string'
        )

    def test_french_to_english(self):
        french_text = 'Bonjour'
        expected_translation = 'Hello'
        translation = frenchToEnglish(french_text)
        self.assertEqual(translation, expected_translation)

    def test_french_to_english_wrong_value(self):
        wrong_value = 2
        with self.assertRaises(ValueError) as exception_context:
            frenchToEnglish(wrong_value)
        self.assertEqual(
            str(exception_context.exception),
            'The value provided is not a string'
        )

if __name__ == '__main__': 
    unittest.main()