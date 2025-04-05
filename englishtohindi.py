import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Create Recognizer and Translator instances
recognizer = sr.Recognizer()
translator = Translator()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening for your speech...")
        audio = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio)
            return recognized_text.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Main loop
while True:
    print("Say 'translate' to start the translation process or 'exit' to quit.")
    command = recognize_speech()

    if command:
        if 'translate' in command:
            print("Please say the sentence you want to translate...")
            sentence = recognize_speech()
            if sentence:
                print(f"Translating: {sentence}")
                translated = translator.translate(sentence, dest='hi')  # Change 'hi' to your desired language code
                print(f"Translated Text: {translated.text}")

                # Convert translated text to speech
                tts = gTTS(text=translated.text, lang='hi')
                tts.save("translated_voice.mp3")
                os.system("start translated_voice.mp3")  # Adjust for your OS
        elif 'exit' in command:
            print("Exiting the program.")
            break