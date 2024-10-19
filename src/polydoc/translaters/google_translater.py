from deep_translator import GoogleTranslator

class GoogleTranslater:
    @staticmethod
    def translate_to_portuguese(text, source_language: str = 'en') -> str:
        translator = GoogleTranslator(source=source_language, target='pt')
        translated_text = translator.translate(text)
        
        return translated_text
    
    