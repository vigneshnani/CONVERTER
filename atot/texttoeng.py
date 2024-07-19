from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

def detect_language(text):
    """Detect the language of the text."""
    lang_info = translator.detect(text)
    return lang_info.lang

def translate_text(text, dest_language='en'):
    """Translate text to the destination language."""
    translated = translator.translate(text, dest=dest_language)
    print(f"Translated text: {translated.text}")
    return translated.text

def text_to_speech(text, lang='en'):
    """Convert text to speech."""
    tts = gTTS(text=text, lang=lang)
    tts.save("translated_audio.mp3")
    os.system("start translated_audio.mp3")  

def main():
    """Main function to run the text translator."""
    text = input("Please enter your text: ")
    
    if text:
        detected_language = detect_language(text)
        print(f"Detected language code: {detected_language}")
        
        # Translate text to English
        translated_text = translate_text(text, dest_language='en') 
        print(translated_text)
        
        # Convert translated text to speech
        text_to_speech(translated_text, lang='en')  

if __name__ == "__main__":
    main()
