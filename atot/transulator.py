import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
recognizer = sr.Recognizer()
translator = Translator()
def record_audio():
    """Record audio from the microphone and return the audio data."""
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source)
    return audio_data

def transcribe_audio(audio_data):
    """Convert audio to text."""
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there was a problem with the request.")
        return None

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
    """Main function to run the voice translator."""
    audio_data = record_audio()
    text = transcribe_audio(audio_data)
    
    if text:
        
        detected_language = detect_language(text)
        print(f"Detected language code: {detected_language}")
        
        # Translate text to English
        translated_text = translate_text(text, dest_language='en') 
        
        # Convert translated text to speech
        text_to_speech(translated_text, lang='en')  

if __name__ == "__main__":
    main()
